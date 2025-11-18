import os.path
import whisper

print("\nNote: Python file must be placed in same directory as video\n")

fileName = input("File name: ")
video_path = os.path.abspath(os.path.join(os.path.dirname(__file__), fileName))

print("Target: " + video_path)

isTranslate = bool(input("\nTranslate? "))

if isTranslate:
    targetLanguage = input("Select language: ")

# From Subtitle Generator
subtitleSavePath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Subtitles', fileName))
if not os.path.exists(subtitleSavePath):
    os.makedirs(subtitleSavePath)


print("\nLoading model...")
model = whisper.load_model("medium", device="cuda")

print("\nTranscribing...\n")

if isTranslate:
    result = model.transcribe(video_path, language=targetLanguage, task="transcribe", verbose=True)
else:
    result = model.transcribe(video_path, verbose=True)

# Timestamp function
def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# SRT file

if isTranslate:
    SRT_PATH = os.path.join(subtitleSavePath, fileName + '_' + targetLanguage + '.srt')
else:
    SRT_PATH = os.path.join(subtitleSavePath, fileName + '.srt')

with open(SRT_PATH, "w", encoding="utf-8") as f:
    for idx, segment in enumerate(result["segments"], start=1):
        start_time = format_timestamp(segment["start"])
        end_time = format_timestamp(segment["end"])
        text = segment["text"].strip()

        f.write(f"{idx}\n{start_time} --> {end_time}\n{text}\n\n")

print("\nSubtitles generated and saved.")