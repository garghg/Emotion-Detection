#Reference: https://github.com/manish-9245/Facial-Emotion-Recognition-using-OpenCV-and-Deepface/blob/main/emotion.py

from deepface import DeepFace
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def emotion_detector(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) != 0:
        em_dict = DeepFace.analyze(img, actions = ['emotion'])
        emotion = em_dict[0]['dominant_emotion']
    else:
        emotion = "unknown"

    return emotion, faces, gray