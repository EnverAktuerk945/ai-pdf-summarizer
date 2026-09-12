import os
import tkinter as tk
from tkinter import simpledialog, messagebox

from src.pdf_reader import extract_text_from_pdf
from src.ai_agent import summarize_text

# 1. Unsichtbares Hauptfenster erstellen (damit nur Pop-ups erscheinen)
root = tk.Tk()
root.withdraw()

# 2. PDF-Dateien aus data/ suchen
alle_dateien = os.listdir("data")
pdf_dateien = [d for d in alle_dateien if d.endswith(".pdf")]

if not pdf_dateien:
    messagebox.showerror("Fehler", "Keine PDFs im Ordner 'data' gefunden!")
    exit()

# 3. Text für das Fenster vorbereiten
menue_text = "Verfügbare PDFs:\n\n"
for nummer, datei in enumerate(pdf_dateien, 1):
    menue_text += f"[{nummer}] {datei}\n"
menue_text += "\nGib die Nummer der Datei ein die du Zusammfassen willst:"

# 4. Fenster 1: Pop-up mit Eingabefeld
auswahl_text = simpledialog.askstring("PDF auswählen", menue_text)

# Prüfen, ob der Nutzer auf 'Abbrechen' geklickt oder nichts eingegeben hat
if not auswahl_text:
    exit()

auswahl_index = int(auswahl_text) - 1
gewaehlte_datei = pdf_dateien[auswahl_index]
pfad = f"data/{gewaehlte_datei}"

# 5. Text extrahieren & durch KI jagen
pdf_text = extract_text_from_pdf(pfad)
ergebnis = summarize_text(pdf_text)

# 6. Fenster 2: Pop-up mit der Zusammenfassung
messagebox.showinfo("Zusammenfassung", ergebnis)