import cv2  # For image processing
import numpy as np  # For numerical operations
import dlib  # For face detection and landmarks
from imutils import face_utils  # For converting dlib shapes to numpy
from playsound import playsound
import threading

# Start webcam
cap = cv2.VideoCapture(0)

# Load face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\cv_project_driver_drowsiness\Driver-Drowsiness-Detection-master\shape_predictor_68_face_landmarks (1).dat")

# Variables to track status
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

# Distance between two points
def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

# Eye aspect ratio calculation
def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    if ratio > 0.25:
        return 2  # Open
    elif 0.21 < ratio <= 0.25:
        return 1  # Drowsy
    else:
        return 0  # Closed

def play_sound(file):
    threading.Thread(target=playsound, args=(file,), daemon=True).start()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    face_frame = frame.copy()  # Always define to avoid crash

    for face in faces:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()

        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # Eye landmark points
        left_blink = blinked(landmarks[36], landmarks[37],
                             landmarks[38], landmarks[41],
                             landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43],
                              landmarks[44], landmarks[47],
                              landmarks[46], landmarks[45])

        # Drowsiness logic
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 6:
                status = "SLEEPING !!!"
                color = (255, 0, 0)
                play_sound(r"C:\cv_project_driver_drowsiness\Driver-Drowsiness-Detection-master\sleepy.mp3")
                
        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                status = "Drowsy !"
                color = (0, 0, 255)
                play_sound(r"C:\cv_project_driver_drowsiness\Driver-Drowsiness-Detection-master\drowsy.mp3")
        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 6:
                status = "Active :)"
                color = (0, 255, 0)

        # Display status
        cv2.putText(frame, status, (100, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        # Draw all landmarks
        for (x, y) in landmarks:
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    # Show result
    cv2.imshow("Frame", frame)
    if len(faces) > 0:
        cv2.imshow("Result of detector", face_frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
