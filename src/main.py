import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap, QPainter, QFont
from PyQt5.QtCore import QTimer, Qt
from emotions import emotion_detector
import webbrowser

class EmotionRecognitionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize OpenCV video capture
        self.cap = cv2.VideoCapture(0)

        # Initialize emotion detector
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Set up the GUI
        self.setWindowTitle("Emotion Recognition")
        self.setGeometry(100, 100, 1200, 600)

        # Layouts
        self.image_label = QLabel()
        self.emotion_label = QLabel()
        self.message_label = QLabel()

        # Set default message
        self.message_label.setText("No emotion detected")
        self.message_label.setFont(QFont('Times New Roman', 20))
        self.message_label.setWordWrap(True)

        # Set default emotion text
        self.emotion_label.setFont(QFont('Arial', 24))
        self.emotion_label.setAlignment(Qt.AlignCenter)

        # Buttons
        self.music_button = QPushButton("Play Music")
        self.share_button = QPushButton("Share on Social Media")
        self.journal_button = QPushButton("Mood Journal")
        self.relax_button = QPushButton("Relaxation Exercise")

        # Set button styles
        button_style = """
            QPushButton {
                font-size: 16px;
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        self.music_button.setStyleSheet(button_style)
        self.share_button.setStyleSheet(button_style)
        self.journal_button.setStyleSheet(button_style)
        self.relax_button.setStyleSheet(button_style)

        # Connect buttons to functions
        self.music_button.clicked.connect(self.play_music)
        self.share_button.clicked.connect(self.share_on_social_media)
        self.journal_button.clicked.connect(self.open_mood_journal)
        self.relax_button.clicked.connect(self.start_relaxation)

        # Hide buttons initially
        self.music_button.hide()
        self.share_button.hide()
        self.journal_button.hide()
        self.relax_button.hide()

        # Vertical layout for buttons with spacing
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.music_button)
        self.button_layout.addWidget(self.share_button)
        self.button_layout.addWidget(self.journal_button)
        self.button_layout.addWidget(self.relax_button)
        self.button_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.button_layout.setAlignment(Qt.AlignCenter)  # Center the buttons

        # Horizontal layout for video feed, message, and buttons
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.image_label)
        h_layout.addSpacing(20)  # Add space between video feed and message
        h_layout.addWidget(self.message_label)
        h_layout.addSpacing(20)  # Add space between message and buttons
        h_layout.addLayout(self.button_layout)

        # Vertical layout to include the emotion text and video
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.emotion_label)
        v_layout.addLayout(h_layout)

        container = QWidget()
        container.setLayout(v_layout)
        self.setCentralWidget(container)

        # Timer to update the video feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 30 ms for approximately 30 FPS

        # Variables for emotion detection tracking
        self.previous_emotion = None
        self.emotion_frame_count = 0

    def update_frame(self):
        ret, img = self.cap.read()
        if not ret:
            return

        img = cv2.flip(img, 1)

        emotion, faces, gray = emotion_detector(img)

        # Check if the same emotion is detected for 3 consecutive frames
        if emotion == self.previous_emotion:
            self.emotion_frame_count += 1
        else:
            self.emotion_frame_count = 0
            self.previous_emotion = emotion

        # Show buttons if emotion is detected for 3 consecutive frames
        if self.emotion_frame_count >= 3 and (emotion == "happy" or emotion == "neutral" or emotion == "surprise"):
            self.show_happy_buttons()
        elif self.emotion_frame_count >= 3 and (emotion == "sad" or emotion == "angry"):
            self.show_sad_buttons()
        else:
            self.hide_buttons()

        # Mapping emotions to emoji Unicode characters and messages
        emoji_dict = {
            "happy": "😊",
            "sad": "😢",
            "neutral": "😐",
            "angry": "😠",
            "surprise": "😲"
        }

        message_dict = {
            "happy": "You look happy today! Keep smiling! Maybe play some music or share your happiness on social media? 😊",
            "sad": "It seems like you're feeling a bit down. Everything will be okay! 😢 Would you like to write down what's bothering you or watch a video to help you relax?",
            "neutral": "You're feeling neutral. Just another day! Maybe play some music or share some thoughts on social media? 😐",
            "angry": "You seem a bit angry. Take a deep breath! 😠 Would you like to write down what happened or watch a video to help you calm down?",
            "surprise": "Wow! Something surprised you! Maybe listen to some of your favorite music or share your thoughts on social media? 😲"
        }

        emoji = emoji_dict.get(emotion, "")
        message = message_dict.get(emotion, "No emotion detected")

        # Update the emotion label
        self.emotion_label.setText(emotion.capitalize())

        # Update the message label
        self.message_label.setText(message)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        # Convert OpenCV image (BGR) to QImage (RGB)
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        q_image = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)

        # Display the image in the QLabel
        self.image_label.setPixmap(QPixmap.fromImage(q_image))

        # Overlay the emoji
        if emoji:
            painter = QPainter(self.image_label.pixmap())
            painter.setFont(QFont('Arial', 50))
            painter.drawText(25, 75, emoji)
            painter.end()

        # Repaint to ensure the overlay is rendered correctly
        self.image_label.repaint()

    def show_happy_buttons(self):
        self.music_button.show()
        self.share_button.show()

    def show_sad_buttons(self):
        self.journal_button.show()
        self.relax_button.show()

    def hide_buttons(self):
        self.music_button.hide()
        self.share_button.hide()
        self.journal_button.hide()
        self.relax_button.hide()

    def play_music(self):
        # Example: Open a YouTube playlist based on mood
        webbrowser.open("...")

    def share_on_social_media(self):
        # Example: Share a message on Twitter: https://twitter.com/intent/tweet?text=I'm feeling great! 😊
        webbrowser.open("...")

    def open_mood_journal(self):
        # Example: Open a text editor
        webbrowser.open("notepad.exe")  # For Windows

    def start_relaxation(self):
        # Example: Play a relaxation video on YouTube
        webbrowser.open("...")

    def closeEvent(self, event):
        self.cap.release()
        cv2.destroyAllWindows()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmotionRecognitionApp()
    window.show()
    sys.exit(app.exec_())
