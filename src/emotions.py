from deepface import DeepFace
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:

	_, img = cap.read()
	img = cv2.flip(img, 1)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	if len(faces) != 0:
		try:
			em_dict = DeepFace.analyze(img, actions = ['emotion'])
		except:
			pass
		emotion = em_dict[0]['dominant_emotion']
		cv2.putText(img, emotion, (25, 25), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 1)
	else:
		emotion = "unknown"
		cv2.putText(img, emotion, (25, 25), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 1)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		
	cv2.imshow('img',img)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()