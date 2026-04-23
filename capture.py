import cv2  #camera + image processing
import os   #Doing file creating and storage and path actions



# this down is the one where all data is gonna stored
BASE_PATH = "Z:/GRADEPROJ/dataset"



#Input
class_name = input("Enter Class (e.g., 10A): ").upper().strip() #irrespective of 10a or 10A both give 10A
name = input("Enter Student Name: ").upper().strip() #irrespective of sathya or SATHYA both give SATHYA
name = ''.join(c for c in name.upper() if c.isalnum()) #this part gives a cleanname for the file if input = Sathya@ ==> SATHYA irrespective of symbols



#this section generates auto ID
def generate_student_id(base_path, class_name):   #function!
    class_path = os.path.join(base_path, class_name)     #joins 2 paths base one and the class path
    if not os.path.exists(class_path):
        return f"{class_name}001"
    existing_folders = os.listdir(class_path)
    max_num = 0
    for folder in existing_folders:
        try:
            # folder format: 10A001_SATHYA
            id_part = folder.split("_")[0]
            num = int(id_part.replace(class_name, ""))
            max_num = max(max_num, num)
        except:
            continue
    new_num = max_num + 1
    return f"{class_name}{str(new_num).zfill(3)}"



#Generate ID
student_id = generate_student_id(BASE_PATH, class_name)
#this section create folder like dataset/12A/10A001_SATHYA
folder_name = f"{student_id}_{name}"
save_path = os.path.join(BASE_PATH, class_name, folder_name)
os.makedirs(save_path, exist_ok=True)
print(f"\nGenerated ID: {student_id}")
print(f"Saving to: {save_path}")



#this section is camera section
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
count = 0
MAX_IMAGES = 20    #stores no. of faces!!!
while True:
    ret, frame = cam.read()
    if not ret:
        print("Camera error")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        count += 1
        face = gray[y:y+h, x:x+w]
        file_path = os.path.join(save_path, f"{count}.jpg")
        cv2.imwrite(file_path, face)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print(f"Saved: {file_path}")
    cv2.imshow("Capturing Faces", frame)
    if count >= MAX_IMAGES:
        print("\nImage capture complete")
        break
        #this down will off break tht loop above
    if cv2.waitKey(1) == ord('q'):
        print("\nStopped manually")
        break



#release camera and ending line
cam.release()
cv2.destroyAllWindows()
print(f"\n Done: {name} ({student_id}) added to {class_name}")