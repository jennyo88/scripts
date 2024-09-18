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

# Function to play video using VLC on the default VGA monitor
def play_vlc(playlist):
    # Set VLC to use the correct display environment (DISPLAY=:0 should work for most desktop setups)
    command = f"DISPLAY=:0 cvlc --fullscreen --no-video-title-show --playlist-autostart --loop {playlist}"
    print(f"Running command: {command}")
    os.system(command)

# Function to stop VLC
def stop_vlc():
    print("Stopping VLC...")
    os.system("pkill vlc")

# Get current show based on time
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

# Function to play ads randomly
def play_ad():
    command = f"DISPLAY=:0 cvlc --no-video-title-show --playlist-autostart --loop {ads_playlist}"
    print(f"Running command: {command}")
    os.system(command)

# Main loop to manage the retro TV schedule
try:
    while True:
        current_show = get_current_show()

        # Off-air hours (12:00 AM to 5:59 AM)
        if current_show == off_air_playlist:
            stop_vlc()
            play_vlc(off_air_playlist)
            time.sleep(60 * 60)  # Sleep for an hour before checking again
        else:
            stop_vlc()
            play_vlc(current_show)

            # Play ads every 20 minutes (1200 seconds)
            time.sleep(1200)
            play_ad()

            # Resume the current show after the ad
            stop_vlc()
            play_vlc(current_show)

except KeyboardInterrupt:
    # Handle Ctrl+C and stop VLC
    print("Script interrupted. Stopping VLC and exiting.")
    stop_vlc()
