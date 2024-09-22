import os
import random
import datetime
from moviepy.editor import VideoFileClip

# Define your programming schedule here
programming_schedule = {
    "Mon": [
        ("/home/jenny/playlists/morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("/home/jenny/playlists/game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("/home/jenny/playlists/soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("/home/jenny/playlists/cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("/home/jenny/playlists/evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("/home/jenny/playlists/movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("/home/jenny/playlists/talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("/home/jenny/playlists/infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("/home/jenny/playlists/off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Tue": [
        ("/home/jenny/playlists/morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("/home/jenny/playlists/game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("/home/jenny/playlists/soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("/home/jenny/playlists/cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("/home/jenny/playlists/evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("/home/jenny/playlists/movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("/home/jenny/playlists/talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("/home/jenny/playlists/infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("/home/jenny/playlists/off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Wed": [
        ("/home/jenny/playlists/morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("/home/jenny/playlists/game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("/home/jenny/playlists/soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("/home/jenny/playlists/cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("/home/jenny/playlists/evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("/home/jenny/playlists/movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("/home/jenny/playlists/talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("/home/jenny/playlists/infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("/home/jenny/playlists/off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Thu": [
        ("/home/jenny/playlists/morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("/home/jenny/playlists/game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("/home/jenny/playlists/soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("/home/jenny/playlists/cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("/home/jenny/playlists/evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("/home/jenny/playlists/movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("/home/jenny/playlists/talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("/home/jenny/playlists/infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("/home/jenny/playlists/off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Fri": [
        ("/home/jenny/playlists/morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("/home/jenny/playlists/game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("/home/jenny/playlists/soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("/home/jenny/playlists/cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("/home/jenny/playlists/evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("/home/jenny/playlists/movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("/home/jenny/playlists/talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("/home/jenny/playlists/infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("/home/jenny/playlists/off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Sat": [
        ("/home/jenny/playlists/cartoons.m3u", "Cartoons", "Children", 360),  # 6:00 - 12:00
        ("/home/jenny/playlists/sports.m3u", "Sports", "Sports", 180),     # 12:00 - 15:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 180),        # 15:00 - 18:00
        ("/home/jenny/playlists/evening_news.m3u", "Evening News", "News", 60),   # 18:00 - 19:00
        ("/home/jenny/playlists/game_shows.m3u", "Game Shows", "Game Show", 60),   # 19:00 - 20:00
        ("/home/jenny/playlists/movies.m3u", "Movies", "Movie", 120),               # 20:00 - 22:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 60),   # 22:00 - 23:00
        ("/home/jenny/playlists/talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("/home/jenny/playlists/SNL.m3u", "Variety", "Comedy", 60),  # 00:00 - 01:00
        ("/home/jenny/playlists/infomercials.m3u", "Infomercial", "Infomercial", 60),  # 01:00 - 02:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 02:00 - 04:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 60),  # 04:00 - 05:00
        ("/home/jenny/playlists/off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Sun": [
        ("/home/jenny/playlists/morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("/home/jenny/playlists/talk_shows.m3u", "Talk Shows", "Talk Show", 180),  # 9:00 - 12:00
        ("/home/jenny/playlists/sports.m3u", "Sports", "Sports", 360),     # 12:00 - 18:00
        ("/home/jenny/playlists/evening_news.m3u", "Evening News", "News", 60),   # 18:00 - 19:00
        ("/home/jenny/playlists/game_shows.m3u", "Game Shows", "Game Show", 60),   # 19:00 - 20:00
        ("/home/jenny/playlists/movies.m3u", "Movies", "Movie", 120),               # 20:00 - 22:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 60),   # 22:00 - 23:00
        ("/home/jenny/playlists/talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("/home/jenny/playlists/late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("/home/jenny/playlists/sitcoms.m3u", "Sitcoms", "Comedy", 120),  # 02:00 - 04:00
        ("/home/jenny/playlists/off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    # Add similar blocks for other days (Tue, Wed, etc.)
}

# Helper functions for filling time blocks, loading video files, etc.
def load_m3u_playlist(file_path):
    """Load and return the list of video files from the M3U playlist."""
    with open(file_path, 'r') as file:
        videos = [line.strip() for line in file if line.strip() and not line.startswith("#")]
    return videos

def get_video_duration(video_file):
    """Return the duration of a video file in seconds."""
    clip = VideoFileClip(video_file)
    return clip.duration

# Function to fill the block with videos from the playlist to match the required duration
def fill_time_block(playlist_path, required_duration_minutes):
    videos = load_m3u_playlist(playlist_path)
    random.shuffle(videos)  # Shuffle videos for variety
    selected_videos = []
    total_duration = 0
    required_duration_seconds = required_duration_minutes * 60
    
    while total_duration < required_duration_seconds:
        for video in videos:
            video_duration = get_video_duration(video)
            if total_duration + video_duration <= required_duration_seconds:
                selected_videos.append(video)
                total_duration += video_duration
            else:
                break
    
    return selected_videos

# Function for creating the full weekly playlist based on the schedule
def create_weekly_schedule(programming_schedule):
    for day, blocks in programming_schedule.items():
        print(f"Creating schedule for {day}")
        for block in blocks:
            playlist_path, block_name, block_type, block_duration = block
            print(f"Filling block: {block_name} ({block_type}) for {block_duration} minutes")
            selected_videos = fill_time_block(playlist_path, block_duration)
            # Add logic to write selected_videos to output M3U file

# Call the function to create the weekly schedule
create_weekly_schedule(programming_schedule)
