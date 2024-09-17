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

# Function to play video using VLC with PulseAudio
def play_vlc(playlist):
    os.system(f"DISPLAY=:0 cvlc --aout=pulse --one-instance --no-playlist-enqueue --playlist-autostart --loop --no-video-title-show {playlist}")

# Function to stop VLC
def stop_vlc():
    os.system("pkill vlc")

# Function to insert ads randomly with PulseAudio
def play_ad():
    os.system(f"DISPLAY=:0 cvlc --aout=pulse --one-instance --no-playlist-enqueue --no-video-title-show --playlist-autostart {ads_playlist}")

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

# Wait for Bluetooth connection before starting
def wait_for_bluetooth(mac_address):
    print(f"Waiting for Bluetooth device {mac_address} to connect...")
    while not is_bluetooth_connected(mac_address):
        print("Bluetooth not connected. Checking again in 5 seconds...")
        time.sleep(5)
    print("Bluetooth connected!")
    time.sleep(5)  # Wait an additional 5 seconds to ensure audio routing

def is_bluetooth_connected(mac_address):
    result = os.popen(f"bluetoothctl info {mac_address}").read()
    return "Connected: yes" in result

# Wait for Bluetooth connection before starting
wait_for_bluetooth("00:25:DB:12:0F:C1")  # Replace with your Bluetooth MAC address

# Main loop
while True:
    current_show = get_current_show()

    # Check if it's off-air hours (12:00 AM to 5:59 AM)
    if current_show == off_air_playlist:
        # Don't kill VLC, but switch to off-air playlist
        play_vlc(off_air_playlist)
        time.sleep(60 * 60)  # Check again in an hour
    else:
        # Play the current show
        stop_vlc()  # Stop any previous instances
        play_vlc(current_show)

        # Play ads every 20 minutes (1200 seconds)
        time.sleep(1200)
        stop_vlc()  # Stop current show before playing ads
        play_ad()

        # Resume the current show after the ad
        stop_vlc()  # Stop the ad instance
        play_vlc(current_show)
