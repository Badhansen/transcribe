# Audio Transcription Tool

This tool extracts audio from video files and transcribes it using OpenAI's Whisper model.

## Prerequisites

- Python 3.11 or later
- FFmpeg installed on your system
- uv (Python package installer)
- CUDA-compatible GPU (optional, for faster transcription)

## Installation

### 1. Install FFmpeg

#### macOS
```bash
brew install ffmpeg
```

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Windows
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add `ffmpeg` into the user `PATH`
1. Download the `.7z` or `.zip` file.
2. Extract the downloaded ZIP file to a folder `ffmpeg`.
3. Edit the path variable. `Path` -> `New` -> place the  `ffmpeg/bin` directory.
4. Save and restart the terminal.

*Before running the project, please check if `ffmpeg` is working in you computer or not.*
```bash
ffmpeg -version
```

### 2. Install uv (Modern Python Package Installer)

```bash
pip install uv
```

### 3. Set up the project

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/Badhansen/transcribe.git
cd transcribe
```

### 4. Create virtual environment and install dependencies

```bash
uv sync
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

## Usage

1. Place your video file in the project directory
2. Update the video filename in `main.py` if needed
3. Run the transcription:

```bash
python main.py
```

The transcription will be saved to `transcript.txt`.

## Dependencies

- ffmpeg-python: Python bindings for FFmpeg
- openai-whisper: OpenAI's Whisper speech recognition model
- PyTorch: Required for Whisper model execution
