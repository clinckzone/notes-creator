import customtkinter as ctk
import threading
from services.transcript_fetcher import get_transcript
from services.llm_factory import generate_notes_with_llm

class MainWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # URL Input Frame
        self.url_frame = ctk.CTkFrame(self)
        self.url_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.url_frame.grid_columnconfigure(0, weight=1)

        self.url_entry = ctk.CTkEntry(self.url_frame, placeholder_text="Enter YouTube URL")
        self.url_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.generate_button = ctk.CTkButton(self.url_frame, text="Generate Notes", command=self.on_generate_click)
        self.generate_button.grid(row=0, column=1, padx=5, pady=5)

        # Notes Display
        self.notes_display = ctk.CTkTextbox(self)
        self.notes_display.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.notes_display.insert("0.0", "Your generated notes will appear here.")
        self.notes_display.configure(state="disabled")

    def on_generate_click(self):
        """
        Handles the click event of the 'Generate Notes' button.
        """
        url = self.url_entry.get()
        if not url:
            self.update_notes_display("Please enter a YouTube URL.")
            return

        self.generate_button.configure(state="disabled")
        self.update_notes_display("Generating notes, please wait...")

        thread = threading.Thread(target=self.generate_notes_thread, args=(url,))
        thread.start()

    def generate_notes_thread(self, url: str):
        """
        The function that runs in a separate thread to generate notes.
        """
        transcript = get_transcript(url)
        if transcript.startswith("Error"):
            self.update_notes_display(transcript)
            self.generate_button.configure(state="normal")
            return

        notes = generate_notes_with_llm(transcript)
        self.update_notes_display(notes)
        self.generate_button.configure(state="normal")

    def update_notes_display(self, text: str):
        """
        Updates the notes display textbox in a thread-safe way.
        """
        self.notes_display.configure(state="normal")
        self.notes_display.delete("0.0", "end")
        self.notes_display.insert("0.0", text)
        self.notes_display.configure(state="disabled")
