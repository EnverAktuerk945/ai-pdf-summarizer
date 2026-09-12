# AI PDF Summarizer (CLI)

Ein modularer Python-basierter KI-Agent, der den Inhalt beliebiger PDF-Dokumente extrahiert und mithilfe der Groq-API (LLM) strukturiert auf der Konsole zusammenfasst.

## Features

- **Text-Extraktion:** Robustes Auslesen mehrseitiger PDF-Dateien via `pypdf`.
- **LLM-Integration:** Schnelle Zusammenfassungen über die Groq-Cloud-API (`llama-3.3-70b-versatile`).
- **Modulare Architektur:** Klare Trennung von Datenextraktion (`pdf_reader.py`), KI-Logik (`ai_agent.py`) und Ablaufsteuerung (`main.py`).
- **Sichere Konfiguration:** Auslagerung von API-Keys über Umgebungsvariablen (`.env`).

## Projektstruktur

```text
ai-pdf-summarizer/
├── data/              # Lokale PDF-Dateien (z. B. Test.pdf)
├── src/
│   ├── ai_agent.py    # Schnittstelle zur Groq-API & Prompt-Logik
│   └── pdf_reader.py  # PDF-Parsing & Textextraktion
├── .env               # Lokale Umgebungsvariablen (nicht versioniert)
├── .gitignore         # Ignoriert u.a. .env und virtuelle Umgebungen
├── main.py            # Orchestrierung des Workflows
├── requirements.txt   # Projekt-Abhängigkeiten
└── README.md          # Dokumentation