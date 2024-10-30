# YouTube MP3 Downloader

A lightweight tool to download YouTube videos as MP3 files.

## Installation

```bash
poetry install
```

## Usage

```python
from youtube_mp3.downloader import download_audio

mp3_path = download_audio("YOUR_YOUTUBE_URL")
```

## Requirements
- Python 3.9+
- FFmpeg
- Poetry