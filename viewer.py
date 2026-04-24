#import packages!
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
import os



#dataset path
DATASET_PATH = "Z:/GRADEPROJ/dataset"



#MySQL connector and settings
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hidden",    #password is hidden change pass when you try use it
    database="attendance_system"
)
cursor = conn.cursor()



#get classes
def get_classes():
    return [f for f in os.listdir(DATASET_PATH)
            if os.path.isdir(os.path.join(DATASET_PATH, f))]



#Window
root = tk.Tk()
root.title("Attendance Viewer")
root.geometry("900x500")
root.configure(bg="#0b1120")



#STYLE
style = ttk.Style()
style.theme_use("default")



#Table style
style.configure("Treeview",
                background="#1e293b",
                foreground="white",
                rowheight=30,
                fieldbackground="#1e293b",
                bordercolor="#334155")
style.map("Treeview",
          background=[("selected", "#3b82f6")])



# Header style
style.configure("Treeview.Heading",
                background="#020617",
                foreground="white",
                font=("Segoe UI", 10, "bold"))



# Combobox style
style.configure("TCombobox",
                fieldbackground="#1e293b",
                background="#1e293b",
                foreground="white")



#panel
top = tk.Frame(root, bg="#0b1120")
top.pack(pady=15)



#class dropdown list
class_var = tk.StringVar()
dropdown = ttk.Combobox(
    top,
    textvariable=class_var,
    values=get_classes(),
    state="readonly",
    width=18,
    font=("Segoe UI", 10)
)
dropdown.grid(row=0, column=0, padx=10)



#date picker 
date_picker = DateEntry(
    top,
    width=15,
    background="#3b82f6",
    foreground="white",
    date_pattern="yyyy-mm-dd"
)
date_picker.grid(row=0, column=1, padx=10)



#table
columns = ("Student ID", "Name", "Class", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(fill="both", expand=True, padx=15, pady=10)



#load data
def load_data(event=None):
    selected_class = class_var.get()
    selected_date = date_picker.get()
    for row in tree.get_children():
        tree.delete(row)
    if selected_class:
        cursor.execute(
            "SELECT student_id, name, class, date FROM attendance WHERE class=%s AND date=%s",
            (selected_class, selected_date)
        )
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)



# Bind events
dropdown.bind("<<ComboboxSelected>>", load_data)
date_picker.bind("<<DateEntrySelected>>", load_data)



#buttons
btn_frame = tk.Frame(root, bg="#0b1120")
btn_frame.pack(pady=10)
def create_btn(text, command):
    return tk.Button(
        btn_frame,
        text=text,
        command=command,
        bg="#3b82f6",
        fg="white",
        activebackground="#2563eb",
        font=("Segoe UI", 10, "bold"),
        bd=0,
        padx=15,
        pady=5,
        cursor="hand2"
    )



#Reset button
reset_btn = create_btn("Reset", lambda: [class_var.set(""), load_data()])
reset_btn.grid(row=0, column=0, padx=10)



#Exit button
exit_btn = create_btn("Exit", root.destroy)
exit_btn.grid(row=0, column=1, padx=10)


#run
root.mainloop()
cursor.close()
conn.close()
