#!/bin/bash

# Function to start VLC with the desired playlist
start_vlc() {
    local playlist_path=$1
    echo "Starting VLC with playlist: $playlist_path"
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random "$playlist_path" &
}

# Function to kill VLC if it's not playing the desired playlist
kill_vlc_if_needed() {
    local expected_playlist=$1

    # Get the command line of the running VLC process
    vlc_processes=$(pgrep -af vlc)

    # Check if VLC is running
    if [[ -n "$vlc_processes" ]]; then
        # Check if VLC is playing the correct playlist
        if ! echo "$vlc_processes" | grep -q "$expected_playlist"; then
            echo "Stopping VLC as it's playing a different playlist..."
            pkill -f vlc
        else
            echo "VLC is already playing the correct playlist. No action needed."
            return
        fi
    fi

    # Start VLC with the desired playlist if needed
    start_vlc "$expected_playlist"
}

# Define paths to playlists
CARTOON_PLAYLIST="/home/jenny/playlists/cartoon.m3u"
SITCOM_PLAYLIST="/home/jenny/playlists/sitcom.m3u"
GAME_SHOW_PLAYLIST="/home/jenny/playlists/game_show.m3u"
DRAMA_PLAYLIST="/home/jenny/playlists/drama.m3u"
MOVIE_PLAYLIST="/home/jenny/playlists/movie.m3u"
HORROR_PLAYLIST="/home/jenny/playlists/horror.m3u"
ADS_PLAYLIST="/home/jenny/playlists/ads.m3u"
OFF_AIR_PLAYLIST="/home/jenny/playlists/off_air.m3u"

# Function to handle off-air period
handle_off_air() {
    echo "Off-air period..."
    kill_vlc_if_needed "$OFF_AIR_PLAYLIST"
}

# Get the current hour
current_hour=$(date +'%H')

# Determine which playlist to start based on the current time
if [ "$current_hour" -ge 0 ] && [ "$current_hour" -lt 6 ]; then
    handle_off_air
elif [ "$current_hour" -ge 6 ] && [ "$current_hour" -lt 9 ]; then
    kill_vlc_if_needed "$CARTOON_PLAYLIST"
elif [ "$current_hour" -ge 9 ] && [ "$current_hour" -lt 12 ]; then
    kill_vlc_if_needed "$SITCOM_PLAYLIST"
elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 15 ]; then
    kill_vlc_if_needed "$GAME_SHOW_PLAYLIST"
elif [ "$current_hour" -ge 15 ] && [ "$current_hour" -lt 18 ]; then
    kill_vlc_if_needed "$DRAMA_PLAYLIST"
elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 21 ]; then
    kill_vlc_if_needed "$MOVIE_PLAYLIST"
else
    kill_vlc_if_needed "$HORROR_PLAYLIST"
fi
