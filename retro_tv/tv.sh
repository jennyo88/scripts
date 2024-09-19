#!/usr/bin/env bash

# Function to start the off-air playlist
off_air_playlist() {
    echo "Off-air period..."
    echo "Starting VLC with playlist: Off-Air"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/off_air.m3u
}

# Function to start the morning news playlist
morning_news_playlist() {
    echo "Starting VLC with playlist: Morning News"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/morning_news_playlist.m3u
}

# Function to start the game show playlist
game_show_playlist() {
    echo "Starting VLC with playlist: Game Show"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/game_show_playlist.m3u
}

# Function to start the soap opera playlist
soap_opera_playlist() {
    echo "Starting VLC with playlist: Soap Opera"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/soap_opera_playlist.m3u
}

# Function to start the cartoon playlist
cartoon_playlist() {
    echo "Starting VLC with playlist: Cartoon"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/cartoon_playlist.m3u
}

# Function to start the evening news playlist
evening_news_playlist() {
    echo "Starting VLC with playlist: Evening News"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/evening_news_playlist.m3u
}

# Function to start the sitcom playlist
sitcom_playlist() {
    echo "Starting VLC with playlist: Sitcom"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/sitcom_playlist.m3u
}

# Function to start the movie playlist
movie_playlist() {
    echo "Starting VLC with playlist: Movie"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/movie_playlist.m3u
}

# Function to start the talk show playlist
talk_show_playlist() {
    echo "Starting VLC with playlist: Talk Show"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/talk_show_playlist.m3u
}

# Function to start the infomercial playlist
infomercial_playlist() {
    echo "Starting VLC with playlist: Infomercial"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/infomercial_playlist.m3u
}

# Function to start the late-night movie playlist
late_night_movie_playlist() {
    echo "Starting VLC with playlist: Late-Night Movie"
    pkill -f vlc
    vlc --fullscreen --no-video-title-show --playlist-autostart --loop --random /home/jenny/playlists/late_night_movie_playlist.m3u
}

# Get the current day and hour
current_day=$(date +'%a') # Mon, Tue, Wed, Thu, Fri, Sat, Sun
current_hour=$(date +'%H')

# Determine which playlist to start based on the current time and day
case "$current_day" in
    Mon|Tue|Wed|Thu|Fri)
        if [ "$current_hour" -ge 06 ] && [ "$current_hour" -lt 09 ]; then
            morning_news_playlist
        elif [ "$current_hour" -ge 09 ] && [ "$current_hour" -lt 12 ]; then
            game_show_playlist
        elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 15 ]; then
            soap_opera_playlist
        elif [ "$current_hour" -ge 15 ] && [ "$current_hour" -lt 18 ]; then
            cartoon_playlist
        elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 20 ]; then
            evening_news_playlist
        elif [ "$current_hour" -ge 20 ] && [ "$current_hour" -lt 21 ]; then
            sitcom_playlist
        elif [ "$current_hour" -ge 21 ] && [ "$current_hour" -lt 23 ]; then
            movie_playlist
        elif [ "$current_hour" -ge 23 ] && [ "$current_hour" -lt 24 ]; then
            talk_show_playlist
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 06 ]; then
            off_air_playlist
        fi
        ;;
    Sat)
        if [ "$current_hour" -ge 06 ] && [ "$current_hour" -lt 12 ]; then
            cartoon_playlist
        elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 15 ]; then
            sports_playlist
        elif [ "$current_hour" -ge 15 ] && [ "$current_hour" -lt 19 ]; then
            sitcom_playlist
        elif [ "$current_hour" -ge 19 ] && [ "$current_hour" -lt 20 ]; then
            game_show_playlist
        elif [ "$current_hour" -ge 20 ] && [ "$current_hour" -lt 22 ]; then
            movie_playlist
        elif [ "$current_hour" -ge 22 ] && [ "$current_hour" -lt 24 ]; then
            sitcom_playlist
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 01 ]; then
            SNL_playlist
        elif [ "$current_hour" -ge 01 ] && [ "$current_hour" -lt 02 ]; then
            infomercial_playlist
        elif [ "$current_hour" -ge 02 ] && [ "$current_hour" -lt 04 ]; then
            late_night_movie_playlist
        elif [ "$current_hour" -ge 05 ] && [ "$current_hour" -lt 06 ]; then
            off_air_playlist
        fi
        ;;
    Sun)
        if [ "$current_hour" -ge 06 ] && [ "$current_hour" -lt 09 ]; then
            morning_news_playlist
        elif [ "$current_hour" -ge 09 ] && [ "$current_hour" -lt 12 ]; then
            talk_show_playlist
        elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 19 ]; then
            sports_playlist
        elif [ "$current_hour" -ge 19 ] && [ "$current_hour" -lt 20 ]; then
            game_show_playlist
        elif [ "$current_hour" -ge 20 ] && [ "$current_hour" -lt 23 ]; then
            movie_playlist
        elif [ "$current_hour" -ge 23 ] && [ "$current_hour" -lt 24 ]; then
            late_night_movie_playlist
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 02 ]; then
            sitcom_playlist
        fi
        ;;
esac
