from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_to_pdf(filename, title, summary, explanation):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, f"📌 Topic: {title}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 720, "Summary Notes:")
    text_obj = c.beginText(50, 700)
    text_obj.setFont("Helvetica", 11)
    for line in summary.split(". "):
        text_obj.textLine("- " + line.strip())
    c.drawText(text_obj)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 550, "Detailed Explanation:")
    text_obj = c.beginText(50, 530)
    text_obj.setFont("Helvetica", 11)
    for line in explanation.split(". "):
        text_obj.textLine("- " + line.strip())
    c.drawText(text_obj)

    c.save()
