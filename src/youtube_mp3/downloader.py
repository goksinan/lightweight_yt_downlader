from yt_dlp import YoutubeDL
import os

def download_audio(url: str, output_dir: str = "./") -> str:
    """
    Download YouTube video as MP3 using yt-dlp.
    
    Args:
        url: YouTube video URL
        output_dir: Directory to save the MP3 file
    
    Returns:
        str: Path to the downloaded MP3 file
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])
            info = ydl.extract_info(url, download=False)
            mp3_file = os.path.join(output_dir, f"{info['title']}.mp3")
            return mp3_file
            
    except Exception as e:
        raise Exception(f"Error downloading audio: {str(e)}")