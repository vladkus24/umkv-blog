import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime

class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Планувальник")

        self.tasks = []

        self.task_name_var = tk.StringVar()
        self.priority_var = tk.StringVar()
        self.due_date_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Task Name Label and Entry
        tk.Label(self.root, text="Назва завдання:").grid(row=0, column=0, sticky="e")
        task_name_entry = tk.Entry(self.root, textvariable=self.task_name_var)
        task_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Priority Label and Dropdown
        tk.Label(self.root, text="Пріорітет:").grid(row=1, column=0, sticky="e")
        priority_values = ["Без пріорітету", "Низький", "Середній", "Високий"]
        priority_dropdown = ttk.Combobox(self.root, textvariable=self.priority_var, values=priority_values)
        priority_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    def add_task(self):
        name = self.task_name_var.get()
        priority = self.priority_var.get()
        due_date = self.due_date_var.get()

        if name and priority and due_date:
            task = Task(name, priority, due_date)
            self.tasks.append(task)

            self.task_list_treeview.insert("", tk.END, text=task.name, values=(task.priority, task.due_date))

            self.task_name_var.set("")
            self.priority_var.set("")
            self.due_date_var.set("")
        else:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()