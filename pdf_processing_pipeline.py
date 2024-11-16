import csv
from datetime import datetime
import gc
import hashlib
import json
import os
import random
import re
import shutil
import tempfile
import time
import traceback
import xml.etree.ElementTree as ET
from xml.dom import minidom

import fitz  # PyMuPDF
import pandas as pd
import pdfplumber
import PIL.Image
from joblib import Parallel, delayed
from tqdm import tqdm
from ultralytics import YOLO

_yolo_model = None


def format_time(seconds):
    """Format time to 2 decimal places"""
    return f"{seconds:.2f}"


# PDF Processing Functions
def clean_cell(cell):
    """Clean text cell content by removing newlines"""
    if cell is None:
        return ""
    return cell.replace("\n", " ")


def pdf_to_jpg(pdf_path, output_images):
    """Convert PDF pages to JPG images"""
    os.makedirs(output_images, exist_ok=True)
    doc = fitz.open(pdf_path)
    jpg_count = 0
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    try:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            output_path = os.path.join(
                output_images, f"{base_name}_page{page_num + 1}.jpg"
            )
            pix.save(output_path)
            jpg_count += 1
    finally:
        doc.close()
    return jpg_count


def extract_text_tables_and_save(pdf_path, output_directory):
    """Extract text and table coordinates, saving to TSV files"""
    os.makedirs(output_directory, exist_ok=True)
    global_table_counter = 1
    pdf_basename = os.path.splitext(os.path.basename(pdf_path))[0]

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, plumb_page in enumerate(pdf.pages):
            # Save coordinates of text and tables
            coord_tsv_filename = os.path.join(
                output_directory, f"{pdf_basename}_page{page_num + 1}.tsv"
            )
            with open(
                coord_tsv_filename, "w", newline="", encoding="utf-8"
            ) as coord_file:
                writer = csv.writer(coord_file, delimiter="\t")
                writer.writerow(["text", "x1", "y1", "x2", "y2"])
                tables = plumb_page.find_tables()
                if tables:
                    for i, table in enumerate(tables):
                        x1, y1, x2, y2 = table.bbox
                        writer.writerow(
                            [f"table_{global_table_counter + i}", x1, y1, x2, y2]
                        )

            # Save table contents
            for i, table in enumerate(tables):
                tsv_content = [
                    clean_cell(cell) for row in table.extract() for cell in row
                ]
                table_tsv_filename = os.path.join(
                    output_directory,
                    f"{pdf_basename}_page{page_num+1}_table{global_table_counter}.tsv",
                )
                with open(
                    table_tsv_filename, "w", newline="", encoding="utf-8"
                ) as tsv_file:
                    writer = csv.writer(tsv_file, delimiter="\t")
                    writer.writerows([[cell] for cell in tsv_content])

                global_table_counter += 1


def process_single_pdf(pdf_path, output_directory):
    """Process a single PDF file"""
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_output_directory = os.path.join(output_directory, base_name + "_output")

    try:
        # Extract text and tables
        extract_text_tables_and_save(pdf_path, pdf_output_directory)

        # Create images
        output_images = os.path.join(pdf_output_directory, base_name + "_images")
        jpg_count = pdf_to_jpg(pdf_path, output_images)

        return jpg_count
    except Exception as e:
        with open("processing_errors.log", "a") as log_file:
            log_file.write(f"Error processing {pdf_path}: {str(e)}\n")
            traceback.print_exc(file=log_file)
        return 0


def process_pdf_directory(input_path, output_directory, pdf_chunk_size=25):
    """Process all PDFs in the input directory"""
    start_time = time.time()

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get all PDF files in the input directory
    pdf_paths = [
        os.path.join(input_path, f)
        for f in os.listdir(input_path)
        if f.endswith(".pdf")
    ]
    total_jpg_count = 0

    # Process PDFs in chunks to manage memory
    for start_idx in range(0, len(pdf_paths), pdf_chunk_size):
        end_idx = start_idx + pdf_chunk_size
        pdf_chunk = pdf_paths[start_idx:end_idx]

        # Process chunk in parallel
        chunk_jpg_count = sum(
            Parallel(n_jobs=4)(
                delayed(process_single_pdf)(pdf_path, output_directory)
                for pdf_path in tqdm(pdf_chunk, desc="Processing PDFs")
            )
        )
        total_jpg_count += chunk_jpg_count

        # Clean up memory
        gc.collect()

    end_time = time.time()
    total_time = end_time - start_time
    avg_time_per_page = total_time / total_jpg_count if total_jpg_count else 0

    print(f"Total pages processed: {total_jpg_count}")
    print(f"Total processing time: {total_time:.2f} seconds")
    print(f"Average time per page: {avg_time_per_page:.2f} seconds/page")

    return total_jpg_count, total_time, avg_time_per_page


