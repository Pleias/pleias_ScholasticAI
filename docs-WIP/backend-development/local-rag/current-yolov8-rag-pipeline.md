# Current YOLOv8 RAG pipeline

Three main scripts + 1 json parsing script for processing from PDF files to chunks ready to be embedded.\\

## Section 1: PDF to Image Conversion and Table Extraction

### Key Steps:

1. Convert PDF files to JPG images
   * We transform the PDF files to JPG, one image per page, since YOLO only analyzes images.
   * The standard YOLO DPI resolution seems to be 72, which works but is somewhat blurry for human reading. A PDF ready to be printed into a book normally has between 200 and 300 DPI.
   * Recommendation: Use 144 DPI (multiples of 72 to avoid artifacts) for a balance between readability and processing time.
2. Extract tables using pdfplumber
   * We use pdfplumber to recognize the tables present in the PDF.
   * The script saves the coordinates of the tables, extracts the text inside them, and saves the content to TSV files, trying to keep the table structure when possible.
   * Note: The results here are mixed, but for now it's the simplest Python solution that seems to work the best and the fastest.
3. Create blank versions of PDFs with tables covered
   * Once we extract the table information, we use the coordinates to add white rectangles to the images.
   * This step allows YOLO to work more efficiently in the next section by ignoring the table areas.
   * Note: We need to benchmark how efficient the Table Recognition capacities from YOLO are. From empirical tests, they also give mixed results.

```python
// 

import pdfplumber
import fitz  # PyMuPDF
import csv
import os
import time
import traceback
import gc
from joblib import Parallel, delayed
from tqdm import tqdm


def clean_cell(cell):
    # Clean cell content by replacing newlines with spaces.
    if cell is None:
        return ''
    return cell.replace('\n', ' ')

def pdf_to_jpg_original(args):
    # Convert PDF pages to JPG images.
    pdf_path, output_images = args
    os.makedirs(output_images, exist_ok=True)
    doc = fitz.open(pdf_path)
    jpg_count = 0
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        output_path = os.path.join(output_images, f"{base_name}_page{page_num + 1}.jpg")
        pix.save(output_path)
        jpg_count += 1
    doc.close()
    return jpg_count

def extract_text_tables_and_save(args):
    # Extract text and tables from a PDF and save them as TSV files.
    pdf_path, output_directory = args
    os.makedirs(output_directory, exist_ok=True)
    global_table_counter = 1
    pdf_basename = os.path.splitext(os.path.basename(pdf_path))[0]

    with pdfplumber.open(pdf_path) as pdf, fitz.open(pdf_path) as doc:
        tables = []
        for page_num, plumb_page in enumerate(pdf.pages):
            # Save coordinates of text and tables
            coord_tsv_filename = os.path.join(output_directory, f"{pdf_basename}_page{page_num + 1}.tsv")
            with open(coord_tsv_filename, 'w', newline='', encoding='utf-8') as coord_file:
                writer = csv.writer(coord_file, delimiter='\t')
                writer.writerow(['text', 'x1', 'y1', 'x2', 'y2'])
                tables = plumb_page.find_tables()
                if tables:
                    for i, table in enumerate(tables):
                        x1, y1, x2, y2 = table.bbox
                        writer.writerow([f"table_{global_table_counter + i}", x1, y1, x2, y2])
            
            # Save table contents
            for i, table in enumerate(tables):
                tsv_content = [clean_cell(cell) for row in table.extract() for cell in row]
                table_tsv_filename = os.path.join(output_directory, f"{pdf_basename}_page{page_num+1}_table{global_table_counter}.tsv")
                with open(table_tsv_filename, 'w', newline='', encoding='utf-8') as tsv_file:
                    writer = csv.writer(tsv_file, delimiter='\t')
                    writer.writerows([[cell] for cell in tsv_content])

                global_table_counter += 1

def cover_tables_in_pdf(args):
    # Create a new PDF with tables covered in white.
    pdf_path, output_path = args
    table_areas = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            for table in page.find_tables():
                table_areas.append((page_number, table.bbox))
    doc = fitz.open(pdf_path)
    for page_number, bbox in table_areas:
        page = doc[page_number]
        rect = fitz.Rect(bbox[0], bbox[1], bbox[2], bbox[3])
        shape = page.new_shape()
        shape.draw_rect(rect)
        shape.finish(width=1, color=(1, 1, 1), fill=(1, 1, 1))
        shape.commit()
    doc.save(output_path, garbage=4, deflate=True)
    doc.close()

def pdf_to_jpg(args):
    # Convert PDF pages to JPG images (for the version with covered tables).
    blank_path, output_images = args
    os.makedirs(output_images, exist_ok=True)
    doc = fitz.open(blank_path)
    jpg_count = 0
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        output_path = os.path.join(output_images, f"page_{page_num + 1}.jpg")
        pix.save(output_path)
        jpg_count += 1
    doc.close()
    return jpg_count

def process_pdf(pdf_path):
    # Process a single PDF file: extract text/tables, create images, and cover tables.
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_directory = os.path.join(base_output_directory, base_name + "_output")
    
    try:
        extract_text_tables_and_save((pdf_path, output_directory))
        
        # Create original images
        output_images_original = os.path.join(output_directory, base_name + "_images_original")
        jpg_count_original = pdf_to_jpg_original((pdf_path, output_images_original))
        
        # Create blank images (with tables covered)
        output_path = os.path.join(output_directory, base_name + "_blank.pdf")
        cover_tables_in_pdf((pdf_path, output_path))
        output_images = os.path.join(output_directory, base_name + "_images")
        jpg_count = pdf_to_jpg((output_path, output_images))
        
        return jpg_count + jpg_count_original  # Return total number of JPGs created
    except Exception as e:
        with open("processing_errors.log", "a") as log_file:
            log_file.write(f"Error processing {pdf_path}: {str(e)}\n")
            traceback.print_exc(file=log_file)
        return 0

def process_pdf_directory(input_directory):
    # Process all PDF files in the input directory.
    start_time = time.time()
    
    pdf_paths = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith('.pdf')]
    total_jpg_count = 0
    
    chunk_size = 250

    for start_idx in range(0, len(pdf_paths), chunk_size):
        end_idx = start_idx + chunk_size
        pdf_chunk = pdf_paths[start_idx:end_idx]
        
        chunk_jpg_count = sum(Parallel(n_jobs=10)(delayed(process_pdf)(pdf_path) for pdf_path in pdf_chunk))
        total_jpg_count += chunk_jpg_count

        gc.collect()
    
    end_time = time.time()
    total_time = end_time - start_time
    avg_time_per_page = total_time / total_jpg_count if total_jpg_count else 0
    
    print(f"Total pages processed: {total_jpg_count}")
    print(f"Total processing time: {total_time:.2f} seconds")
    print(f"Average time per page: {avg_time_per_page:.2f} seconds/page")

# Base output directory where all results will be saved.
base_output_directory = "/mnt/jupiter/c/mozilla/first_test"

if __name__ == "__main__":
    input_directory = "/mnt/jupiter/c/mozilla/pdf"
    process_pdf_directory(input_directory)
```

