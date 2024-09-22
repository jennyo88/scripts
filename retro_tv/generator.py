import os
import random
from datetime import datetime, timedelta

# Define the path to your playlists
playlists_directory = "/home/jenny/playlists"

# Define the programming schedule based on your specifications
programming_schedule = {
    "Mon": [
        ("morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Tue": [
        ("morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Wed": [
        ("morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Thu": [
        ("morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Fri": [
        ("morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("game_shows.m3u", "Game Shows", "Game Show", 180),  # 9:00 - 12:00
        ("soap_operas.m3u", "Soap Operas", "Drama", 180),     # 12:00 - 15:00
        ("cartoons.m3u", "Cartoons", "Children", 180),        # 15:00 - 18:00
        ("evening_news.m3u", "Evening News", "News", 120),   # 18:00 - 20:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 60),              # 20:00 - 21:00
        ("movies.m3u", "Movies", "Movie", 120),               # 21:00 - 23:00
        ("talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("infomercials.m3u", "Infomercial", "Infomercial", 60),  # 02:00 - 03:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 03:00 - 05:00
        ("off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Sat": [
        ("cartoons.m3u", "Cartoons", "Children", 360),  # 6:00 - 12:00
        ("sports.m3u", "Sports", "Sports", 180),     # 12:00 - 15:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 180),        # 15:00 - 18:00
        ("evening_news.m3u", "Evening News", "News", 60),   # 18:00 - 19:00
        ("game_shows.m3u", "Game Shows", "Game Show", 60),   # 19:00 - 20:00
        ("movies.m3u", "Movies", "Movie", 120),               # 20:00 - 22:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 60),   # 22:00 - 23:00
        ("talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("SNL.m3u", "Variety", "Comedy", 60),  # 00:00 - 01:00
        ("infomercials.m3u", "Infomercial", "Infomercial", 60),  # 01:00 - 02:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 02:00 - 04:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 60),  # 04:00 - 05:00
        ("off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    "Sun": [
        ("morning_news.m3u", "Morning News", "News", 180),  # 6:00 - 9:00
        ("talk_shows.m3u", "Talk Shows", "Talk Show", 180),  # 9:00 - 12:00
        ("sports.m3u", "Sports", "Sports", 360),     # 12:00 - 18:00
        ("evening_news.m3u", "Evening News", "News", 60),   # 18:00 - 19:00
        ("game_shows.m3u", "Game Shows", "Game Show", 60),   # 19:00 - 20:00
        ("movies.m3u", "Movies", "Movie", 120),               # 20:00 - 22:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 60),   # 22:00 - 23:00
        ("talk_shows.m3u", "Talk Shows", "Talk Show", 60),   # 23:00 - 24:00
        ("late_night_movie.m3u", "Late Night Movie", "Movie", 120),  # 00:00 - 02:00
        ("sitcoms.m3u", "Sitcoms", "Comedy", 120),  # 02:00 - 04:00
        ("off_air.m3u", "Off-Air", "Off-Air", 60)             # 05:00 - 06:00
    ],
    # Continue with the rest of the days
}

def read_m3u(file_path):
    """Read an M3U file and return a list of video file paths."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_videos_for_block(playlist_name, block_length):
    """Get random videos for a given block length from the corresponding playlist."""
    file_path = os.path.join(playlists_directory, playlist_name)
    videos = read_m3u(file_path)
    selected_videos = []
    total_length = 0

    while total_length < block_length:
        video = random.choice(videos)
        video_length = get_video_length(video)  # Implement your own logic to get the video length
        if total_length + video_length <= block_length:
            selected_videos.append(video)
            total_length += video_length

    return selected_videos

def generate_m3u_for_day(day):
    """Generate an M3U playlist for a specific day based on the programming schedule."""
    m3u_content = []
    start_time = datetime.now().replace(hour=6, minute=0, second=0, microsecond=0)  # Starting at 6 AM
    for entry in programming_schedule[day]:
        playlist_file, title, category, block_length = entry
        videos = get_videos_for_block(playlist_file, block_length)
        for video in videos:
            start_time_str = start_time.strftime('%Y%m%d%H%M%S +0000')
            end_time = start_time + timedelta(seconds=block_length)
            end_time_str = end_time.strftime('%Y%m%d%H%M%S +0000')

            m3u_content.append(f"#EXTINF:-1, {title} ({category})")
            m3u_content.append(video)
            start_time = end_time

    return m3u_content

def write_m3u_file(day):
    """Write the generated M3U content to a file for the specified day."""
    m3u_content = generate_m3u_for_day(day)
    m3u_file_path = os.path.join(playlists_directory, f"{day.lower()}_program.m3u")
    with open(m3u_file_path, 'w') as m3u_file:
        m3u_file.write("#EXTM3U\n")
        m3u_file.write("\n".join(m3u_content))

def main():
    for day in programming_schedule.keys():
        write_m3u_file(day)

if __name__ == "__main__":
    main()
