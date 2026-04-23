import os
import face_recognition
import pickle

# 📁 Dataset path
DATASET_PATH = "Z:/GRADEPROJ/dataset"

encodings = []
ids = []
names = []
classes = []

print("🔄 Training started...")

for class_name in os.listdir(DATASET_PATH):
    class_path = os.path.join(DATASET_PATH, class_name)

    if not os.path.isdir(class_path):
        continue

    for folder_name in os.listdir(class_path):
        person_path = os.path.join(class_path, folder_name)

        if not os.path.isdir(person_path):
            continue

        try:
            # 📌 Format: 10A001_SATHYA
            student_id, name = folder_name.split("_", 1)
        except:
            print(f"⚠️ Skipping invalid folder: {folder_name}")
            continue

        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)

            try:
                image = face_recognition.load_image_file(image_path)
                encoding = face_recognition.face_encodings(image)

                if encoding:
                    encodings.append(encoding[0])
                    ids.append(student_id)
                    names.append(name)
                    classes.append(class_name)

                    print(f"✅ Encoded: {student_id} - {name} ({class_name})")

            except Exception as e:
                print(f"❌ Error processing {image_path}: {e}")

# 💾 Save data
data = {
    "encodings": encodings,
    "ids": ids,
    "names": names,
    "classes": classes
}

with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("\n🎉 Training completed successfully!")
print(f"Total faces encoded: {len(encodings)}")