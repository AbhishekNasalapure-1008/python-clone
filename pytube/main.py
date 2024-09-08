# from pytube import YouTube

# link=YouTube("https://youtu.be/1RW8XfqaS0Q?si=jJqjHxKIWBRwI8b8")

# video=link.streams.get_lowest_resolution()

# video.download()


from pytube import YouTube
import time

def download_video(url, retries=5):
    for i in range(retries):
        try:
            yt = YouTube(url)
            video = yt.streams.get_lowest_resolution()
            print(f"Downloading: {yt.title}")
            video.download()
            print("Download completed successfully!")
            return
        except Exception as e:
            print(f"An error occurred (attempt {i+1}/{retries}): {str(e)}")
            if i < retries - 1:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Max retries reached. Download failed.")

# URL of the video you want to download
video_url = "https://youtu.be/1RW8XfqaS0Q?si=jJqjHxKIWBRwI8b8"

# Attempt to download the video
download_video(video_url)