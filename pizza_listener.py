"""
pizza_listener.py
------------------
Listens through your microphone and logs every time the word
"pizza" is detected — with a timestamp and date.

Built because my lecturer genuinely could not stop saying pizza. 🍕

Usage:
    python3 pizza_listener.py

Press Ctrl+C to stop.

Requirements:
    pip install -r requirements.txt
"""

import os
import time
import datetime
import speech_recognition as sr


# ──────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────

KEYWORD        = "pizza"
LOG_FILE       = "pizza_log.txt"
LISTEN_TIMEOUT = 5    # seconds to wait for speech before cycling again
LOOP_DELAY     = 0.1  # small pause between cycles to reduce CPU usage


# ──────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────

def init_log(log_file: str) -> None:
    """Create the log file with a header if it doesn't already exist."""
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("🍕 Pizza Log\n")
            f.write("=" * 30 + "\n")
        print(f"[Info] Log file created: {log_file}")


def log_detection(keyword: str, log_file: str) -> None:
    """Write a timestamped entry to the log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{timestamp}: '{keyword}' detected.\n")
    print(f"  ✅ Logged at {timestamp}")


def listen_once(recognizer: sr.Recognizer, source: sr.Microphone) -> None:
    """
    Listen for a single audio chunk and check for the keyword.
    Times out cleanly if no speech is detected within LISTEN_TIMEOUT seconds.
    """
    print(f"\nListening for '{KEYWORD}'...")

    try:
        audio = recognizer.listen(source, timeout=LISTEN_TIMEOUT)
    except sr.WaitTimeoutError:
        print("  No audio detected — listening again...")
        return

    try:
        text = recognizer.recognize_google(audio)
        print(f"  Heard: \"{text}\"")
        if KEYWORD.lower() in text.lower():
            print(f"  🍕 '{KEYWORD}' detected!")
            log_detection(KEYWORD, LOG_FILE)

    except sr.UnknownValueError:
        print("  Could not understand audio — listening again...")
    except sr.RequestError as e:
        print(f"  [Error] Speech recognition service unavailable: {e}")


# ──────────────────────────────────────────
# ENTRY POINT
# ──────────────────────────────────────────

def main() -> None:
    print("=" * 40)
    print("        🍕 Pizza Keyword Listener       ")
    print("=" * 40)
    print(f"\nKeyword  : '{KEYWORD}'")
    print(f"Log file : {LOG_FILE}")
    print("\nPress Ctrl+C to stop.\n")

    init_log(LOG_FILE)

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Calibrating microphone — stay quiet for 2 seconds...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Done. Listening...\n")

        try:
            while True:
                listen_once(recognizer, source)
                time.sleep(LOOP_DELAY)
        except KeyboardInterrupt:
            print("\n\nStopped. Check pizza_log.txt for the full tally. 🍕")


if __name__ == "__main__":
    main()
