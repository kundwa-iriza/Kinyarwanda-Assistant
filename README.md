# 🗣️ Kinyarwanda Voice Assistant

This is an open-source voice assistant for the Kinyarwanda language, featuring automatic speech recognition (ASR), natural language understanding (NLU), and text-to-speech (TTS). It allows users to ask questions in Kinyarwanda and get spoken responses.

---

## 🚀 Features

- **ASR with KinyaWhisper** – Converts spoken Kinyarwanda into text using a Whisper model fine-tuned for the language.
- **NLU with simple NLP matching** – Finds best-matching answers from a local Q&A database using fuzzy string matching.
- **TTS with Coqui TTS** – Synthesizes responses in natural-sounding speech.
- **Local audio playback** – Works on Windows, macOS, and Linux.

---

## 🧰 Technologies Used

- Python 3.8+
- HuggingFace Transformers
- Torchaudio
- Coqui TTS
- Git & GitHub

---

## 📁 Project Structure
```yaml
kinya-voice-assistant/ ├── data/ │ └── qa_pairs.json # Q&A knowledge base ├── audio/ │ └── response.wav # Generated speech ├── src/ │ ├── asr.py # Audio-to-text using KinyaWhisper │ ├── nlp.py # Text matching and response selection │ ├── ttls.py # Text-to-speech using Coqui TTS │ └── main.py # Main script ├── requirements.txt # Dependencies └── README.md # This file
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/kinya-voice-assistant.git
cd kinya-voice-assistant
```
2. Create Virtual Environment
```bash
python -m venv venv

# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
If you haven’t installed Coqui TTS yet:

```bash
pip install TTS
```
🧪 How to Run
Place a 16kHz WAV file in the project folder.

Update the path in src/main.py if needed.

Run the assistant:

```bash
python src/main.py
```
The assistant will transcribe the audio, find a matching response, and play the reply using Coqui TTS.

🗃️ Add Your Own Q&A
Edit the file at data/qa_pairs.json:

```json
{
  "amakuru yawe": "Ni meza cyane!",
  "witwa nde": "Nitwa Umufasha wanyu."
}
```
📌 Notes
KinyaWhisper may require GPU for faster transcription.

TTS uses Coqui’s multilingual model: tts_models/multilingual/multi-dataset/your_tts.

Improve pronunciation by adjusting text phonetically.

🤝 Contributing
Feel free to fork, contribute, and improve this voice assistant for Rwandan languages!

👋 Acknowledgements
Benax-RW/KinyaWhisper

Coqui TTS

Hugging Face Transformers

vbnet
Copy
Edit

Would you like this saved to a file (like `README.md`) or added to your GitHub project directly?
