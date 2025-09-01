from transformers import pipeline

# Pretrained model load karo
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, max_len=200):
    # Large text ko chunks mein tod do
    if len(text.split()) > 800:
        text = " ".join(text.split()[:800])
    summary = summarizer(text, max_length=max_len, min_length=50, do_sample=False)
    return summary[0]['summary_text']
