# 📄 AI PDF Summarizer (Native Python & Desktop GUI)

Ein leichtgewichtiges, modulares Python-Tool, das mehrseitige PDF-Dokumente automatisiert analysiert und über modernste KI (Llama 3.3 via Groq) präzise zusammenfasst. 

Im Gegensatz zu Web-Apps läuft dieses Projekt zu 100 % in reinem Python und nutzt native OS-Fenster (Tkinter) für eine intuitive Bedienung ohne Browser.

---

## ✨ Features

* **Native Desktop-Dialoge (GUI):** Schlankes Pop-up-Fenster zur bequemen Auswahl der PDF per Zifferneingabe.
* **Automatisches Dokumenten-Parsing:** Schnelle Extraktion von Plain-Text aus mehrseitigen PDFs mittels `pypdf`.
* **High-Speed KI-Inferenz:** Direkte Anbindung an die Groq-Cloud-API für Zusammenfassungen in Sekundenschnelle.
* **Ergebnis-Präsentation:** Die finale Zusammenfassung ploppt direkt in einem sauberen Infofenster auf.
* **Saubere Architektur:** Strikte Trennung von Textextraktion (`src/pdf_reader.py`), KI-Logik (`src/ai_agent.py`) und Orchestrierung (`main.py`).
* **Sicherheitsstandard:** Schutz sensibler API-Keys über `.env` und `.gitignore`.

---

## 🛠️ Tech Stack

* **Sprache:** Python 3
* **GUI:** `tkinter` (Natives Desktop-Toolkit)
* **PDF Engine:** `pypdf`
* **LLM / API:** `groq` (Qwen 3.8 / Groq LLM)
* **Environment Management:** `python-dotenv`

---

## 📁 Projektstruktur

```text
ai-pdf-summarizer/
├── data/              # Lokaler Speicherort für PDFs (z. B. Test.pdf)
├── src/
│   ├── ai_agent.py    # Anbindung an Groq-LLM & Prompt-Design
│   └── pdf_reader.py  # PDF-Parsing & String-Konvertierung
├── .env.example       # Vorlage für Umgebungsvariablen
├── .gitignore         # Schützt sensible Daten vor Git-Tracking
├── main.py            # Startpunkt & GUI-Ablaufsteuerung
├── requirements.txt   # Projekt-Abhängigkeiten
└── README.md          # Projektdokumentation
```

---

## 🚀 Schnelleinrichtung & Start (Schritt-für-Schritt)

Folge diesen Schritten im Terminal, um das Projekt lokal auszuführen:

**1. Repository klonen:**
```bash
git clone [https://github.com/EnverAktuerk945/ai-pdf-summarizer.git](https://github.com/EnverAktuerk945/ai-pdf-summarizer.git)
cd ai-pdf-summarizer
```

**2. Eigene virtuelle Python-Umgebung erstellen und aktivieren:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Benötigte Bibliotheken installieren:**
```bash
pip install -r requirements.txt
```

**4. API-Schlüssel konfigurieren:**
Kopiere die Vorlage und trage deinen Groq-API-Key ein:
```bash
cp .env.example .env
```
*(Trage danach deinen Key in die neu erstellte `.env`-Datei ein)*

**5. Programm starten:**
Lege eine beliebige PDF-Datei in den `data/`-Ordner und starte das Skript:
```bash
python3 main.py
```