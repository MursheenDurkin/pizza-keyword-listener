# 🍕 Pizza Keyword Listener

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-PyAudio-red?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A Python script that listens through your microphone and logs every time the word **"pizza"** is detected — complete with a timestamp and date. Built because my lecturer genuinely could not stop saying pizza. 🍕

---

## 🖥️ Example Output

```
========================================
        🍕 Pizza Keyword Listener
========================================

Keyword  : 'pizza'
Log file : pizza_log.txt

Press Ctrl+C to stop.

Calibrating microphone — stay quiet for 2 seconds...
Done. Listening...

Listening for 'pizza'...
  Heard: "has anyone mentioned pizza today"
  🍕 'pizza' detected!
  ✅ Logged at 2025-11-04 14:32:07

Listening for 'pizza'...
  No audio detected — listening again...
```

**pizza_log.txt**
```
🍕 Pizza Log
==============================
2025-11-04 14:32:07: 'pizza' detected.
2025-11-04 14:45:21: 'pizza' detected.
2025-11-04 15:01:53: 'pizza' detected.
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/barneyhk1804/pizza-keyword-listener.git
cd pizza-keyword-listener
```

### 2. (Recommended) Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ **PyAudio** can be fiddly to install. If it fails, try:
> - **Windows:** `pip install pipwin` then `pipwin install pyaudio`
> - **Linux:** `sudo apt install python3-pyaudio`
> - **macOS:** `brew install portaudio` then `pip install pyaudio`

### 4. Run it

```bash
python3 pizza_listener.py
```

Press **Ctrl+C** to stop. Detections are saved to `pizza_log.txt` in the same folder.

---

## 📁 Project Structure

```
├── pizza_listener.py   # The script
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores pizza_log.txt, __pycache__, venv, etc.
└── README.md
```

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — microphone input and Google Speech Recognition
- [PyAudio](https://pypi.org/project/PyAudio/) — audio stream handling

---

## 📋 Requirements

- Python 3.10+
- A working microphone
- Internet connection (uses Google Speech Recognition)
- Dependencies listed in `requirements.txt`

---

## 🙋 About

A fun little project built while learning Python — specifically around audio input, speech recognition, and file I/O. My lecturer had a habit of saying "pizza" constantly, so this felt like the only reasonable response.

---

*Made with ☕ and an unhealthy awareness of pizza mentions*
