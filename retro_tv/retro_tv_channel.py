import os
import subprocess
import time
from datetime import datetime

def play_vlc(playlist):
    command = f"DISPLAY=:0 cvlc --fullscreen --no-video-title-show --playlist-autostart --loop {playlist}"
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Return code: {result.returncode}")
    print(f"STDOUT: {result.stdout.decode()}")
    print(f"STDERR: {result.stderr.decode()}")

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
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Return code: {result.returncode}")
    print(f"STDOUT: {result.stdout.decode()}")
    print(f"STDERR: {result.stderr.decode()}")

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
