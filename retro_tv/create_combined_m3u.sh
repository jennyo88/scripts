#!/bin/bash

# Directories
m3u_dir="/home/jenny/playlists"
xmltv_file="/home/jenny/xmltv.xml"  # Update this with the path to your XMLTV file
output_playlist="$m3u_dir/combined_playlist.m3u"

# Initialize the output playlist
echo "#EXTM3U" > "$output_playlist"

# Function to get the total duration of a video file
get_video_duration() {
    ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1"
}

# Read the XMLTV file
while IFS= read -r line; do
    # Extract channel ID, title, and duration from the XMLTV file
    title=$(echo "$line" | grep -oP '<title>\K[^<]+')
    duration_start=$(echo "$line" | grep -oP 'start="\K[^"]+')
    duration_end=$(echo "$line" | grep -oP 'stop="\K[^"]+')
    
    # Calculate total duration in seconds
    start_time=$(date -d "${duration_start:0:8} ${duration_start:8:2}:${duration_start:10:2}:${duration_start:12:2}" +%s)
    end_time=$(date -d "${duration_end:0:8} ${duration_end:8:2}:${duration_end:10:2}:${duration_end:12:2}" +%s)
    total_duration=$((end_time - start_time))

    # Map titles to their respective playlist files
    case "$title" in
        "Morning News") playlist_file="$m3u_dir/morning_news.m3u" ;;
        "Game Shows") playlist_file="$m3u_dir/game_shows.m3u" ;;
        "Soap Operas") playlist_file="$m3u_dir/soap_operas.m3u" ;;
        "Cartoons") playlist_file="$m3u_dir/cartoons.m3u" ;;
        "Evening News") playlist_file="$m3u_dir/evening_news.m3u" ;;
        "Sitcoms") playlist_file="$m3u_dir/sitcoms.m3u" ;;
        "Movies") playlist_file="$m3u_dir/movies.m3u" ;;
        "Talk Shows") playlist_file="$m3u_dir/talk_shows.m3u" ;;
        "Late Night Movie") playlist_file="$m3u_dir/late_night_movie.m3u" ;;
        "Infomercial") playlist_file="$m3u_dir/infomercials.m3u" ;;
        "Sports") playlist_file="$m3u_dir/sports.m3u" ;;
        "SNL") playlist_file="$m3u_dir/snl.m3u" ;;
        "Off-Air") playlist_file="$m3u_dir/off_air.m3u" ;;
        *) playlist_file="" ;;
    esac

    # Append contents of the selected playlist to the output playlist
    if [[ -f "$playlist_file" ]]; then
        total_played_duration=0
        while IFS= read -r m3u_line; do
            if [[ "$m3u_line" == "#EXTINF:"* ]]; then
                echo "$m3u_line" >> "$output_playlist"
                read -r m3u_url

                # Check the duration of the video file
                video_length=$(get_video_duration "$m3u_url")

                # Add to the total played duration
                total_played_duration=$(echo "$total_played_duration + $video_length" | bc)

                echo "$m3u_url" >> "$output_playlist"

                # Check if we've reached or exceeded the required duration
                if (( $(echo "$total_played_duration >= $total_duration" | bc -l) )); then
                    break
                fi
            fi
        done < "$playlist_file"
    fi

    # If we exceeded the required duration, output a message
    if (( $(echo "$total_played_duration > $total_duration" | bc -l) )); then
        echo "Total duration exceeded for $title (expected ${total_duration}s, found ${total_played_duration}s)"
    fi

done < <(xmllint --xpath '//programme' "$xmltv_file")

echo "Combined playlist created at $output_playlist"
