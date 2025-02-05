import os
import instaloader
import yt_dlp as ydl
from time import sleep

# Function to download Instagram Reels
def download_instagram_reel(url):
    try:
        loader = instaloader.Instaloader()
        # Using instaloader to load the post from the URL
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])  # Get the shortcode from URL
        # Download Reels from Instagram
        print(f"Downloading Instagram Reels from: {url}")
        loader.download_post(post, target="Instagram_Reels")
        print("Download complete!")
    except Exception as e:
        print(f"Error downloading Instagram Reels: {e}")

# Function to download Facebook Video
def download_facebook_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download the best quality video and audio
            'outtmpl': 'Facebook_Video/%(title)s.%(ext)s',  # Save with video title
            'quiet': False,
            'no_warnings': True
        }
        with ydl.YoutubeDL(ydl_opts) as ydl_instance:
            print(f"Downloading Facebook Video from: {url}")
            ydl_instance.download([url])
            print("Download complete!")
    except Exception as e:
        print(f"Error downloading Facebook video: {e}")

# Function to display the menu and handle user input
def show_menu():
    print("\nChoose the platform to download video:")
    print("1. Instagram")
    print("2. Facebook")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
            url = input("Enter the Instagram reel URL: ")
            download_instagram_reel(url)
        elif choice == '2':
            url = input("Enter the Facebook video URL: ")
            download_facebook_video(url)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()