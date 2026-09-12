from src.pdf_reader import extract_text_from_pdf
from src.ai_agent import summarize_text

pfad = "data/Test.pdf"
text = extract_text_from_pdf(pfad)
zusammenfassung = summarize_text(text)

print(zusammenfassung)