# Image Processing Functions
def load_yolo_model(model_path):
    """Load YOLO model if not already loaded"""
    print("Loading YOLO model...")
    global _yolo_model
    if _yolo_model is None:
        _yolo_model = YOLO(model_path)
    return _yolo_model


def unload_yolo_model():
    """Unload YOLO model from memory."""
    print("Unloading YOLO model...")
    global _yolo_model
    _yolo_model = None
    gc.collect()  # Force garbage collection to free up memory


def process_image_batch(image_batch, output_folder, model_path):
    """Process a batch of images using YOLO model"""
    model = load_yolo_model(model_path)
    results = model(image_batch, conf=0.12, imgsz=640)

    for img_path, result in zip(image_batch, results):
        boxes = result.boxes.xyxy.numpy()
        class_ids = result.boxes.cls.numpy()
        confidences = result.boxes.conf.tolist()
        names = result.names
        data = []

        for box, class_id, confidence in zip(boxes, class_ids, confidences):
            x1, y1, x2, y2 = box
            class_id = int(class_id)
            class_name = names[class_id]
            data.append([x1, y1, x2, y2, confidence, class_id, class_name])

        df = pd.DataFrame(
            data,
            columns=["x1", "y1", "x2", "y2", "confidence", "class_id", "class_name"],
        )
        df = df.sort_values("y1")  # Sort by y1 column
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        output_path = os.path.join(output_folder, f"{base_name}.tsv")
        df.to_csv(output_path, sep="\t", index=False)

        # Clear memory for this iteration
        del boxes, class_ids, confidences, data, df

    # Clear batch results
    del results
    gc.collect()


def process_images_in_output_folder(output_folder, model_path, batch_size=10):
    """Process all images in a specific output folder"""
    image_folder = os.path.join(
        output_folder, f"{os.path.basename(output_folder[:-7])}_images"
    )
    if not os.path.exists(image_folder):
        return 0, 0

    results_yolo_folder = os.path.join(output_folder, "results_yolo")
    os.makedirs(results_yolo_folder, exist_ok=True)
    image_files = [
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if os.path.isfile(os.path.join(image_folder, f)) and f.lower().endswith(".jpg")
    ]

    start_time = time.time()
    # batch_size = 10  # Adjusted for CPU processing

    for i in range(0, len(image_files), batch_size):
        batch = image_files[i : i + batch_size]
        process_image_batch(batch, results_yolo_folder, model_path)

        # Clear memory after each batch
        gc.collect()

    end_time = time.time()
    return len(image_files), end_time - start_time


def process_images_directory(output_directory, model_path, batch_size=10):
    """Process all images in all output directories"""
    total_images_processed = 0
    total_time_spent = 0.0

    for entry in os.listdir(output_directory):
        path = os.path.join(output_directory, entry)
        if os.path.isdir(path) and path.endswith("_output"):
            images_processed, time_spent = process_images_in_output_folder(
                path, model_path, batch_size=batch_size
            )
            total_images_processed += images_processed
            total_time_spent += time_spent

    avg_time_per_image = (
        total_time_spent / total_images_processed if total_images_processed > 0 else 0
    )

    print(f"Total JPEG images processed: {total_images_processed}")
    print(f"Total processing time: {total_time_spent:.2f} seconds")
    print(f"Average time per JPEG image: {avg_time_per_image:.2f} seconds")

    return total_images_processed, total_time_spent, avg_time_per_image


