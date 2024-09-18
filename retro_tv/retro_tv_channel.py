import os
import subprocess
import sys
import time

# Define paths for different playlists
playlists = {
    "cartoon": "/home/jenny/playlists/cartoon_playlist.m3u",
    "sitcom": "/home/jenny/playlists/sitcom_playlist.m3u",
    "game_show": "/home/jenny/playlists/game_show_playlist.m3u",
    "drama": "/home/jenny/playlists/drama_playlist.m3u",
    "movie": "/home/jenny/playlists/movie_playlist.m3u",
    "horror": "/home/jenny/playlists/horror_playlist.m3u",
    "off_air": "/home/jenny/playlists/off_air.m3u",
    "ads": "/home/jenny/playlists/ads.m3u"
}

def play_vlc(playlist):
    command = f"DISPLAY=:0 vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random {playlist}"
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Return code: {result.returncode}")
    print(f"STDOUT: {result.stdout.decode()}")
    print(f"STDERR: {result.stderr.decode()}")

def stop_vlc():
    print("Stopping VLC...")
    os.system("pkill vlc")

def play_ad():
    command = f"DISPLAY=:0 vlc --no-video-title-show --play-and-exit {playlists['ads']}"
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Return code: {result.returncode}")
    print(f"STDOUT: {result.stdout.decode()}")
    print(f"STDERR: {result.stderr.decode()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a playlist type (cartoon, sitcom, game_show, drama, movie, horror, off_air).")
        sys.exit(1)

    playlist_type = sys.argv[1]

    if playlist_type not in playlists:
        print(f"Invalid playlist type: {playlist_type}")
        sys.exit(1)

    # Stop any currently running VLC instance
    stop_vlc()

    # Play the selected playlist
    play_vlc(playlists[playlist_type])
