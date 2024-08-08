from deepface import DeepFace
import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def emotion_detector(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Check if any faces are detected
    if len(faces) != 0:
        # Analyze the image for emotions using DeepFace
        em_dict = DeepFace.analyze(img, actions=['emotion'])
        emotion = em_dict[0]['dominant_emotion']
    else:
        # If no faces are detected, return "unknown" for emotion
        emotion = "unknown"

    return emotion, faces, gray
