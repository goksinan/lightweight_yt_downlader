import click
from pathlib import Path
from typing import List
from youtube_mp3.downloader import download_audio

def read_urls_from_file(file_path: str) -> List[str]:
    """Read URLs from a text file, skipping empty lines and stripping whitespace."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def process_url(url: str, output_dir: str) -> bool:
    """Process a single URL and return True if successful."""
    try:
        mp3_path = download_audio(url, output_dir)
        click.echo(f"Successfully downloaded: {mp3_path}")
        return True
    except Exception as e:
        click.echo(f"Error downloading {url}: {str(e)}", err=True)
        return False

@click.command()
@click.argument('input_path')
@click.option('--output-dir', '-o', default="./", help='Directory to save the MP3 files')
def main(input_path: str, output_dir: str):
    """
    Download YouTube video(s) as MP3.
    
    INPUT_PATH can be either a single URL or a path to a .txt file containing URLs (one per line).
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Determine if input is a file or direct URL
    if input_path.endswith('.txt'):
        try:
            urls = read_urls_from_file(input_path)
            if not urls:
                click.echo("Error: No valid URLs found in the file.", err=True)
                exit(1)
                
            total = len(urls)
            successful = 0
            click.echo(f"Found {total} URLs to process...")
            
            for i, url in enumerate(urls, 1):
                click.echo(f"\nProcessing URL {i}/{total}: {url}")
                if process_url(url, output_dir):
                    successful += 1
                    
            click.echo(f"\nComplete! Successfully downloaded {successful}/{total} files.")
            if successful != total:
                exit(1)
                
        except FileNotFoundError:
            click.echo(f"Error: File '{input_path}' not found.", err=True)
            exit(1)
        except Exception as e:
            click.echo(f"Error reading file: {str(e)}", err=True)
            exit(1)
    else:
        # Handle single URL
        if not process_url(input_path, output_dir):
            exit(1)

if __name__ == '__main__':
    main()