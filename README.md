# Alex-virtual-assistant

Alex is a Python-based voice assistant that can respond to voice commands, fetch the latest news, open websites, and play songs on YouTube. It continuously listens for the wake word **"Alex"** and executes commands accordingly.

## 🚀 Features
- **Wake Word Detection**: Listens for "Alex" and responds.
- **Open Websites**: Open Google, YouTube, Facebook, and LinkedIn with voice commands.
- **Fetch News**: Retrieves the latest news headlines from NewsAPI.
- **Play Music on YouTube**: Searches for any song and plays it.
- **Speech Recognition**: Uses Google Speech-to-Text for command processing.
- **Text-to-Speech**: Converts responses to speech.

## Required Libraries:

speechrecognition (For voice input)
pyttsx3 (For text-to-speech)
requests (For fetching news)
webbrowser (For opening websites)
urllib.parse (For YouTube search)

## 🎤 How to Use
Run the program with command - python main.py
Say "Alex" to activate the assistant.
Give commands, like:
"Open Google" → Opens Google
"Play Lover" → Plays Lover on YouTube
"News" → Reads the latest news headlines