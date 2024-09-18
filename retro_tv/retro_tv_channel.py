import os
import subprocess
import time
from datetime import datetime

# Define paths for different playlists
cartoon_playlist = "/home/jenny/playlists/cartoon_playlist.m3u"
sitcom_playlist = "/home/jenny/playlists/sitcom_playlist.m3u"
game_show_playlist = "/home/jenny/playlists/game_show_playlist.m3u"
drama_playlist = "/home/jenny/playlists/drama_playlist.m3u"
movie_playlist = "/home/jenny/playlists/movie_playlist.m3u"
horror_playlist = "/home/jenny/playlists/horror_playlist.m3u"
ads_playlist = "/home/jenny/playlists/ads.m3u"
off_air_playlist = "/home/jenny/playlists/off_air.m3u"

# Function to play VLC media files with playlist shuffle
def play_vlc(playlist):
    command = f"DISPLAY=:0 vlc --fullscreen --no-video-title-show --playlist-autostart --loop --one-instance --playlist-enqueue --random {playlist}"
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Return code: {result.returncode}")
    print(f"STDOUT: {result.stdout.decode()}")
    print(f"STDERR: {result.stderr.decode()}")

# Function to play ads after each video
def play_ad():
    command = f"DISPLAY=:0 vlc --no-video-title-show --play-and-exit {ads_playlist}"
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Return code: {result.returncode}")
    print(f"STDOUT: {result.stdout.decode()}")
    print(f"STDERR: {result.stderr.decode()}")

# Function to stop VLC
def stop_vlc():
    print("Stopping VLC...")
    os.system("pkill vlc")

# Schedule function based on current time
def get_current_show():
    now = datetime.now()
    hour = now.hour

    if 6 <= hour < 9:
        return cartoon_playlist
    elif 9 <= hour < 12:
        return sitcom_playlist
    elif 12 <= hour < 15:
        return game_show_playlist
    elif 15 <= hour < 18:
        return drama_playlist
    elif 18 <= hour < 21:
        return movie_playlist
    elif 21 <= hour < 24:
        return horror_playlist
    else:
        return off_air_playlist

# Main loop
try:
    while True:
        current_show = get_current_show()

        # If it's off-air hours (12:01 AM to 5:59 AM), play the off-air playlist
        if current_show == off_air_playlist:
            stop_vlc()
            play_vlc(off_air_playlist)
            time.sleep(60 * 60)  # Sleep for an hour before checking again
        else:
            # Play the current show and add an ad after each video
            stop_vlc()
            play_vlc(current_show)
            time.sleep(5)  # Short sleep to allow VLC to start

            # Continuously monitor and play ads after each video
            while True:
                # After each video (assuming 30 mins per video), play an ad
                time.sleep(1800)  # Wait for 30 minutes (adjust according to actual video duration)
                play_ad()

except KeyboardInterrupt:
    print("Script interrupted. Stopping VLC and exiting.")
    stop_vlc()
