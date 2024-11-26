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


answer = """
### Answer ###
Humans and AI language models often commit errors when solving problems due to various factors. One of the primary sources of error is inherent bias present within training data. Biases can be absorbed by these models from the biases in the source material or selection process for training data<ref name=""62d6d314276154d6"">""Biases can be introduced or amplified through algorithms that place more importance on certain features or data points.""</ref>. These biases may then influence how they solve problems, leading to potentially discriminatory outcomes.
Another significant issue is the ambiguity of cultural norms. As language models are trained on a limited dataset reflecting specific cultural contexts, accurately capturing diverse cultural perspectives can be challenging<ref name=""d877f2827995cb75"">""Determining which norms to encode in AI models is a complex task that requires a nuanced understanding of diverse cultural perspectives.""</ref>. This ambiguity can result in errors when dealing with complex and multifaceted problems requiring broad cultural understanding.
Moreover, the concept of fairness itself poses challenges. Defining ""fairness"" for an AI model in different contexts involves stakeholders from various backgrounds, each bringing their own interpretations<ref name=""d877f2827995cb75"">""Eliminating bias from AI models requires defining 'fair' in the context of applications, which is challenging due to the diverse range of stakeholders and perspectives.""</ref>. As a result, these varying definitions can lead to discrepancies in how fairness is applied by different systems.
Transparency plays an essential role in mitigating errors. Ensuring that users understand how AI models make decisions allows for informed decision-making<ref name=""c3106ffc40e315ea"">""Emphasizing transparency can help build public trust in AI systems, as it demonstrates a commitment to ethical development and responsible deployment.""</ref>. This transparency fosters collaboration between developers, researchers, policymakers, and affected communities, enabling continuous improvement of the models<ref name=""c3106ffc40e315ea"">""Transparency can facilitate collaboration between developers, researchers, policymakers, and aﬀected communities, enabling them to share insights and feedback that can help guide the development of more equitable and ethical AI systems.""</ref>.
In terms of human-AI interaction, customization options for models can help mitigate some biases by tailoring behavior according to user preferences or specific contexts<ref name=""d877f2827995cb75"">""Users can be provided with options to customize the model' s behavior, adjusting the output according to their preferences or requirements.""</ref>. However, these approaches are not foolproof as bias can still persist from different sources within the system.
Finally, dialect usage in AI systems without real evidence can significantly impact decisions. Language models trained on specific dialects may make mistakes when confronted with"
"""
"""
TO test this function please use 
from IPython.core.display import HTML
out = convert_input_msg_to_html(answer)          
HTML(out)
"""