# 📄 AI PDF Summarizer (Native Python & Desktop GUI)

Ein leichtgewichtiges, modulares Python-Tool, das mehrseitige PDF-Dokumente automatisiert analysiert und über modernste KI (Llama 3.3 via Groq) präzise zusammenfasst. 

Im Gegensatz zu Web-Apps läuft dieses Projekt zu 100 % in reinem Python und nutzt native OS-Fenster (Tkinter) für eine intuitive Bedienung ohne Browser.

---

## ✨ Features

- Native Desktop-Dialoge (GUI): Kein Terminal-Gefummel beim Start – ein schlankes Pop-up-Fenster listet alle verfügbaren PDFs im Ordner auf und lässt dich bequem per Eingabe der Ziffer wählen.
- Automatisches Dokumenten-Parsing: Schnelle Extraktion von Plain-Text aus mehrseitigen PDFs mittels pypdf.
- High-Speed KI-Inferenz: Direkte Anbindung an die Groq-Cloud-API für Zusammenfassungen in Sekundenschnelle.
- Ergebnis-Präsentation: Die finale Zusammenfassung ploppt direkt in einem sauberen Infofenster auf.
- Saubere Architektur (Separation of Concerns): Strikte Trennung von Textextraktion (src/pdf_reader.py), KI-Logik (src/ai_agent.py) und Orchestrierung (main.py).
- Sicherheitsstandard: Schutz sensibler API-Keys über .env und .gitignore.

---

## 🛠️ Tech Stack

- Sprache: Python 3
- GUI: tkinter (Natives Desktop-Toolkit)
- PDF Engine: pypdf
- LLM / API: groq (Llama 3.3)
- Environment Management: python-dotenv

---

## 📁 Projektstruktur

ai-pdf-summarizer/
├── data/              # Lokaler Speicherort für PDFs (z. B. Test.pdf)
├── src/
│   ├── ai_agent.py    # Anbindung an Groq-LLM & Prompt-Design
│   └── pdf_reader.py  # PDF-Parsing & String-Konvertierung
├── .env               # Lokale Umgebungsvariablen (wird nicht hochgeladen)
├── .gitignore         # Schützt sensible Daten vor Git-Tracking
├── main.py            # Startpunkt & GUI-Ablaufsteuerung
├── requirements.txt   # Projekt-Abhängigkeiten
└── README.md          # Projektdokumentation

---

## 🚀 Schnelleinrichtung & Start (Schritt-für-Schritt)

Folge einfach diesen Schritten im Terminal, um das Projekt lokal auf deinem Rechner zu starten:

1. Repository auf deinen Rechner herunterladen:
git clone https://github.com/EnverAktuerk945/ai-pdf-summarizer.git
cd ai-pdf-summarizer

2. Eigene virtuelle Python-Umgebung erstellen und aktivieren:
python3 -m venv .venv
source .venv/bin/activate

3. Benötigte Bibliotheken mit einem Befehl installieren:
pip install -r requirements.txt

4. API-Schlüssel hinterlegen:
Erstelle eine Textdatei mit dem genauen Namen .env direkt im Hauptordner und trage deinen Groq-Key ein:
GROQ_API_KEY=dein_persoenlicher_groq_api_key

5. Programm starten:
Lege eine beliebige PDF-Datei in den data/ Ordner und starte das Skript:
python3 main.py

Es öffnet sich sofort ein kleines Dialogfenster auf deinem Desktop, in dem du die gewünschte PDF auswählen kannst. Die KI generiert anschließend die Zusammenfassung und zeigt sie in einem Info-Fenster an.