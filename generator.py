import os
import whisper
import torch
import tkinter as tk
from tkinter import filedialog

def get_optimal_whisper_model():
    if not torch.cuda.is_available():
        print("Defaulting to CPU.")
        return "base"

    vram_bytes = torch.cuda.get_device_properties(0).total_memory
    vram_gb = vram_bytes / (1024 ** 3)
    print(f"VRAM: {vram_gb:.2f} GB")

    if vram_gb >= 10.0:
        return "large"
    elif vram_gb >= 5.0:
        return "medium"
    elif vram_gb >= 2.0:
        return "small"
    else:
        return "base"

def format_timestamp(total_seconds: float) -> str:
    total_seconds_int = int(total_seconds)
    milliseconds = int(round((total_seconds - total_seconds_int) * 1000))

    if milliseconds >= 1000:
        milliseconds = 0
        total_seconds_int += 1

    hours = total_seconds_int // 3600
    minutes = (total_seconds_int % 3600) // 60
    seconds = total_seconds_int % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"GPU acceleration available: {torch.cuda.is_available()}")
optimal_model = get_optimal_whisper_model()

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Select file")

if not file_path:
    exit()

file_dir = os.path.dirname(file_path)
file_name_with_ext = os.path.basename(file_path)
file_name, _ = os.path.splitext(file_name_with_ext)
print(f"Selected: {file_name_with_ext}")

subtitle_save_path = os.path.join(file_dir, "Subtitles")
os.makedirs(subtitle_save_path, exist_ok=True)

print(f"\nLoading '{optimal_model}'...")
model = whisper.load_model(optimal_model, device=device)

transcription_data = model.transcribe(
    file_path,
    language=None,
    task="transcribe",
    verbose=True
)

detected_language = transcription_data.get("language", "auto")
print(f"\nDetected language: {detected_language.upper()}")


srt_path = os.path.join(subtitle_save_path, f"{file_name}_{detected_language}.srt")

print(f"Saving to: {srt_path}")

segments = transcription_data.get("segments", [])
if not segments:
    print("Whisper found 0 segments.")
else:
    try:
        with open(srt_path, "w", encoding="utf-8") as f:
            for idx, segment in enumerate(segments, start=1):
                start_time = format_timestamp(segment["start"])
                end_time = format_timestamp(segment["end"])
                text = segment["text"].strip()

                f.write(f"{idx}\n{start_time} --> {end_time}\n{text}\n\n")

        print(f"Wrote {len(segments)} subtitle entries.")
    except Exception as e:
        print(f"Error while writing file: {e}")

print(f"\nSubtitles folder: {subtitle_save_path}")