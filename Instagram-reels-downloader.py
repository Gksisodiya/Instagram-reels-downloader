import os
import requests
from bs4 import BeautifulSoup
import time

def download_reel(url):
    """Downloads an Instagram Reel video using web scraping."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

        # Fetch the page content with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML to find the video URL
        soup = BeautifulSoup(response.text, 'html.parser')
        video_tag = soup.find('meta', property='og:video')

        if not video_tag:
            print("❌ Reel video URL not found. Instagram may be blocking access.")
            return

        video_url = video_tag['content']

        # Download the video
        video_response = requests.get(video_url, headers=headers)
        video_response.raise_for_status()

        # Ensure "downloads" folder exists
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        # Generate a unique filename
        filename = os.path.join("downloads", f"reel_{int(time.time())}.mp4")

        with open(filename, 'wb') as f:
            f.write(video_response.content)

        print(f"✅ Reel downloaded successfully! Saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    reel_url = input("Enter the Instagram Reel URL: ")
    download_reel(reel_url)