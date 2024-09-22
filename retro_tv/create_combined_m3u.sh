#!/bin/bash

# Directories for input M3U files and output M3U file
M3U_DIR="/home/jenny/playlists" # Update this to your M3U files directory
OUTPUT_M3U="/home/jenny/playlists/output_playlist.m3u"
XMLTV_ID_PREFIX="1" # The prefix used in your XMLTV for tvg-id

# Start creating the new M3U file
echo "#EXTM3U" > "$OUTPUT_M3U"

# Array of program types and their corresponding M3U files
declare -A PROGRAMMING=(
    ["morning_news"]="morning_news.m3u"
    ["game_shows"]="game_shows.m3u"
    ["soap_operas"]="soap_operas.m3u"
    ["cartoons"]="cartoons.m3u"
    ["evening_news"]="evening_news.m3u"
    ["sitcoms"]="sitcoms.m3u"
    ["movies"]="movies.m3u"
    ["talk_shows"]="talk_shows.m3u"
    ["infomercials"]="infomercials.m3u"
    ["late_night_movie"]="late_night_movie.m3u"
    ["sports"]="sports.m3u"
    ["SNL"]="snl.m3u"
    ["off_air"]="off_air.m3u"
)

# Loop through all program types and add entries to the output M3U
for program in "${!PROGRAMMING[@]}"; do
    # Define M3U file path
    M3U_FILE="$M3U_DIR/${PROGRAMMING[$program]}"
    
    # Check if the M3U file exists
    if [[ -f "$M3U_FILE" ]]; then
        # Read the M3U file and append to the output M3U with the correct tvg-id and name
        while IFS= read -r line; do
            if [[ $line == \#EXTINF* ]]; then
                # Add tvg-id and tvg-name based on the program
                echo "$line tvg-id=\"$XMLTV_ID_PREFIX$program\" tvg-name=\"$program\"" >> "$OUTPUT_M3U"
            else
                # Add the URL or stream link
                echo "$line" >> "$OUTPUT_M3U"
            fi
        done < "$M3U_FILE"
    else
        echo "Warning: M3U file for '$program' not found!"
    fi
done

echo "M3U playlist generated at $OUTPUT_M3U."
