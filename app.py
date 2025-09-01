import streamlit as st
from utils.transcript import get_transcript
from utils.summarizer import generate_summary
from utils.explainer import generate_explanation
from utils.exporter import save_to_pdf

st.set_page_config(page_title="YouTube AI Notes Generator", layout="centered")

st.title("YouTube Lecture to AI Notes Generator")

video_url = st.text_input("Paste YouTube Video Link:")

if st.button("Generate Notes"):
    if video_url:
        try:
            with st.spinner("Fetching transcript..."):
                transcript = get_transcript(video_url)

            with st.spinner("Generating summary..."):
                summary = generate_summary(transcript)

            with st.spinner("Explaining notes..."):
                explanation = generate_explanation(summary)

            st.success("Notes generated successfully!")

            st.subheader("Summary Notes")
            st.write(summary)

            st.subheader("Detailed Explanation")
            st.write(explanation)

            # Save PDF
            filename = "outputs/notes.pdf"
            save_to_pdf(filename, "YouTube Lecture", summary, explanation)

            with open(filename, "rb") as f:
                st.download_button("⬇Download Notes as PDF", f, file_name="notes.pdf")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste a valid YouTube link!")
