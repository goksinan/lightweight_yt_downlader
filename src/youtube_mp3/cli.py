import click
from youtube_mp3.downloader import download_audio

@click.command()
@click.argument('url')
@click.option('--output-dir', '-o', default="./", help='Directory to save the MP3 file')
def main(url: str, output_dir: str):
    """Download YouTube video as MP3."""
    try:
        mp3_path = download_audio(url, output_dir)
        click.echo(f"Successfully downloaded: {mp3_path}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        exit(1)

if __name__ == '__main__':
    main()