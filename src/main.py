import customtkinter as ctk
from dotenv import load_dotenv
from gui.main_window import MainWindow

def main():
    """
    The main function to run the application.
    """
    load_dotenv()
    app = ctk.CTk()
    app.title("Notes Creator")
    app.geometry("800x600")
    
    window = MainWindow(app)
    window.pack(fill="both", expand=True)
    
    app.mainloop()

if __name__ == "__main__":
    main()
