import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import os

# Ścieżka do pliku JSON
DATA_FILE = "budget.json"

# Funkcja sprawdzająca, czy plik JSON istnieje i tworzenie go, jeśli nie
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({"expenses": [], "limits": {}}, file)

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikacja do zarządzania budżetem osobistym")

        # Dynamiczne skalowanie interfejsu
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Domyślna wielkość czcionki
        self.font_size = 24
        self.root.option_add("*Font", f"TkDefaultFont {self.font_size}")

        self.setup_ui()

    def setup_ui(self):
        # Zakładki
        tab_control = ttk.Notebook(self.root)

        self.add_tab = ttk.Frame(tab_control)
        self.history_tab = ttk.Frame(tab_control)
        self.summary_tab = ttk.Frame(tab_control)
        self.limits_tab = ttk.Frame(tab_control)
        self.settings_tab = ttk.Frame(tab_control)

        tab_control.add(self.add_tab, text="Dodaj wydatek")
        tab_control.add(self.history_tab, text="Historia wydatków")
        tab_control.add(self.summary_tab, text="Podsumowanie")
        tab_control.add(self.limits_tab, text="Limity")
        tab_control.add(self.settings_tab, text="Ustawienia")

        tab_control.grid(row=0, column=0, sticky="nsew")

        self.create_add_tab()
        self.create_history_tab()
        self.create_summary_tab()
        self.create_limits_tab()
        self.create_settings_tab()

    def load_data(self):
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    def save_data(self, data):
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def create_add_tab(self):
        for i in range(3):
            self.add_tab.rowconfigure(i, weight=1)
            self.add_tab.columnconfigure(i, weight=1)

        tk.Label(self.add_tab, text="Kwota:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry = tk.Entry(self.add_tab)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        tk.Label(self.add_tab, text="Kategoria:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.category_entry = tk.Entry(self.add_tab)
        self.category_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        tk.Label(self.add_tab, text="Data:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.date_entry = DateEntry(self.add_tab, date_pattern="yyyy-mm-dd")
        self.date_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        tk.Button(self.add_tab, text="Dodaj", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=20)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            date = self.date_entry.get()

            if not category:
                raise ValueError("Kategoria nie może być pusta.")

            data = self.load_data()
            data["expenses"].append({"amount": amount, "category": category, "date": date})
            self.save_data(data)

            messagebox.showinfo("Sukces", "Wydatek został dodany.")

            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))

    def create_history_tab(self):
        self.history_tab.rowconfigure(0, weight=1)
        self.history_tab.columnconfigure(0, weight=1)

        self.history_tree = ttk.Treeview(self.history_tab, columns=("Kwota", "Kategoria", "Data"), show="headings")
        self.history_tree.heading("Kwota", text="Kwota")
        self.history_tree.heading("Kategoria", text="Kategoria")
        self.history_tree.heading("Data", text="Data")
        self.history_tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(self.history_tab, orient="vertical", command=self.history_tree.yview)
        self.history_tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        tk.Button(self.history_tab, text="Odśwież", command=self.load_history).grid(row=1, column=0, pady=10)

    def load_history(self):
        for row in self.history_tree.get_children():
            self.history_tree.delete(row)

        data = self.load_data()
        for expense in data["expenses"]:
            self.history_tree.insert("", tk.END, values=(expense["amount"], expense["category"], expense["date"]))

    def create_summary_tab(self):
        self.summary_tab.rowconfigure(0, weight=1)
        self.summary_tab.columnconfigure(0, weight=1)

        self.summary_canvas = None
        tk.Button(self.summary_tab, text="Pokaż wykres", command=self.show_summary).grid(row=0, column=0, pady=10)

    def show_summary(self):
        data = self.load_data()
        category_totals = {}

        for expense in data["expenses"]:
            category = expense["category"]
            amount = expense["amount"]
            category_totals[category] = category_totals.get(category, 0) + amount

        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        if self.summary_canvas:
            self.summary_canvas.get_tk_widget().destroy()

        figure = plt.Figure(figsize=(6, 4), dpi=100)
        ax = figure.add_subplot(111)
        ax.pie(amounts, labels=categories, autopct="%1.1f%%")
        ax.set_title("Rozkład wydatków")

        self.summary_canvas = FigureCanvasTkAgg(figure, self.summary_tab)
        self.summary_canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")

    def create_limits_tab(self):
        for i in range(3):
            self.limits_tab.rowconfigure(i, weight=1)
            self.limits_tab.columnconfigure(1, weight=1)

        tk.Label(self.limits_tab, text="Kategoria:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.limit_category_entry = tk.Entry(self.limits_tab)
        self.limit_category_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        tk.Label(self.limits_tab, text="Limit:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.limit_entry = tk.Entry(self.limits_tab)
        self.limit_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        tk.Button(self.limits_tab, text="Ustaw", command=self.set_limit).grid(row=2, column=0, columnspan=2, pady=20)

    def set_limit(self):
        try:
            category = self.limit_category_entry.get()
            limit = float(self.limit_entry.get())

            if not category:
                raise ValueError("Kategoria nie może być pusta.")

            data = self.load_data()
            data["limits"][category] = limit
            self.save_data(data)

            messagebox.showinfo("Sukces", "Limit został ustawiony.")

            self.limit_category_entry.delete(0, tk.END)
            self.limit_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))

    def create_settings_tab(self):
        tk.Label(self.settings_tab, text="Regulacja rozmiaru czcionki:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.font_size_slider = ttk.Scale(
            self.settings_tab, from_=10, to=40, orient="horizontal", command=self.update_font_size
        )
        self.font_size_slider.set(self.font_size)
        self.font_size_slider.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def update_font_size(self, value):
        self.font_size = int(float(value))
        self.root.option_add("*Font", f"TkDefaultFont {self.font_size}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
    