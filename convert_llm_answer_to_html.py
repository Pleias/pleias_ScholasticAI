import re


def replace_references(text, ref_map):
    def ref_replacer(match):
        ref_name = re.findall(r'<ref name="[^"]+">', match.group(0))[0]
        replacement = ref_map[ref_name]
        return replacement

    updated_text = re.sub(r'<ref name="[^"]+">[^<]+</ref>', ref_replacer, text)
    return updated_text


def return_span(number=1):
    return f"""<span style="border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;">{number}</span>"""


def convert_input_msg_to_html(answer):
    start_answer = answer.find("<|source_analysis_start|>")
    end_answer = answer.find("<|source_analysis_end|>")
    answer = answer[start_answer + len("<|source_analysis_start|>"):end_answer]
    references = re.findall(r'<ref name="[^"]+">', answer)
    ref_map = {}
    reference_count = 1
    for ref in references:
        if ref not in ref_map:
            ref_map[ref] = return_span(reference_count)
            reference_count += 1
    updated_text = replace_references(answer, ref_map)
    return updated_text
