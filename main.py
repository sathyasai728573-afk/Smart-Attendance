import cv2
import face_recognition
import pickle
from datetime import datetime
import mysql.connector
import tkinter as tk
from tkinter import ttk
import os



#dataset path
DATASET_PATH = "Z:/GRADEPROJ/dataset"



#Get classes automatically
def get_classes():
    return [f for f in os.listdir(DATASET_PATH)
            if os.path.isdir(os.path.join(DATASET_PATH, f))]
#class selection UI
def select_class():
    classes = get_classes()
    def start():
        selected = class_var.get()
        if selected:
            root.selected_class = selected
            root.destroy()
    root = tk.Tk()
    root.title("Select Class")
    root.geometry("300x150")
    root.configure(bg="#121212")
    tk.Label(root, text="Select Class",
             bg="#121212", fg="white",
             font=("Segoe UI", 12, "bold")).pack(pady=10)
    class_var = tk.StringVar()
    dropdown = ttk.Combobox(root, textvariable=class_var,
                            values=classes, state="readonly")
    dropdown.pack(pady=5)
    tk.Button(root, text="Start",
              command=start, bg="#3a86ff",
              fg="white").pack(pady=10)
    root.selected_class = None
    root.mainloop()

    return root.selected_class



#get class
current_class = select_class()
if not current_class:
    exit()



#mysql connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="attendance_system"
)
cursor = conn.cursor()



#load encodings
with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)



#Camera and recognition
cam = cv2.VideoCapture(0)
marked = set()
while True:
    ret, frame = cam.read()
    if not ret:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)
    for encoding, face in zip(encodings, faces):
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "unidentified"
        student_id = None
        student_class = None
        if True in matches:
            index = matches.index(True)
            student_id = data["ids"][index]
            name = data["names"][index]
            student_class = data["classes"][index]
            if student_class != current_class:
                continue
            date = datetime.now().strftime("%Y-%m-%d")
            sql = """
            INSERT IGNORE INTO attendance (student_id, name, class, date)
            VALUES (%s, %s, %s, %s)
            """
            values = (student_id, name, current_class, date)
            cursor.execute(sql, values)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Marked: {name} ({student_id})")
        #Display
        top, right, bottom, left = face
        label = name if not student_id else f"{student_id} - {name}"
        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, label, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    cv2.imshow(f"Attendance - {current_class}", frame)
    if cv2.waitKey(1) == ord('q'):  #for exiting the camera
        break
cam.release()
cv2.destroyAllWindows()
cursor.close()
conn.close()