# YouTube MP3 Downloader

A lightweight tool to download YouTube videos as MP3 files.

## Installation

```bash
poetry install
```

## Usage

```python
from youtube_mp3.downloader import download_audio

download_audio("https://youtu.be/example")
```

```bash
cli.py "https://youtu.be/example" -o ./downloads
```

or for batch downloading, put all URLs in a txt file:

```bash
cli.py "all_urls.txt" -o ./downloads
```

## Requirements
- Python 3.9+
- FFmpeg
- Poetry