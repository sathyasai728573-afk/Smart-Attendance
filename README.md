# Face Recognition Attendance System

## Overview
This project is a face recognition-based attendance system that automatically detects and identifies individuals using a webcam and records their attendance with timestamps. It reduces manual effort and improves accuracy and efficiency.

## Repository
https://github.com/sathyasai728573-afk/Smart-Attendance

## Features
- Real-time face detection and recognition
- Automatic attendance marking with date and time
- Pre-trained face encodings for faster processing
- Simple and modular structure
- Easy to extend and customize

## Technologies Used
- Python
- OpenCV
- face_recognition
- NumPy
- dlib

## Project Structure

├── capture.py  
├── train.py  
├── encodings.pkl  
├── main.py  
├── app.py  
├── viewer.py  
├── requirements.txt  

## Installation
1. Clone the repository  
git clone https://github.com/sathyasai728573-afk/Smart-Attendance.git  
cd Smart-Attendance  

2. Create a virtual environment  
python -m venv venv  

3. Activate the environment  
venv\Scripts\activate   (Windows)  
source venv/bin/activate   (Mac/Linux)  

4. Install dependencies  
pip install -r requirements.txt  

## Usage
Run the following commands step by step:

python capture.py  
python train.py  
python main.py  
python viewer.py  

## App Gui Feature
by simply running this app.py file you can directly access to all the files easily without jumping from any files.
run this to use app.py

python app.py

## How It Works
The system captures facial images, generates encodings, detects faces in real-time through a webcam, compares them with stored encodings, and records attendance with timestamps.

## Use Cases
- Schools and colleges  
- Offices and workplaces  
- Secure entry systems  

## Future Improvements
- GUI enhancements  
- Database integration (MySQL)  
- Cloud-based storage  
- Mobile application support  

## License
This project is licensed under the MIT License.

## Author
Sathya Sai
