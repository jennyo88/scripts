# source ~/my_python_envs/moviepy_env/bin/activate
import os
import random
import datetime
from moviepy.editor import VideoFileClip

def read_m3u(m3u_file):
    if not os.path.exists(m3u_file):
        print(f"File not found: {m3u_file}")
        return []
    with open(m3u_file, 'r') as file:
        return [line.strip() for line in file if not line.startswith('#')]

def get_video_length(video_path):
    try:
        with VideoFileClip(video_path) as video:
            return int(video.duration)  # Return length in seconds
    except Exception as e:
        print(f"Error getting length of {video_path}: {e}")
        return 0  # Return 0 if there's an error

def generate_weekly_m3u():
    # Define the programming schedule based on your specifications
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
        # Continue with the rest of the days...
    }

    today = datetime.datetime.now()
    current_day = today.strftime('%a')

    # Get today's schedule
    schedule = programming_schedule.get(current_day)

    def fill_time_block(m3u_file, duration_required):
    videos = read_m3u(m3u_file)
    selected_videos = []
    total_duration = 0

    while total_duration < duration_required and videos:
        video = random.choice(videos)
        video_length = get_video_length(video)

        if video_length + total_duration <= duration_required:
            selected_videos.append(video)
            total_duration += video_length
        else:
            # Even if the video exceeds, you might want to still include it
            # to match your rule of going slightly over the time limit
            selected_videos.append(video)
            total_duration += video_length
            break

    return selected_videos, total_duration


    output_m3u = "#EXTM3U\n"

    for m3u_file, title, category, block_length in schedule:
        video_files = read_m3u(m3u_file)
        selected_videos = []
        
        total_length = 0
        
        while total_length < block_length * 60:  # Convert block length from minutes to seconds
            if not video_files:  # Check if there are no video files
                print(f"No videos found in {m3u_file}")
                break
            video = random.choice(video_files)
            video_length = get_video_length(video)
            if total_length + video_length <= block_length * 60:
                selected_videos.append(video)
                total_length += video_length

        for video in selected_videos:
            output_m3u += f"#EXTINF:-1,{title}\n{video}\n"

    # Write the output M3U file
    with open("weekly_programming.m3u", 'w') as f:
        f.write(output_m3u)

# Call the function to generate the M3U
generate_weekly_m3u()
