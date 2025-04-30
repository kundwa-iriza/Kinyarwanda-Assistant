import os
import platform
import soundfile as sf
from TTS.api import TTS

# Load Coqui TTS model that supports multilingual speech
tts_model = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)


def speak_text(text, output_path="audio/response.wav"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Generate speech (assumes Kinyarwanda is detected automatically or closely matches phonetic)
    tts_model.tts_to_file(text=text, file_path=output_path)

    # Play the audio depending on OS
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system(f"start {output_path}")
    elif system_platform == "Darwin":  # MacOS
        os.system(f"afplay {output_path}")
    else:  # Linux
        os.system(f"xdg-open {output_path}")
