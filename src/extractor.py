from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str | Path) -> str:
    """Extrahiert den gesamten Text aus einer angegebenen PDF-Datei."""
    path = Path(pdf_path)

    # Prüfen, ob die Datei überhaupt existiert
    if not path.is_file():
        raise FileNotFoundError(f"Die Datei unter '{path}' existiert nicht.")

    reader = PdfReader(path)
    extracted_pages = []

    # Durch jede Seite iterieren und den Text sammeln
    for index, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            extracted_pages.append(text.strip())

    # Alle Seiten mit Zeilenumbrüchen zu einem sauberen String zusammenfügen
    return "\n\n".join(extracted_pages)


# Dieser Block wird nur ausgeführt, wenn du diese Datei direkt startest (wie 'public static void main' in Java)
if __name__ == "__main__":
    test_file = Path("data/test.pdf")

    print("Starte Textextraktion...")
    full_text = extract_text_from_pdf(test_file)

    print("\n--- Gefundener Text (Auszug) ---")
    # Zeige die ersten 500 Zeichen an, damit das Terminal nicht geflutet wird
    print(full_text[:500])
    print(f"\nGesamtlänge des extrahierten Texts: {len(full_text)} Zeichen.")