## Section 2: Image Layout Analysis with YOLO

### Key Steps:

1. Analyze layout using YOLO
   * We use the YOLO model to analyze the layout of the blanked-out pages.
   * This step identifies various elements of the page layout, such as titles, paragraphs, and other text zones.
2. Save results in TSV format
   * We save the coordinates and labels from each bounding box to TSV format (1 file per page).
   * We prefer using TSV format because it allows us to order the entries from top to bottom (like reading a document) using the y1 coordinate.
   * This makes it easy to quickly check if the results we're getting are good and correspond to the actual page layout.
   * It also allows us to concatenate the texts from the different entries into appropriate chunks in the next section.
3. Use of SegmOnto labels
   * The labels used by the fine-tuned model are from the SegmOnto project.
   * The coordinates we save are in the classic x1, y1, x2, y2 format for bounding boxes.
   * These coordinates use the YOLO notation but can be easily transformed to Florence, COCO, CVAT, etc.

###

```python
import pdfplumber
import fitz  # PyMuPDF
import csv
import os
import time
import traceback
import gc
from joblib import Parallel, delayed
from tqdm import tqdm


def clean_cell(cell):
    # Clean cell content by replacing newlines with spaces.
    if cell is None:
        return ''
    return cell.replace('\n', ' ')

def pdf_to_jpg_original(args):
    # Convert PDF pages to JPG images.
    pdf_path, output_images = args
    os.makedirs(output_images, exist_ok=True)
    doc = fitz.open(pdf_path)
    jpg_count = 0
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        output_path = os.path.join(output_images, f"{base_name}_page{page_num + 1}.jpg")
        pix.save(output_path)
        jpg_count += 1
    doc.close()
    return jpg_count

def extract_text_tables_and_save(args):
    # Extract text and tables from a PDF and save them as TSV files.
    pdf_path, output_directory = args
    os.makedirs(output_directory, exist_ok=True)
    global_table_counter = 1
    pdf_basename = os.path.splitext(os.path.basename(pdf_path))[0]

    with pdfplumber.open(pdf_path) as pdf, fitz.open(pdf_path) as doc:
        tables = []
        for page_num, plumb_page in enumerate(pdf.pages):
            # Save coordinates of text and tables
            coord_tsv_filename = os.path.join(output_directory, f"{pdf_basename}_page{page_num + 1}.tsv")
            with open(coord_tsv_filename, 'w', newline='', encoding='utf-8') as coord_file:
                writer = csv.writer(coord_file, delimiter='\t')
                writer.writerow(['text', 'x1', 'y1', 'x2', 'y2'])
                tables = plumb_page.find_tables()
                if tables:
                    for i, table in enumerate(tables):
                        x1, y1, x2, y2 = table.bbox
                        writer.writerow([f"table_{global_table_counter + i}", x1, y1, x2, y2])
            
            # Save table contents
            for i, table in enumerate(tables):
                tsv_content = [clean_cell(cell) for row in table.extract() for cell in row]
                table_tsv_filename = os.path.join(output_directory, f"{pdf_basename}_page{page_num+1}_table{global_table_counter}.tsv")
                with open(table_tsv_filename, 'w', newline='', encoding='utf-8') as tsv_file:
                    writer = csv.writer(tsv_file, delimiter='\t')
                    writer.writerows([[cell] for cell in tsv_content])

                global_table_counter += 1

def cover_tables_in_pdf(args):
    # Create a new PDF with tables covered in white.
    pdf_path, output_path = args
    table_areas = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            for table in page.find_tables():
                table_areas.append((page_number, table.bbox))
    doc = fitz.open(pdf_path)
    for page_number, bbox in table_areas:
        page = doc[page_number]
        rect = fitz.Rect(bbox[0], bbox[1], bbox[2], bbox[3])
        shape = page.new_shape()
        shape.draw_rect(rect)
        shape.finish(width=1, color=(1, 1, 1), fill=(1, 1, 1))
        shape.commit()
    doc.save(output_path, garbage=4, deflate=True)
    doc.close()

def pdf_to_jpg(args):
    # Convert PDF pages to JPG images (for the version with covered tables).
    blank_path, output_images = args
    os.makedirs(output_images, exist_ok=True)
    doc = fitz.open(blank_path)
    jpg_count = 0
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        output_path = os.path.join(output_images, f"page_{page_num + 1}.jpg")
        pix.save(output_path)
        jpg_count += 1
    doc.close()
    return jpg_count

def process_pdf(pdf_path):
    # Process a single PDF file: extract text/tables, create images, and cover tables.
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_directory = os.path.join(base_output_directory, base_name + "_output")
    
    try:
        extract_text_tables_and_save((pdf_path, output_directory))
        
        # Create original images
        output_images_original = os.path.join(output_directory, base_name + "_images_original")
        jpg_count_original = pdf_to_jpg_original((pdf_path, output_images_original))
        
        # Create blank images (with tables covered)
        output_path = os.path.join(output_directory, base_name + "_blank.pdf")
        cover_tables_in_pdf((pdf_path, output_path))
        output_images = os.path.join(output_directory, base_name + "_images")
        jpg_count = pdf_to_jpg((output_path, output_images))
        
        return jpg_count + jpg_count_original  # Return total number of JPGs created
    except Exception as e:
        with open("processing_errors.log", "a") as log_file:
            log_file.write(f"Error processing {pdf_path}: {str(e)}\n")
            traceback.print_exc(file=log_file)
        return 0

def process_pdf_directory(input_directory):
    # Process all PDF files in the input directory.
    start_time = time.time()
    
    pdf_paths = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith('.pdf')]
    total_jpg_count = 0
    
    chunk_size = 250

    for start_idx in range(0, len(pdf_paths), chunk_size):
        end_idx = start_idx + chunk_size
        pdf_chunk = pdf_paths[start_idx:end_idx]
        
        chunk_jpg_count = sum(Parallel(n_jobs=10)(delayed(process_pdf)(pdf_path) for pdf_path in pdf_chunk))
        total_jpg_count += chunk_jpg_count

        gc.collect()
    
    end_time = time.time()
    total_time = end_time - start_time
    avg_time_per_page = total_time / total_jpg_count if total_jpg_count else 0
    
    print(f"Total pages processed: {total_jpg_count}")
    print(f"Total processing time: {total_time:.2f} seconds")
    print(f"Average time per page: {avg_time_per_page:.2f} seconds/page")

# Base output directory where all results will be saved.
base_output_directory = "/mnt/jupiter/c/mozilla/first_test"

if __name__ == "__main__":
    input_directory = "/mnt/jupiter/c/mozilla/pdf"
    process_pdf_directory(input_directory)
```

Section 3:

* In this section we use PyMuPDF to extract the text from the boxes identified by Yolo and add this text to the entries of the tsv files.
* The script also creates a CVAT.xml file which contains the coordinates and labels of each page, ready to be imported to CVAT (the client we used to annotate) if we want to manually modifiy the boxes for better chunking or fine tuning.

json\_parsing

* This script will take the final tsv files and parse them to a json file per PDF, with chunks ready to be embedded.
* Those chunks are made following some rules for concatenation, like for example putting together different MainZone-P texts into the same json entry, until a new label like MainZone-Title appears, then a new entry starts.
* In this iteration of the script I mainly ignored the less frequent tags (they appear very rarely) like signature zone, stamp zone or others, since it was mainly noise instead of text.
* The goal was to keep chunks of around 300 words lenght. The rules of concatenation or title notation can be modified. The sections that it add are Section (title of the section), Text, Word Count, Document (the name of the file) and page (it indicates the number of the pages the text present in those chunks belong to)
* (note, there's also a file to put all the jsons in one single one and add a hash to each entry, i'll add it here)

RAG

* For the RAG, currently we are using lancedb for storing and embedding of the chunks. We use a fine-tuned version of Llama 3.1 8b which gives sourced answers quoting the documents with a predefined format.
