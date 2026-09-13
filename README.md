# 📄 AI PDF Summarizer (Native Python & Desktop GUI)

Ein leichtgewichtiges, modulares Desktop-Tool zur automatisierten Analyse und Verdichtung mehrseitiger PDF-Dokumente mittels lokaler Textextraktion (`pypdf`) und Cloud-LLM-Inferenz (Qwen 3.8 via Groq).

Die Anwendung läuft vollständig in reinem Python und nutzt native Betriebssystem-Dialoge (`tkinter`), kombiniert mit asynchroner Hintergrundverarbeitung für eine unterbrechungsfreie Benutzererfahrung ohne Browser-Overhead.

---

## ✨ Features

* **Non-blocking Desktop-GUI:** Hintergrundverarbeitung via `threading` verhindert das Einfrieren des Fensters bei rechen- oder netzwerkintensiven Abfragen.
* **Visuelles Feedback:** Modaler Ladedialog mit animierter `ttk.Progressbar` während der Textextraktion und Inferenz.
* **Automatisches Dokumenten-Parsing:** Schnelle Extraktion von Plain-Text aus mehrseitigen PDFs mittels `pypdf`.
* **High-Speed KI-Inferenz:** Direkte Anbindung an die Groq-Cloud-API (`qwen/qwen3.8-27b`) für strukturierte Zusammenfassungen in Sekundenschnelle.
* **Enterprise Error Handling:** Dediziertes Abfangen von beschädigten/verschlüsselten PDFs (`PdfReadError`, `FileNotDecryptedError`), leeren Scans, fehlenden API-Schlüsseln und API-Rate-Limits.
* **Standardisiertes Logging:** Vollständige Protokollierung aller Prozessschritte über Pythons internes `logging`-Modul mit Zeitstempeln und Loglevels (`INFO`, `WARNING`, `ERROR`).
* **Saubere Architektur:** Strikte Trennung von Datenextraktion (`src/pdf_reader.py`), KI-Prompt-Logik (`src/ai_agent.py`) und Orchestrierung (`main.py`).
* **Sicherheitsstandard:** Schutz sensibler API-Keys über `.env` und `.gitignore`.

---

## 🛠️ Tech Stack & Tooling

* **Sprache:** Python 3 (Typisiert mit Type Hints)
* **GUI & Threading:** `tkinter`, `ttk`, `threading`
* **PDF Engine:** `pypdf`
* **LLM / API:** `groq` SDK (`qwen/qwen3.8-27b`)
* **Environment:** `python-dotenv`
* **Linter / Formatter:** `ruff` (konfiguriert via `pyproject.toml`)
* **Lizenz:** MIT License

---

## 📁 Projektstruktur

```text
ai-pdf-summarizer/
├── data/              # Lokaler Speicherort für PDF-Dateien (inkl. Beispieldaten)
├── src/
│   ├── __init__.py    # Paket-Initialisierung
│   ├── ai_agent.py    # LLM-Orchestrierung, Prompt-Design & API-Error-Handling
│   └── pdf_reader.py  # PDF-Parsing, Validierung & String-Extraktion
├── .env.example       # Konfigurationsvorlage für Umgebungsvariablen
├── .gitignore         # Ignoriert virtuelle Umgebungen, Caches und Secrets
├── LICENSE            # MIT-Lizenz
├── main.py            # GUI-Ablaufsteuerung, Threading & Einstiegspunkt
├── pyproject.toml     # Projekt-Metadaten & Ruff-Konfiguration
├── requirements.txt   # Abhängigkeiten für den Produktivbetrieb
└── README.md          # Projektdokumentation
```

---

## 🚀 Schnelleinrichtung & Start

Folge diesen Schritten im Terminal, um das Projekt lokal auszuführen:

**1. Repository klonen:**
```bash
git clone [https://github.com/EnverAktuerk945/ai-pdf-summarizer.git](https://github.com/EnverAktuerk945/ai-pdf-summarizer.git)
cd ai-pdf-summarizer
```

**2. Virtuelle Umgebung erstellen und aktivieren:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Abhängigkeiten installieren:**
```bash
python3 -m pip install -r requirements.txt
```

**4. API-Schlüssel hinterlegen:**
Erstelle deine `.env`-Datei anhand der Vorlage:
```bash
cp .env.example .env
```
Öffne `.env` und trage deinen Groq-API-Key ein:
```text
GROQ_API_KEY=gsk_dein_api_schluessel_hier
```

**5. Anwendung starten:**
Lege eine beliebige PDF-Datei in den `data/`-Ordner (oder nutze die mitgelieferten Test-Dateien) und starte das Tool:
```bash
python3 main.py
```

---

## ⚖️ Lizenz

Dieses Projekt ist unter der [MIT License](LICENSE) lizenziert.