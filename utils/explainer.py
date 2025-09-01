from transformers import pipeline

explainer = pipeline("summarization", model="t5-base")

def generate_explanation(summary_text, max_len=250):
    explanation = explainer(
        "explain: " + summary_text,
        max_length=max_len,
        min_length=60,
        do_sample=False
    )
    return explanation[0]['summary_text']
