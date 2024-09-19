#!/bin/bash

# Function to start the off-air playlist
off_air_playlist() {
    echo "Off-air period..."
    echo "Starting VLC with playlist: Off-Air"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/off_air.m3u
}

# Function to start the cartoon playlist
cartoon_playlist() {
    echo "Starting VLC with playlist: Cartoon"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/cartoon_playlist.m3u
}

# Function to start the sitcom playlist
sitcom_playlist() {
    echo "Starting VLC with playlist: Sitcom"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/sitcom_playlist.m3u
}

# Function to start the game show playlist
game_show_playlist() {
    echo "Starting VLC with playlist: Game Show"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/game_show_playlist.m3u
}

# Function to start the drama playlist
drama_playlist() {
    echo "Starting VLC with playlist: Drama"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/drama_playlist.m3u
}

# Function to start the movie playlist
movie_playlist() {
    echo "Starting VLC with playlist: Movie"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/movie_playlist.m3u
}

# Function to start the horror playlist
horror_playlist() {
    echo "Starting VLC with playlist: Horror"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/horror_playlist.m3u
}

# Get the current hour
current_hour=$(date +'%H')


# Determine which playlist to start based on the current time
if [ "$current_hour" -ge 0 ] && [ "$current_hour" -lt 6 ]; then
    off_air_playlist
elif [ "$current_hour" -ge 6 ] && [ "$current_hour" -lt 9 ]; then
    cartoon_playlist
elif [ "$current_hour" -ge 9 ] && [ "$current_hour" -lt 12 ]; then
    sitcom_playlist
elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 15 ]; then
    game_show_playlist
elif [ "$current_hour" -ge 15 ] && [ "$current_hour" -lt 18 ]; then
    drama_playlist
elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 21 ]; then
    movie_playlist
else
    horror_playlist
fi
