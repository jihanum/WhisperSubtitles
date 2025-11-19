Generates an .srt file containing timed closed captions sourced from an input video or audio file. Can output translated closed captions.

Requires openai-whisper, CUDA PyTorch, and ffmpeg to function. Code is written to run on Nvidia GPUs.

Dependency installation commands:
- pip install openai-whisper
- pip install torch --index-url https://download.pytorch.org/whl/cu130 (**change to current version**)
- winget install Gyan.FFmpeg

Note: The audio/video file must be in the same directory, although it may be configured.

Made by Ji Han Um
