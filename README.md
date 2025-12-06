Generates an .srt file containing timed closed captions sourced from an input video or audio file. Can output translated closed captions.

Code is written to run on Nvidia GPUs.

Dependency installation commands:
- pip install openai-whisper
- pip install torch --index-url https://download.pytorch.org/whl/cu131 (**change to current version**)
- winget install Gyan.FFmpeg

Note: The audio/video file must be in the same directory.

Made by Ji Han Um
