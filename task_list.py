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
