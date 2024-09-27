#!/usr/bin/env bash

# Function to start the off-air playlist
off_air_playlist() {
    echo "Off-air period..."
    echo "Starting DISPLAY=:0 vlc with playlist: Off-Air"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/Other/off_air.m3u
}

# Function to start the morning news playlist
morning_news_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Morning News"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/News/morning_news.m3u
}

# Function to start the evening news playlist
evening_news_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Evening News"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/News/evening_news.m3u
}

# Function to start the infomercial playlist
infomercials_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Infomercials"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/Other/infomercials.m3u
}

# Function to start the morning news playlist
snl_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: SNL"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/TV/snl.m3u
}

# Function to start the game show playlist
game_shows_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Game Shows"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/TV/game_shows.m3u
}

# Function to start the soap opera playlist
soap_operas_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Soap Operas"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/TV/soap_operas.m3u
}

# Function to start the cartoon playlist
cartoons_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Cartoons"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/TV/cartoons.m3u
}

# Function to start the cartoon playlist
sports_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Sports"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/Other/sports.m3u
}

# Function to start the sitcom playlist
sitcoms_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Sitcoms"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/TV/sitcoms.m3u
}

# Function to start the movie playlist
saturday_night_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Saturday Night"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/Movies/saturday_night.m3u
}

# Function to start the talk show playlist
talk_shows_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Talk Shows"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/TV/talk_shows.m3u
}

# Function to start the late-night movie playlist
horror_night_playlist() {
    echo "Starting DISPLAY=:0 vlc with playlist: Horror Night"
    DISPLAY=:0 vlc --fullscreen --aspect 16:9 --no-video-title-show --random /home/jenny/retro_tv/programming/Movies/horror_night.m3u
}

# Get the current day and hour
current_day=$(date +'%a') # Mon, Tue, Wed, Thu, Fri, Sat, Sun
current_hour=$(date +'%H')

# Determine which playlist to start based on the current time and day
case "$current_day" in
    Mon|Tue|Wed|Thu|Fri)
        if [ "$current_hour" -ge 06 ] && [ "$current_hour" -lt 09 ]; then
            morning_news_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 09 ] && [ "$current_hour" -lt 12 ]; then
            game_shows_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 15 ]; then
            soap_operas_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 15 ] && [ "$current_hour" -lt 18 ]; then
            cartoons_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 20 ]; then
            evening_news_playlist & sleep 2h && pkill vlc
        elif [ "$current_hour" -ge 20 ] && [ "$current_hour" -lt 21 ]; then
            sitcoms_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 21 ] && [ "$current_hour" -lt 23 ]; then
            saturday_night_playlist & sleep 2h && pkill vlc
        elif [ "$current_hour" -ge 23 ] && [ "$current_hour" -lt 24 ]; then
            talk_shows_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 02 ]; then
            saturday_night_playlist  & sleep 2h && pkill vlc
        elif [ "$current_hour" -ge 02 ] && [ "$current_hour" -lt 03 ]; then
            infomercials_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 03 ] && [ "$current_hour" -lt 05 ]; then
            horror_night_playlist & sleep 2h && pkill vlc
        elif [ "$current_hour" -ge 05 ] && [ "$current_hour" -lt 06 ]; then
            off_air_playlist & sleep 60m && pkill vlc
        fi
        ;;
    Sat)
        if [ "$current_hour" -ge 06 ] && [ "$current_hour" -lt 12 ]; then
            cartoons_playlist & sleep 6h && pkill vlc
        elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 15 ]; then
            sports_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 15 ] && [ "$current_hour" -lt 18 ]; then
            sitcoms_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 19 ]; then
            evening_news_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 19 ] && [ "$current_hour" -lt 20 ]; then
            game_shows_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 20 ] && [ "$current_hour" -lt 22 ]; then
            saturday_night_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 22 ] && [ "$current_hour" -lt 23 ]; then
            sitcoms_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 23 ] && [ "$current_hour" -lt 24 ]; then
            talk_shows_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 01 ]; then
            snl_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 01 ] && [ "$current_hour" -lt 02 ]; then
            infomercials_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 02 ] && [ "$current_hour" -lt 04 ]; then
            horror_night_playlist & sleep 2h && pkill vlc
        elif [ "$current_hour" -ge 04 ] && [ "$current_hour" -lt 05 ]; then
            sitcoms_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 05 ] && [ "$current_hour" -lt 06 ]; then
            off_air_playlist & sleep 60m && pkill vlc
        fi
        ;;
    Sun)
        if [ "$current_hour" -ge 06 ] && [ "$current_hour" -lt 09 ]; then
            morning_news_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 09 ] && [ "$current_hour" -lt 12 ]; then
            talk_shows_playlist & sleep 3h && pkill vlc
        elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 18 ]; then
            sports_playlist & sleep 6h && pkill vlc
        elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 19 ]; then
            evening_news_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 19 ] && [ "$current_hour" -lt 20 ]; then
            game_shows_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 20 ] && [ "$current_hour" -lt 22 ]; then
            saturday_night_playlist & sleep 2h && pkill vlc
        elif [ "$current_hour" -ge 22 ] && [ "$current_hour" -lt 23 ]; then
            sitcoms_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 23 ] && [ "$current_hour" -lt 24 ]; then
            talk_shows_playlist & sleep 60m && pkill vlc
        elif [ "$current_hour" -ge 00 ] && [ "$current_hour" -lt 02 ]; then
            horror_night_playlist & sleep 2h && pkill vlc
        elif [ "$current_hour" -ge 02 ] && [ "$current_hour" -lt 04 ]; then
            sitcoms_playlist & sleep 2h && pkill vlc
        elif [ "$current_hour" -ge 05 ] && [ "$current_hour" -lt 06 ]; then
            off_air_playlist & sleep 60m && pkill vlc
        fi
        ;;
esac
