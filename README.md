# Enhancing User Experience using Text-to-Speech Systems

### Assistive Technology Project | Python | Google Text-to-Speech (gTTS)

---

## Overview

This project implements a **Text-to-Speech (TTS) system** that converts written text into spoken audio using the **Google Text-to-Speech (gTTS) API**.
The goal of this project is to improve **accessibility and user interaction** by enabling applications to deliver information through voice output.

The system can read **user-entered text** or **text from files** and generate an **audio output in MP3 format**, making it suitable for accessibility tools such as **screen readers, voice-enabled learning platforms, and assistive technologies**.

---

## Key Features

* Converts **text into natural-sounding speech**
* Supports **manual text input**
* Supports **file-based text input**
* Generates **MP3 audio output**
* Simple and modular **Python implementation**
* Designed for **accessibility-focused applications**

---

## Tech Stack

* **Programming Language:** Python
* **Library:** Google Text-to-Speech (gTTS)
* **Audio Playback:** Playsound
* **Version Control:** Git & GitHub

---

## Project Structure

```
text-to-speech-system
│
├── app.py
├── tts_engine.py
├── requirements.txt
├── README.md
│
├── input_text
│   └── sample.txt
│
├── output_audio
│   └── speech.mp3
│
└── utils
    └── file_handler.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/text-to-speech-system.git
cd text-to-speech-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

Run the main application:

```bash
python app.py
```

You will be prompted to:

1. Enter text manually
2. Read text from a file

The program will convert the text into **speech** and save the audio file in:

```
output_audio/speech.mp3
```

---

## Applications

This project can be used in various **assistive and interactive systems**, including:

* Screen readers for visually impaired users
* Voice-based educational tools
* Accessibility support in web applications
* Voice notification systems
* Interactive AI assistants

---

## Future Enhancements

* Support for **multiple languages**
* Adjustable **speech speed and tone**
* **Web interface** using Streamlit or Flask
* Integration with **voice assistants**

---

## Author

**Byreddy Sai Reddy**
Electronics and Communication Engineering
SR University, Warangal

Interested in **Software Development, AI Applications, and Accessibility Technologies**

---
