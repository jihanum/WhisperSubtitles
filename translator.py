import os
import tkinter as tk
from tkinter import filedialog
from deep_translator import GoogleTranslator

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Select .srt file to translate:",
    filetypes=[("Subtitles", "*.srt")]
)

if not file_path:
    exit()

file_dir = os.path.dirname(file_path)
file_name_with_ext = os.path.basename(file_path)
file_name, _ = os.path.splitext(file_name_with_ext)
print(f"Selected: {file_name_with_ext}")

lang_input = input("\nEnter target languages separated by commas (e.g., 'es, pt, ko'): ").strip()
if not lang_input:
    exit()

target_languages = [lang.strip().lower() for lang in lang_input.split(",")]


def parse_srt(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    blocks = content.split('\n\n')
    parsed_blocks = []

    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            index = lines[0]
            timestamps = lines[1]
            text = '\n'.join(lines[2:])
            parsed_blocks.append({
                "index": index,
                "timestamps": timestamps,
                "text": text
            })

    return parsed_blocks


srt_data = parse_srt(file_path)
total_lines = len(srt_data)
print(f"Found {total_lines} blocks.")

for lang in target_languages:
    print(f"\nTranslating to '{lang}'...")

    try:
        translator = GoogleTranslator(source='auto', target=lang)
    except Exception as e:
        print(f"Language code '{lang}' is invalid.")
        continue

    new_srt_path = os.path.join(file_dir, f"{file_name}_{lang}.srt")

    with open(new_srt_path, "w", encoding="utf-8") as f:
        for i, block in enumerate(srt_data, start=1):
            original_text = block["text"]

            try:
                translated_text = translator.translate(original_text)
            except Exception as e:
                print(f"Failed to translate block {block['index']}. Using original text.")
                translated_text = original_text

            f.write(f"{block['index']}\n")
            f.write(f"{block['timestamps']}\n")
            f.write(f"{translated_text}\n\n")

            print(f"Progress: {i}/{total_lines} lines translated...")

    print(f"Saved to {new_srt_path}")

print("\nDone.")