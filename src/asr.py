from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import torchaudio

# Load model and processor (KinyaWhisper)
model_path = "benax-rw/KinyaWhisper"
processor = WhisperProcessor.from_pretrained(model_path)
model = WhisperForConditionalGeneration.from_pretrained(model_path)

def transcribe_audio(audio_path, save_path="transcribe/"):
    # Load and validate audio
    waveform, sample_rate = torchaudio.load(audio_path)

    if sample_rate != 16000:
        raise ValueError("Audio must be at 16kHz!")

    # Set generation config to avoid forced_decoder_ids errors
    generation_config = model.generation_config
    generation_config.forced_decoder_ids = None

    # Prepare input features and attention mask
    inputs = processor(
        waveform.squeeze().numpy(),
        sampling_rate=sample_rate,
        return_tensors="pt"
    )
    inputs["attention_mask"] = torch.ones_like(inputs["input_features"][:, :, 0])

    # Generate transcription
    predicted_ids = model.generate(
        inputs["input_features"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=5,
        no_repeat_ngram_size=1,
        suppress_tokens=[],
        generation_config=generation_config
    )

    # Decode output
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    print("🎙️ Transcription Output:", transcription)

    # Optionally save transcription
    import os
    os.makedirs(save_path, exist_ok=True)
    base_name = os.path.basename(audio_path).split('.')[0]
    with open(os.path.join(save_path, f"{base_name}.txt"), "a", encoding="utf-8") as f:
        f.write(transcription)

    return transcription
