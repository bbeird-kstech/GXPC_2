import tkinter as tk

class HomeView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text="Home View")
        self.label.pack(fill="both", expand=True)

    def __str__(self):
        return ".!frame2.!homeview" if self.master.winfo_toplevel() == self.master else ""