# Text Extraction Functions
def extract_text_from_pdf(pdf_path, page_num, boxes):
    """Extract text from specific regions of a PDF page"""
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)
    texts = []
    for box in boxes:
        rect = fitz.Rect(box[:4])
        text = page.get_text("text", clip=rect)
        texts.append(text)
    doc.close()
    return texts


def create_cvat_task_xml(output_directory, task_name):
    """Create CVAT task XML from processed data"""
    root = ET.Element("annotations")
    version = ET.SubElement(root, "version")
    version.text = "1.1"

    image_id = 0
    for entry in os.listdir(output_directory):
        pdf_output_dir = os.path.join(output_directory, entry)
        if os.path.isdir(pdf_output_dir) and pdf_output_dir.endswith("_output"):
            base_name = entry[:-7]  # Remove '_output' from the end
            final_dir = os.path.join(pdf_output_dir, "final")
            images_dir = os.path.join(pdf_output_dir, base_name + "_images")

            if os.path.exists(final_dir) and os.path.exists(images_dir):
                for tsv_file in sorted(os.listdir(final_dir)):
                    if tsv_file.startswith("combined_page") and tsv_file.endswith(
                        ".tsv"
                    ):
                        page_num = tsv_file.split("page")[1].split(".")[0]
                        tsv_path = os.path.join(final_dir, tsv_file)
                        df = pd.read_csv(tsv_path, sep="\t", encoding="utf-8")

                        image_name = f"{base_name}_page{page_num}.jpg"
                        image_path = os.path.join(images_dir, image_name)

                        if os.path.exists(image_path):
                            with PIL.Image.open(image_path) as img:
                                width, height = img.size

                            image = ET.SubElement(
                                root,
                                "image",
                                {
                                    "id": str(image_id),
                                    "name": image_name,
                                    "width": str(width),
                                    "height": str(height),
                                },
                            )

                            for _, row in df.iterrows():
                                if (
                                    pd.isna(row["class_name"])
                                    or pd.isna(row["x1"])
                                    or pd.isna(row["y1"])
                                    or pd.isna(row["x2"])
                                    or pd.isna(row["y2"])
                                ):
                                    continue

                                ET.SubElement(
                                    image,
                                    "box",
                                    {
                                        "label": str(row["class_name"]),
                                        "xtl": str(row["x1"]),
                                        "ytl": str(row["y1"]),
                                        "xbr": str(row["x2"]),
                                        "ybr": str(row["y2"]),
                                        "occluded": "0",
                                        "z_order": "0",
                                    },
                                )

                            image_id += 1

    xml_str = ET.tostring(root, encoding="unicode")
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ")

    cvat_directory = os.path.join(output_directory, "cvat")
    os.makedirs(cvat_directory, exist_ok=True)
    xml_output_path = os.path.join(cvat_directory, f"{task_name}.xml")

    with open(xml_output_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    return xml_output_path


def process_page_for_text(pdf_path, page_num, base_output_directory):
    """Process a single page for text extraction"""
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)

    base_name = os.path.basename(pdf_path)[:-4]  # Remove '.pdf'
    page_df_path = os.path.join(
        base_output_directory, f"results_yolo/{base_name}_page{page_num+1}.tsv"
    )
    bareme_df_path = os.path.join(
        base_output_directory, f"{base_name}_page{page_num+1}.tsv"
    )

    tsv_files_produced = 0

    if os.path.exists(page_df_path) and os.path.exists(bareme_df_path):
        page_df = pd.read_csv(page_df_path, delimiter="\t")
        bareme_df = pd.read_csv(bareme_df_path, delimiter="\t")

        filter_strings = "(MainZone|MarginText|Title|TableZone|GraphicZone)"
        page_df = page_df[
            page_df["class_name"].str.contains(filter_strings, case=False, regex=True)
        ]

        boxes = page_df[["x1", "y1", "x2", "y2"]].values.tolist()
        texts = extract_text_from_pdf(pdf_path, page_num, boxes)

        page_df["text"] = texts
        page_df.sort_values(
            by="class_name", ascending=True, key=lambda x: x.str.contains("MainZone")
        )

        page_df["text_no_spaces"] = page_df["text"].apply(lambda x: "".join(x.split()))
        page_df.drop_duplicates(subset=["text_no_spaces"], keep="first", inplace=True)
        page_df.drop(columns=["text_no_spaces"], inplace=True)

        combined_df = pd.concat([bareme_df, page_df], axis=0, ignore_index=True)
        combined_df.sort_values(by="y1", inplace=True)

        new_output_directory = os.path.join(base_output_directory, "final")
        os.makedirs(new_output_directory, exist_ok=True)

        combined_df_output_path = os.path.join(
            new_output_directory, f"combined_page{page_num+1}.tsv"
        )
        combined_df.to_csv(combined_df_output_path, sep="\t", index=False)
        tsv_files_produced = 1

    doc.close()
    return tsv_files_produced


