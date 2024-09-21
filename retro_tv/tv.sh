#!/usr/bin/env bash

# Function to check if cvlc is running
check_cvlc_running() {
    if pgrep -x "cvlc" > /dev/null; then
        echo "VLC is already running. Exiting..."
        exit 1
    fi
}

# Function to start the off-air playlist
off_air_playlist() {
    check_cvlc_running
    echo "Off-air period..."
    echo "Starting DISPLAY=:0 cvlc with playlist: Off-Air"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/off_air.m3u
}

# Function to start the morning news playlist
morning_news_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Morning News"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/morning_news_playlist.m3u
}

# Function to start the evening news playlist
evening_news_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Evening News"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/evening_news_playlist.m3u
}

# Function to start the infomercial playlist
infomercial_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Infomercial"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/infomercial_playlist.m3u
}

# Function to start the morning news playlist
SNL_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: SNL"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/SNL_playlist.m3u
}

# Function to start the game show playlist
game_show_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Game Show"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/game_show_playlist.m3u
}

# Function to start the soap opera playlist
soap_opera_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Soap Opera"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/soap_opera_playlist.m3u
}

# Function to start the cartoon playlist
cartoon_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Cartoon"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/cartoon_playlist.m3u
}

# Function to start the sitcom playlist
sitcom_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Sitcom"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/sitcom_playlist.m3u
}

# Function to start the movie playlist
movie_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Movie"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/movie_playlist.m3u
}

# Function to start the talk show playlist
talk_show_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Talk Show"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/talk_show_playlist.m3u
}

# Function to start the late-night movie playlist
late_night_movie_playlist() {
    check_cvlc_running
    echo "Starting DISPLAY=:0 cvlc with playlist: Late-Night Movie"
    DISPLAY=:0 cvlc --fullscreen --aspect 16:9 --no-video-title-show --loop --random /home/jenny/playlists/late_night_movie_playlist.m3u
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
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 02 ]; then
            movie_playlist            
        elif [ "$current_hour" -ge 02 ] && [ "$current_hour" -lt 03 ]; then
            infomercial_playlist  
        elif [ "$current_hour" -ge 03 ] && [ "$current_hour" -lt 05 ]; then
            late_night_movie_playlist                
        elif [ "$current_hour" -ge 05 ] && [ "$current_hour" -lt 06 ]; then
            off_air_playlist
        fi
        ;;
    Sat)
        if [ "$current_hour" -ge 06 ] && [ "$current_hour" -lt 12 ]; then
            cartoon_playlist
        elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 15 ]; then
            sports_playlist
        elif [ "$current_hour" -ge 15 ] && [ "$current_hour" -lt 18 ]; then
            sitcom_playlist
        elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 19 ]; then
            evening_news_playlist
        elif [ "$current_hour" -ge 19 ] && [ "$current_hour" -lt 20 ]; then
            game_show_playlist
        elif [ "$current_hour" -ge 20 ] && [ "$current_hour" -lt 22 ]; then
            movie_playlist
        elif [ "$current_hour" -ge 22 ] && [ "$current_hour" -lt 23 ]; then
            sitcom_playlist
        elif [ "$current_hour" -ge 23 ] && [ "$current_hour" -lt 24 ]; then
            talk_show_playlist           
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 01 ]; then
            SNL_playlist
        elif [ "$current_hour" -ge 01 ] && [ "$current_hour" -lt 02 ]; then
            infomercial_playlist
        elif [ "$current_hour" -ge 02 ] && [ "$current_hour" -lt 04 ]; then
            late_night_movie_playlist
        elif [ "$current_hour" -ge 04 ] && [ "$current_hour" -lt 05 ]; then
            sitcom_playlist
        elif [ "$current_hour" -ge 05 ] && [ "$current_hour" -lt 06 ]; then
            off_air_playlist
        fi
        ;;
    Sun)
        if [ "$current_hour" -ge 06 ] && [ "$current_hour" -lt 09 ]; then
            morning_news_playlist
        elif [ "$current_hour" -ge 09 ] && [ "$current_hour" -lt 12 ]; then
            talk_show_playlist
        elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 18 ]; then
            sports_playlist
        elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 19 ]; then
            evening_news_playlist            
        elif [ "$current_hour" -ge 19 ] && [ "$current_hour" -lt 20 ]; then
            game_show_playlist
        elif [ "$current_hour" -ge 20 ] && [ "$current_hour" -lt 22 ]; then
            movie_playlist
        elif [ "$current_hour" -ge 22 ] && [ "$current_hour" -lt 23 ]; then
            sitcom_playlist            
        elif [ "$current_hour" -ge 23 ] && [ "$current_hour" -lt 24 ]; then
            talk_show_playlist            
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 02 ]; then
            late_night_movie_playlist
        elif [ "$current_hour" -ge 02 ] && [ "$current_hour" -lt 04 ]; then
            sitcom_playlist
        elif [ "$current_hour" -ge 05 ] && [ "$current_hour" -lt 06 ]; then
            off_air_playlist            
        fi
        ;;
esac
