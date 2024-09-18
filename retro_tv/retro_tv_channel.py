import os
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

def play_vlc(playlist):
    command = f"DISPLAY=:0 cvlc --fullscreen --no-video-title-show --playlist-autostart --loop {playlist}"
    print(f"Running command: {command}")
    result = os.system(command)
    if result != 0:
        print(f"Error running VLC command: {result}")

def stop_vlc():
    print("Stopping VLC...")
    os.system("pkill vlc")

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

def play_ad():
    command = f"DISPLAY=:0 cvlc --no-video-title-show --playlist-autostart --loop {ads_playlist}"
    print(f"Running command: {command}")
    result = os.system(command)
    if result != 0:
        print(f"Error running VLC command: {result}")

try:
    while True:
        current_show = get_current_show()

        if current_show == off_air_playlist:
            stop_vlc()
            play_vlc(off_air_playlist)
            time.sleep(60 * 60)  # Sleep for an hour before checking again
        else:
            stop_vlc()
            play_vlc(current_show)
            time.sleep(1200)
            play_ad()
            stop_vlc()
            play_vlc(current_show)

except KeyboardInterrupt:
    print("Script interrupted. Stopping VLC and exiting.")
    stop_vlc()
