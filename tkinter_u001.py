import tkinter as tk
from tkinter import simpledialog, messagebox
from your_project import Calculator

class Application:
    def __init__(self):
        super().__init__()
        
        self.title("My First GUI App")
        self.geometry("400x300")
        
        self.withdraw()
        
        self._ask_user_name()

    def _ask_user_name(self):
        user_name = simpledialog.askstring("Name Prompt", "What's your name?", parent=self)
        
        if user_name:
            messagebox.showinfo("Welcome", f"Hello, {user_name}!")
            self._setup_main_window(user_name)
        else:
            self.destroy()

    def _setup_main_window(self, name):
        self.deiconify()
        
        self.label = tk.Label(
            self, 
            text=f"Hello, {name}!\nWelcome to Tkinter", 
            font=("Helvetica", 16)
        )
        self.label.pack(expand=True)

        self.quit_button = tk.Button(self, text="Close", command=self.destroy)
        self.quit_button.pack(pady=20)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