def process_all_pages_parallel(pdf_path, base_output_directory):
    """Process all pages of a PDF in parallel"""
    start_time = time.time()
    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    doc.close()

    results = Parallel(n_jobs=4)(
        delayed(process_page_for_text)(pdf_path, page_num, base_output_directory)
        for page_num in range(num_pages)
    )

    total_tsv_files_produced = sum(results)
    end_time = time.time()
    return end_time - start_time, total_tsv_files_produced


def process_directory_for_text_extraction(output_directory, input_directory):
    """Process all PDFs in the directory for text extraction"""
    total_tsv_files = 0
    total_time = 0.0
    files_processed = 0
    last_gc_threshold = 0

    for pdf_file in os.listdir(input_directory):
        if pdf_file.endswith(".pdf"):
            base_name = pdf_file[:-4]
            output_dir = os.path.join(output_directory, f"{base_name}_output")

            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            pdf_path = os.path.join(input_directory, pdf_file)
            processing_time, tsv_files_produced = process_all_pages_parallel(
                pdf_path, output_dir
            )
            total_tsv_files += tsv_files_produced
            total_time += processing_time
            files_processed += 1

            if files_processed // 10 > last_gc_threshold:
                gc.collect()
                print("Garbage Collected!")
                last_gc_threshold = files_processed // 10

    print(f"Total combined_pageX.tsv files produced: {total_tsv_files}")
    print(f"Total processing time: {total_time:.2f} seconds")
    if total_tsv_files > 0:
        print(
            f"Average processing time per file: {total_time / total_tsv_files:.2f} seconds"
        )
    else:
        print("No files were produced.")

    task_name = "multi_document_task"
    cvat_xml_path = create_cvat_task_xml(output_directory, task_name)
    print(f"CVAT task XML file created: {cvat_xml_path}")

    return total_tsv_files, total_time, cvat_xml_path


# TSV to JSON Processing Functions
def generate_hash():
    """Generate a random hash for document identification"""
    random_string = str(random.randint(0, 1000000))
    return hashlib.md5(random_string.encode()).hexdigest()[:16]


def classify_class_name(class_name):
    """Classify the type of content based on class name"""
    if pd.isnull(class_name) or class_name == "":
        return "Blank"
    elif "MarginText" in class_name:
        return "Margin"
    elif class_name == "MainZone-Head" or "Title" in class_name:
        if class_name not in ["RunningTitleZone", "PageTitleZone-Index"]:
            return "Special"
    return "Regular"


def split_text(text, max_words=400):
    """Split text into chunks by sentences, respecting max word limit"""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        sentence_word_count = len(sentence.split())
        if current_word_count + sentence_word_count > max_words and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_word_count = 0

        current_chunk.append(sentence)
        current_word_count += sentence_word_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def count_total_files(root_directory):
    """Count total TSV files to process"""
    total = 0
    for subdir, _, files in os.walk(root_directory):
        if subdir.endswith("final") and "_output" in subdir:
            total += len([f for f in files if f.endswith(".tsv")])
    return total


