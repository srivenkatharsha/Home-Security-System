# Home Security System Using Image Processing

## Introduction
A home security system which utilises both face detection and motion detection system. When an intruder is detected, the system sends an alert to the owner remotely.

## Problem
Existing security solutions often require complex and expensive setups. This project aims to bridge the gap by providing an accessible and efficient security system tailored to homeowners' needs, by focusing on motion and face detection.

## Features
Our home security system boasts the following features:
- **Motion detection:** The motion detection system tracks movements and alerts the face detection system if significant motion is detected. 
- **Face detection:** The face detection feature utilizes ArcFace, a powerful deep learning model widely employed in face recognition tasks. ArcFace, known for its effectiveness in facial analysis, leverages convolutional neural networks (CNNs) to accurately detect and compare facial features within images or videos. In our project, when a face is detected, ArcFace captures a photo and performs a comparison against a database of unknown faces. If a face is not detected or fails to find a match, the alert system is activated.
- **Telegram integrated alert system:** When activated, the alert system sends real-time information to the owner. The information includes the captured photo and the date and time when the photo was taken. The owner can then take action accordingly.

## Installation and Usage
To install and use the home security system, follow these steps:

1. Clone the repository: `git clone https://github.com/example/home-security-system.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a virtual environment using the following command:
   - For Windows: `python -m venv venv`
   - For macOS/Linux: `python3 -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`
5. Create an environment file named `.env` and add the following contents:
    ```
    BOT_TOKEN=<your_bot_token>
    SYSTEM_OWNER_TELEGRAM_ID=<your_telegram_id>
    ```
6. Create a folder named "Known" and place the "Known.PNG" file inside it.
7. Create a folder named "Unknown".
8. In one terminal, run the following command to start the motion detector script (project root directory): `python SensitiveMotionDetector.py`
9. In another terminal, run the following command to start the Telegram bot script (project root directory): `python Bot/telegram_bot.py`
