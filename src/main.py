import os
from asr import transcribe_audio
from nlp import get_response
from ttls import speak

def main():
    print("🎙️ Kinyarwanda Voice Assistant")

    audio_path = "C:/Users/PC/PycharmProjects/kinya-voice-assistant/audio/rw-test01.mp3"

    if not os.path.exists(audio_path):
        print(f"❌ Audio file not found: {audio_path}")
        return

    print("🔊 Transcribing audio...")
    transcription = transcribe_audio(audio_path)
    print(f"📝 Recognized Text: {transcription}")

    print("🧠 Processing response...")
    response = get_response(transcription)
    print(f"🤖 Assistant: {response}")

    print("🔈 Speaking out response...")
    speak(response)

if __name__ == "__main__":
    main()
