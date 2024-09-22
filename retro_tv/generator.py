import os
import random
from moviepy.video.io.VideoFileClip import VideoFileClip

# Define your programming blocks
PROGRAMMING = {
    "morning_news": "morning_news.m3u",
    "game_shows": "game_shows.m3u",
    "soap_operas": "soap_operas.m3u",
    "cartoons": "cartoons.m3u",
    "evening_news": "evening_news.m3u",
    "sitcoms": "sitcoms.m3u",
    "movies": "movies.m3u",
    "talk_shows": "talk_shows.m3u",
    "infomercials": "infomercials.m3u",
    "late_night_movie": "late_night_movie.m3u",
    "sports": "sports.m3u",
    "SNL": "snl.m3u",
    "off_air": "off_air.m3u",
}

# Function to get video length
def get_video_length(video_path):
    try:
        with VideoFileClip(video_path) as video:
            return video.duration
    except Exception as e:
        print(f"Error getting length for {video_path}: {e}")
        return 0

# Function to read M3U file and return video paths
def read_m3u(m3u_file):
    with open(m3u_file, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith('#')]

# Function to determine the programming block based on the current time
def determine_programming_block(current_hour, current_day):
    if current_day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
        if 6 <= current_hour < 9:
            return "morning_news"
        elif 9 <= current_hour < 12:
            return "game_shows"
        elif 12 <= current_hour < 15:
            return "soap_operas"
        elif 15 <= current_hour < 18:
            return "cartoons"
        elif 18 <= current_hour < 20:
            return "evening_news"
        elif 20 <= current_hour < 21:
            return "sitcoms"
        elif 21 <= current_hour < 23:
            return "movies"
        elif 23 <= current_hour < 24 or 0 <= current_hour < 2:
            return "talk_shows"
        elif 2 <= current_hour < 3:
            return "infomercials"
        elif 3 <= current_hour < 5:
            return "late_night_movie"
        elif 5 <= current_hour < 6:
            return "off_air"
    elif current_day == "Sat":
        if 6 <= current_hour < 12:
            return "cartoons"
        elif 12 <= current_hour < 15:
            return "sports"
        elif 15 <= current_hour < 18:
            return "sitcoms"
        elif 18 <= current_hour < 19:
            return "evening_news"
        elif 19 <= current_hour < 20:
            return "game_shows"
        elif 20 <= current_hour < 22:
            return "movies"
        elif 22 <= current_hour < 23:
            return "sitcoms"
        elif 23 <= current_hour < 24 or 0 <= current_hour < 1:
            return "talk_shows"
        elif 1 <= current_hour < 2:
            return "infomercials"
        elif 2 <= current_hour < 4:
            return "late_night_movie"
        elif 4 <= current_hour < 5:
            return "sitcoms"
        elif 5 <= current_hour < 6:
            return "off_air"
    elif current_day == "Sun":
        if 6 <= current_hour < 9:
            return "morning_news"
        elif 9 <= current_hour < 12:
            return "talk_shows"
        elif 12 <= current_hour < 18:
            return "sports"
        elif 18 <= current_hour < 19:
            return "evening_news"
        elif 19 <= current_hour < 20:
            return "game_shows"
        elif 20 <= current_hour < 22:
            return "movies"
        elif 22 <= current_hour < 23:
            return "sitcoms"
        elif 23 <= current_hour < 24 or 0 <= current_hour < 2:
            return "talk_shows"
        elif 2 <= current_hour < 4:
            return "late_night_movie"
        elif 4 <= current_hour < 6:
            return "sitcoms"
        elif 5 <= current_hour < 6:
            return "off_air"

    return None

# Function to generate weekly programming
def generate_weekly_m3u():
    weekly_playlist = []
    current_day = os.popen('date +%a').read().strip()  # Get current day
    current_hour = int(os.popen('date +%H').read().strip())  # Get current hour

    # Determine the programming block for the current time
    programming_block = determine_programming_block(current_hour, current_day)
    
    if programming_block:
        m3u_file = PROGRAMMING[programming_block]
        videos = read_m3u(m3u_file)
        block_length = 60 * 60  # Example: set block length to 1 hour (3600 seconds)
        block_videos = []

        # Gather enough videos for this block
        while sum(get_video_length(v) for v in block_videos) < block_length:
            selected_video = random.choice(videos)
            block_videos.append(selected_video)

        weekly_playlist.extend(block_videos)
    
    # Write the new M3U file
    output_file = 'weekly_programming.m3u'
    with open(output_file, 'w') as file:
        for video in weekly_playlist:
            file.write(f"{video}\n")
    
    print(f"Generated weekly programming M3U file: {output_file}")

# Example usage
generate_weekly_m3u()
