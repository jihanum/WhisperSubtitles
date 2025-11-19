Generates an .srt file containing timed closed captions sourced from an input video or audio file. Can output translated closed captions.

Requires openai-whisper, CUDA PyTorch, and ffmpeg to function.

Dependency installation commands:
- pip install openai-whisper
- pip install torch --index-url https://download.pytorch.org/whl/cu130 (**change to current version**)
- winget install Gyan.FFmpeg

Instructions to Run:
1. Locate the ccGen.py script
2. Place the input file in the same directory.
3. Execute ccGen.py inside the same directory ("python ccGen.py")

Made by Ji Han Um
