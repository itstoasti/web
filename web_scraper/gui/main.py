```python
import json
import tkinter as tk
from tkinter import ttk, filedialog

class GUI:
    def __init__(self, root):
        self.root = root
        self.treeview = ttk.Treeview(root)
        self.json_file = None

        # Configure treeview
        self.treeview["columns"] = ("1", "2")
        self.treeview.column("#0", width=270, minwidth=270, stretch=tk.NO)
        self.treeview.column("1", width=150, minwidth=150, stretch=tk.NO)
        self.treeview.column("2", width=400, minwidth=200)
        self.treeview.heading("#0", text="Name", anchor=tk.W)
        self.treeview.heading("1", text="Type", anchor=tk.W)
        self.treeview.heading("2", text="Value", anchor=tk.W)

        # Configure buttons
        load_button = ttk.Button(root, text="Load JSON", command=self.load_json)
        load_button.pack()

        self.treeview.pack()

    def load_json(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.json_file = file_path
            self.populate_treeview()

    def populate_treeview(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)

        for key, value in data.items():
            self.treeview.insert('', 'end', text=key, values=(type(value).__name__, value))

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
```