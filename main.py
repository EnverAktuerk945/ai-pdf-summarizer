import os
import sys
import logging
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from pathlib import Path

from src.pdf_reader import extract_text_from_pdf
from src.ai_agent import summarize_text

# Logging zentral konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def show_loading_dialog(parent: tk.Tk) -> tuple[tk.Toplevel, ttk.Progressbar]:
    """Erstellt ein modales Ladefenster mit animierter Progressbar."""
    dialog = tk.Toplevel(parent)
    dialog.title("Verarbeite Dokument...")
    dialog.geometry("320x110")
    dialog.resizable(False, False)

    # Fenster zentrieren
    dialog.update_idletasks()
    x = (dialog.winfo_screenwidth() - dialog.winfo_width()) // 2
    y = (dialog.winfo_screenheight() - dialog.winfo_height()) // 2
    dialog.geometry(f"+{x}+{y}")

    label = tk.Label(
        dialog,
        text="Extrahiere Text und generiere Zusammenfassung...\nBitte warten.",
        font=("Arial", 10),
        pady=10,
    )
    label.pack()

    progress = ttk.Progressbar(dialog, mode="indeterminate", length=260)
    progress.pack(pady=5)
    progress.start(10)

    dialog.transient(parent)
    dialog.grab_set()
    return dialog, progress


def process_pdf_in_background(
    pdf_path: str,
    root: tk.Tk,
    loading_dialog: tk.Toplevel,
    progress: ttk.Progressbar,
) -> None:
    """Führt Text-Extraktion und LLM-Inferenz in einem separaten Thread aus."""
    summary_result: str = ""
    error_message: str | None = None

    try:
        pdf_text = extract_text_from_pdf(pdf_path)
        summary_result = summarize_text(pdf_text)
    except Exception as exc:
        logger.exception("Fehler während der Verarbeitung aufgetreten.")
        error_message = str(exc)

    # Zurück in den Tkinter-Main-Thread für die UI-Aktualisierung
    def on_complete() -> None:
        progress.stop()
        loading_dialog.destroy()

        if error_message:
            messagebox.showerror("Fehler", error_message)
        else:
            messagebox.showinfo("Zusammenfassung", summary_result)

        root.destroy()
        sys.exit(0)

    root.after(0, on_complete)


def main() -> None:
    root = tk.Tk()
    root.withdraw()

    data_dir = Path("data")
    if not data_dir.exists():
        data_dir.mkdir()
        messagebox.showinfo(
            "Ordner erstellt",
            "Der Ordner 'data/' wurde neu erstellt. Lege dort deine PDFs ab!",
        )
        sys.exit(0)

    pdf_files = [f for f in os.listdir(data_dir) if f.lower().endswith(".pdf")]
    if not pdf_files:
        messagebox.showwarning(
            "Keine Dateien",
            "Keine PDF-Dateien im Ordner 'data/' gefunden.\nBitte lege zuerst eine PDF ab!",
        )
        sys.exit(0)

    # Menütext zusammenstellen
    menu_text = "Verfügbare PDF-Dateien:\n\n"
    for idx, filename in enumerate(pdf_files, start=1):
        menu_text += f"[{idx}] {filename}\n"
    menu_text += "\nGib die Ziffer der gewünschten Datei ein:"

    user_input = simpledialog.askstring("PDF auswählen", menu_text)
    if not user_input:
        logger.info("Abbruch durch Benutzer.")
        sys.exit(0)

    try:
        selected_index = int(user_input.strip()) - 1
        if not (0 <= selected_index < len(pdf_files)):
            raise IndexError("Ungültige Ziffer")
    except (ValueError, IndexError):
        messagebox.showerror("Ungültige Eingabe", "Bitte gib eine gültige Zahl aus der Liste ein.")
        sys.exit(1)

    selected_file = data_dir / pdf_files[selected_index]
    logger.info("Ausgewählte Datei: %s", selected_file)

    # Ladefenster anzeigen
    loading_dialog, progress = show_loading_dialog(root)

    # Worker-Thread starten (verhindert Einfrieren des Fensters)
    worker_thread = threading.Thread(
        target=process_pdf_in_background,
        args=(str(selected_file), root, loading_dialog, progress),
        daemon=True,
    )
    worker_thread.start()

    # GUI Event-Loop starten
    root.mainloop()


if __name__ == "__main__":
    main()