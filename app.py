import tkinter as tk
from tkinter import messagebox
import subprocess

# 🔧 Python path (your virtual env)
PYTHON_PATH = "new_env\\Scripts\\python"

# ---------- FUNCTIONS ----------

def run_script(script_name):
    try:
        subprocess.run([PYTHON_PATH, script_name])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_student():
    run_script("capture.py")

def train_model():
    run_script("train.py")

def start_attendance():
    run_script("main.py")

def view_attendance():
    run_script("viewer.py")

def exit_app():
    if messagebox.askyesno("Exit", "Exit application?"):
        root.destroy()

# ---------- MAIN WINDOW ----------

root = tk.Tk()
root.title("Smart Attendance System")
root.geometry("520x540")
root.configure(bg="#0f172a")

# ---------- HEADER ----------

header = tk.Frame(root, bg="#0f172a")
header.pack(pady=30)

tk.Label(
    header,
    text="SMART ATTENDANCE",
    font=("Segoe UI", 18, "bold"),
    fg="#e2e8f0",
    bg="#0f172a"
).pack()

tk.Label(
    header,
    text="Face Recognition • MySQL • Multi-Class",
    font=("Segoe UI", 9),
    fg="#94a3b8",
    bg="#0f172a"
).pack()

# ---------- BUTTON FRAME ----------

frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=10)

# 🎨 Modern Button with subtitle (lore)
def modern_button(text, command, color, subtitle=None):
    container = tk.Frame(frame, bg="#0f172a")
    container.pack(pady=8)

    btn = tk.Label(
        container,
        text=text,
        bg=color,
        fg="white",
        font=("Segoe UI", 11, "bold"),
        width=28,
        height=2,
        cursor="hand2"
    )

    def on_enter(e):
        btn.config(bg="#1e293b")

    def on_leave(e):
        btn.config(bg=color)

    btn.bind("<Button-1>", lambda e: command())
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    btn.pack()

    # 🔥 Subtitle (lore)
    if subtitle:
        tk.Label(
            container,
            text=subtitle,
            font=("Segoe UI", 8),
            fg="#94a3b8",
            bg="#0f172a"
        ).pack(pady=2)

# ---------- BUTTONS ----------

modern_button(
    "Register Student",
    add_student,
    "#2563eb",
    "Add new student face data"
)

modern_button(
    "Train AI Model",
    train_model,
    "#f59e0b",
    "Only required after adding new students"
)

modern_button(
    "Start Attendance",
    start_attendance,
    "#16a34a",
    "Start face recognition attendance"
)

modern_button(
    "View Attendance",
    view_attendance,
    "#7c3aed",
    "View class-wise attendance records"
)

modern_button(
    "Exit",
    exit_app,
    "#dc2626"
)

# ---------- FOOTER ----------

tk.Label(
    root,
    text="Powered by AI • Designed by Sathyasai",
    font=("Segoe UI", 8),
    fg="#64748b",
    bg="#0f172a"
).pack(side="bottom", pady=15)

# ---------- RUN ----------

root.mainloop()