def parse_tsvs_to_json(directory):
    """Parse TSV files in a directory to JSON format"""
    try:
        tsv_files = sorted(
            [f for f in os.listdir(directory) if f.endswith(".tsv")],
            key=lambda x: int(re.search(r"combined_page(\d+).tsv", x).group(1)),
        )

        if not tsv_files:
            return None, 0

        full_document_name = os.path.basename(os.path.dirname(directory))
        document_name = full_document_name.replace("_output", "")
        json_data = []
        current_section = None
        current_text = ""
        current_chunk_pages = []

        for file_name in tsv_files:
            try:
                page_number = re.search(r"combined_page(\d+).tsv", file_name).group(1)
                file_path = os.path.join(directory, file_name)

                df = pd.read_csv(file_path, sep="\t", encoding="utf-8")
                df["Category"] = df["class_name"].apply(classify_class_name)
                df["text"] = df["text"].astype(str)

                for _, row in df.iterrows():
                    category = row["Category"]
                    text = row["text"].strip()

                    if category in ["Blank", "Margin"]:
                        json_data.append(
                            {
                                "section": text,
                                "text": text,
                                "pages": [page_number],
                                "document": document_name,
                                "word_count": len(text.split()),
                                "hash": generate_hash(),
                            }
                        )
                    elif category == "Special":
                        if current_section is not None and current_text:
                            for chunk in split_text(current_text):
                                json_data.append(
                                    {
                                        "section": current_section,
                                        "text": chunk,
                                        "pages": current_chunk_pages,
                                        "document": document_name,
                                        "word_count": len(chunk.split()),
                                        "hash": generate_hash(),
                                    }
                                )
                        current_section = text
                        current_text = ""
                        current_chunk_pages = [page_number]
                    else:
                        if current_section is None:
                            current_section = text
                        current_text = (
                            current_text + " " + text if current_text else text
                        )
                        if page_number not in current_chunk_pages:
                            current_chunk_pages.append(page_number)

            except Exception as e:
                print(f"Error processing file {file_name}: {str(e)}")
                continue

        # Save JSON file
        json_file_name = f"{document_name}.json"
        json_file_path = os.path.join(directory, json_file_name)
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        return json_file_path, len(tsv_files)

    except Exception as e:
        print(f"Error processing directory {directory}: {str(e)}")
        return None, 0


def process_tsv_directory(output_directory):
    """Process all TSV files in the output directory"""
    print("Step 1: Processing TSV files to JSON...")
    final_directories = []
    json_files = []

    for subdir, dirs, files in os.walk(output_directory):
        if subdir.endswith("final") and "_output" in subdir:
            final_directories.append(subdir)

    if not final_directories:
        print("No final directories found for TSV processing.")
        return None

    total_files = count_total_files(output_directory)
    print(
        f"Found {total_files} TSV files to process in {len(final_directories)} directories"
    )

    start_time = time.time()  # Changed from time() to time.time()
    files_processed = 0

    for directory in tqdm(final_directories, desc="Processing directories"):
        json_file_path, tsv_count = parse_tsvs_to_json(directory)
        if json_file_path:
            json_files.append(json_file_path)
            files_processed += tsv_count

        if len(json_files) % 10 == 0:
            gc.collect()

    end_time = time.time()  # Changed from time() to time.time()
    total_time = end_time - start_time

    return {
        "json_files": json_files,
        "files_processed": files_processed,
        "total_time": total_time,
        "avg_time": total_time / files_processed if files_processed > 0 else 0,
    }


def merge_json_files(json_files, output_file):
    """Merge multiple JSON files into a single output file"""
    print("\nStep 2: Merging all JSON files...")
    combined_data = []

    with tqdm(total=len(json_files), desc="Merging JSON files") as pbar:
        for json_file in json_files:
            try:
                with open(json_file, "r") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        combined_data.extend(data)
                    elif isinstance(data, dict):
                        combined_data.append(data)
            except Exception as e:
                print(f"Error processing {json_file}: {str(e)}")
            pbar.update(1)

    try:
        with open(output_file, "w") as f:
            json.dump(combined_data, f, indent=2, ensure_ascii=False)
        print(f"\nCombined JSON has been written to {output_file}")
        print(f"Total entries in merged file: {len(combined_data)}")
        return output_file, len(combined_data)
    except Exception as e:
        print(f"Error saving merged JSON: {str(e)}")
        return None, 0


# Metadata extractor

