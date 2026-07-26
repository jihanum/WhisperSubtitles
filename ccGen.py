import os.path
import whisper
import torch

print("Is GPU acceleration available? ", torch.cuda.is_available())

print("Select the file.")
# Function; open a file explorer dialog prompt to select the file
# filename =
# file_dir =

isTranslate = bool(input("\nTranslate? "))
if isTranslate:
    targetLanguage = [input("Enter the target language: ")]

# From Subtitle Generator
subtitleSavePath = # output next to video file, in subtitles folder

print("\nLoading model...")
# Implement an autoselection function
model = whisper.load_model("medium", device="cuda")

print("\nTranscribing...\n")
# implement a progress bar

if isTranslate:
    for language in targetLanguage:
        result[] = model.transcribe(fileName, language=language, task="transcribe", verbose=True) # find how to get the index number of language
else:
    result[] = model.transcribe(fileName, verbose=True)

# Timestamp function
def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# SRT file

for language in result:
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

print("\nSubtitles generated and saved. Ready for next file?")