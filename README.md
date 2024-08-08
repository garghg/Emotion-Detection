# Emotion-Detection

## Overview

This Emotion Recognition App leverages OpenCV for face detection and DeepFace for emotion analysis. It provides a real-time video feed from your webcam and displays detected emotions with corresponding emojis and messages. The application features interactive buttons that appear based on the detected emotion, offering various actions such as playing music, sharing on social media, journaling, and relaxation exercises. 

### Applications of Changing GUI

The changing GUI based on detected emotions opens up numerous applications:

- **Personalized User Experience:** Tailors the application’s interface and suggestions to match the user’s current emotional state, making interactions more relevant and engaging.
- **Emotional Well-being:** Offers actionable suggestions and activities (e.g., music, journaling, relaxation exercises) that are aligned with the user's emotional condition, potentially aiding in emotional management and well-being.
- **Educational Tools:** Can be used in educational environments to provide feedback or encouragement based on student emotions, enhancing learning experiences.
- **Therapeutic Applications:** Supports mental health professionals by integrating with therapeutic tools that respond to clients' emotions, facilitating better support and interaction.
- **Customer Service:** Enhances customer service experiences by adapting the interface based on customer emotions, leading to more empathetic and effective support.

## Features

- Real-time face detection and emotion recognition.
- Emotion-based UI updates with emojis and messages.
- Interactive buttons that appear based on detected emotions.
- Support for multiple emotions: happy, sad, neutral, angry, and surprise.
- Actions include playing music, sharing on social media, opening a mood journal, and relaxation exercises.

## Requirements

- Python 3.x
- OpenCV
- DeepFace
- PyQt5
- A webcam

## Installation

1. **Clone the repository:**

2. **Install the required Python packages:**

    ```bash
    pip install opencv-python-headless deepface pyqt5
    ```

3. **Download Haar Cascade XML:**

    Ensure that `haarcascade_frontalface_default.xml` is located in the same directory as your script. You can download it from the [OpenCV GitHub repository](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml). _(also provided in the repository)_

## Usage

1. **Run the application:**

    ```bash
    python <your-script-name>.py
    ```

2. **Interact with the application:**

    - The application will start displaying video from your webcam.
    - The detected emotion will be shown along with an emoji and a message.
    - Based on the detected emotion, buttons for playing music, sharing on social media, journaling, or relaxation exercises will appear.
    - Click the buttons to perform the corresponding actions.

## Button Actions

- **Play Music:** Opens a web browser to a predefined URL (e.g., a YouTube playlist).
- **Share on Social Media:** Opens a web browser to a predefined URL for sharing a message on social media.
- **Mood Journal:** Opens a text editor (e.g., Notepad) for journaling.
- **Relaxation Exercise:** Opens a web browser to a predefined URL for a relaxation video.

## Reference: 
1. Emotion Detection logic based on [manish-9245's application](https://github.com/manish-9245/Facial-Emotion-Recognition-using-OpenCV-and-Deepface/blob/main/emotion.py)