def format_pdf_date(date_str):
    """Format PDF date string to 'YYYY-MM-DD'"""
    date_str = date_str.lstrip("D:").rstrip("Z")

    # Parse the string to a datetime object
    try:
        date_obj = datetime.strptime(date_str, "%Y%m%d%H%M%S")
    except ValueError:
        date_obj = datetime.strptime(date_str, "%Y%m%d")

    # Format to 'YYYY-MM-DD'
    return date_obj.strftime("%Y-%m-%d")


def extract_pdf_metadata(pdf_path):
    """Extract metadata from a PDF file."""
    # Note: often metadata is not complete or missing, we should take care of that
    # Maybe we can extract it from openalex anyway
    with fitz.open(pdf_path) as doc:
        metadata = doc.metadata
    return {
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "subject": metadata.get("subject"),
        "keywords": metadata.get("keywords"),
        "creation_date": format_pdf_date(metadata.get("creationDate")),
    }


# Final wrapper function
def process_pdfs_in_folder(
    pdf_folder="app_storage/pdfs",
    yolo_model_path="models/yolo.pt",
    output_folder=None,
    pdf_chunk_size=25,
    batch_size=10,
):
    """
    Process PDFs in a folder, extracting tables, converting pages to images, processing with YOLO,
    and extracting text to return structured data for each PDF document.

    Args:
        pdf_folder (str): Path to the folder containing PDF files.
        yolo_model_path (str): Path to the YOLO model file.
        output_folder (str, optional): Directory to store intermediate outputs (images, TSVs).
        pdf_chunk_size (int, optional): Number of PDFs processed in each chunk (for memory management).
        batch_size (int, optional): Number of images processed in each YOLO batch.

    Returns:
        list: A list of dictionaries containing extracted information for each PDF document.
    """
    # Set up output directories
    if output_folder is None:
        temp_dir = tempfile.mkdtemp()
        output_directory = temp_dir
    else:
        output_directory = output_folder
        os.makedirs(output_directory, exist_ok=True)

    # Dictionary to store all extracted data
    extracted_data = []

    try:
        # Step 1: Process PDFs to extract images and text
        print("\nStep 1: Processing PDFs...")
        total_pages, pdf_processing_time, avg_time = process_pdf_directory(
            pdf_folder, output_directory, pdf_chunk_size=pdf_chunk_size
        )
        print("PDF processing completed.")

        # Step 2: Process Images with YOLO model
        print("\nStep 2: Processing Images...")
        total_images, image_processing_time, avg_image_time = process_images_directory(
            output_directory, yolo_model_path, batch_size=batch_size
        )
        print("Image processing completed.")

        # Step 3: Extract Text from PDF regions
        print("\nStep 3: Text Extraction...")
        total_files, text_extraction_time, _ = process_directory_for_text_extraction(
            output_directory, pdf_folder
        )
        print("Text extraction completed.")

        # Step 4: TSV to structured data processing
        print("\nStep 4: TSV to JSON Processing...")
        final_directories = []
        for subdir, _, _ in os.walk(output_directory):
            if subdir.endswith("final") and "_output" in subdir:
                final_directories.append(subdir)

        for directory in final_directories:
            document_data = []
            json_file_path, tsv_count = parse_tsvs_to_json(directory)

            if json_file_path:
                with open(json_file_path, "r", encoding="utf-8") as json_file:
                    document_data = json.load(json_file)

                    document_name = os.path.basename(
                        os.path.dirname(directory)
                    ).replace("_output", "")

                    # Extract metadata from the original PDF file
                    pdf_path = os.path.join(pdf_folder, f"{document_name}.pdf")
                    metadata = extract_pdf_metadata(pdf_path)

                    # Append document data with metadata
                    extracted_data.append(
                        {
                            "document_name": document_name,
                            "metadata": metadata,  # Insert metadata here
                            "sections": document_data,
                        }
                    )

        print("\nAll processing completed successfully!")
        return extracted_data

    finally:
        unload_yolo_model()

        # Clean up temporary directory if used
        if output_folder is None:
            shutil.rmtree(temp_dir)


if __name__ == "__main__":
    # Call the function
    processed_data = process_pdfs_in_folder(output_folder="temp/")

    # Print the result to inspect
    import json

    with open("temp.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)
