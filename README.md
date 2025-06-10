# 🚗 Driver Drowsiness Detection System

A real-time computer vision project that detects driver drowsiness using webcam video feed and facial landmarks. It raises audio alerts for drowsy or sleepy states to help prevent accidents.

## 📌 Features

- Real-time face and eye detection using `dlib` and `OpenCV`
- Calculates Eye Aspect Ratio (EAR) to detect:
  - **Active**
  - **Drowsy**
  - **Sleeping**
- Plays warning sounds:
  - `drowsy.mp3` for drowsiness
  - `sleepy.mp3` for closed eyes / sleep detection
- Uses threading to avoid audio blocking the main loop

## 📁 Project Structure

Driver-Drowsiness-Detection/
├── driver_drowsiness.py
├── sleepy.mp3
├── drowsy.mp3
└── shape_predictor_68_face_landmarks.dat

## 🛠 Requirements

- Python 3.x
- OpenCV
- dlib
- imutils
- playsound

Install them using pip:

pip install opencv-python dlib imutils playsound


## 🔧 Setup Instructions

1. Clone or download this repository.
2. Download the `shape_predictor_68_face_landmarks.dat` file from:  
   [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
3. Extract and place the `.dat` file in the same directory as your Python script.
4. In `driver_drowsiness.py`, update the file paths if necessary:
   ```python
   predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
   play_sound("sleepy.mp3")
   play_sound("drowsy.mp3")

▶️ How to Run
Run the script using Python:

python driver_drowsiness.py
Ensure your webcam is enabled.

Press ESC to stop the application.

 Sample Output
Status shown on screen: Active, Drowsy, or SLEEPING!!!

White dots indicate facial landmarks.

Colored rectangle shows face detection.

Audio alerts are triggered automatically based on state.

🙋‍♀️ Author
M R Sree Akshaya

Project based on OpenCV and dlib facial landmark detection
