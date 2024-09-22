from datetime import datetime, timedelta

# Define the weekly schedule with block names and durations
schedule = {
    "Monday": [
        ("Morning News", "06:00", "09:00"),
        ("Game Shows", "09:00", "12:00"),
        ("Soap Operas", "12:00", "15:00"),
        ("Cartoons", "15:00", "18:00"),
        ("Evening News", "18:00", "20:00"),
        ("Sitcoms", "20:00", "21:00"),
        ("Movies", "21:00", "23:00"),
        ("Talk Shows", "23:00", "24:00"),
        ("Late Night Movie", "00:00", "02:00"),
        ("Infomercial", "02:00", "03:00"),
        ("Late Night Movie", "03:00", "05:00"),
        ("Off-Air", "05:00", "06:00"),
    ],
    "Tuesday": [
        ("Morning News", "06:00", "09:00"),
        ("Game Shows", "09:00", "12:00"),
        ("Soap Operas", "12:00", "15:00"),
        ("Cartoons", "15:00", "18:00"),
        ("Evening News", "18:00", "20:00"),
        ("Sitcoms", "20:00", "21:00"),
        ("Movies", "21:00", "23:00"),
        ("Talk Shows", "23:00", "24:00"),
        ("Late Night Movie", "00:00", "02:00"),
        ("Infomercial", "02:00", "03:00"),
        ("Late Night Movie", "03:00", "05:00"),
        ("Off-Air", "05:00", "06:00"),
    ],
    "Wednesday": [
        ("Morning News", "06:00", "09:00"),
        ("Game Shows", "09:00", "12:00"),
        ("Soap Operas", "12:00", "15:00"),
        ("Cartoons", "15:00", "18:00"),
        ("Evening News", "18:00", "20:00"),
        ("Sitcoms", "20:00", "21:00"),
        ("Movies", "21:00", "23:00"),
        ("Talk Shows", "23:00", "24:00"),
        ("Late Night Movie", "00:00", "02:00"),
        ("Infomercial", "02:00", "03:00"),
        ("Late Night Movie", "03:00", "05:00"),
        ("Off-Air", "05:00", "06:00"),
    ],
    "Thursday": [
        ("Morning News", "06:00", "09:00"),
        ("Game Shows", "09:00", "12:00"),
        ("Soap Operas", "12:00", "15:00"),
        ("Cartoons", "15:00", "18:00"),
        ("Evening News", "18:00", "20:00"),
        ("Sitcoms", "20:00", "21:00"),
        ("Movies", "21:00", "23:00"),
        ("Talk Shows", "23:00", "24:00"),
        ("Late Night Movie", "00:00", "02:00"),
        ("Infomercial", "02:00", "03:00"),
        ("Late Night Movie", "03:00", "05:00"),
        ("Off-Air", "05:00", "06:00"),
    ],
    "Friday": [
        ("Morning News", "06:00", "09:00"),
        ("Game Shows", "09:00", "12:00"),
        ("Soap Operas", "12:00", "15:00"),
        ("Cartoons", "15:00", "18:00"),
        ("Evening News", "18:00", "20:00"),
        ("Sitcoms", "20:00", "21:00"),
        ("Movies", "21:00", "23:00"),
        ("Talk Shows", "23:00", "24:00"),
        ("Late Night Movie", "00:00", "02:00"),
        ("Infomercial", "02:00", "03:00"),
        ("Late Night Movie", "03:00", "05:00"),
        ("Off-Air", "05:00", "06:00"),
    ],
    "Saturday": [
        ("Cartoons", "06:00", "12:00"),
        ("Sports", "12:00", "15:00"),
        ("Sitcoms", "15:00", "18:00"),
        ("Evening News", "18:00", "19:00"),
        ("Game Shows", "19:00", "20:00"),
        ("Movies", "20:00", "22:00"),
        ("Sitcoms", "22:00", "23:00"),
        ("Talk Shows", "23:00", "24:00"),
        ("Variety", "00:00", "01:00"),
        ("Infomercial", "01:00", "02:00"),
        ("Late Night Movie", "02:00", "04:00"),
        ("Sitcoms", "04:00", "05:00"),
        ("Off-Air", "05:00", "06:00"),
    ],
    "Sunday": [
        ("Morning News", "06:00", "09:00"),
        ("Talk Shows", "09:00", "12:00"),
        ("Sports", "12:00", "18:00"),
        ("Evening News", "18:00", "19:00"),
        ("Game Shows", "19:00", "20:00"),
        ("Movies", "20:00", "22:00"),
        ("Sitcoms", "22:00", "23:00"),
        ("Talk Shows", "23:00", "24:00"),
        ("Late Night Movie", "00:00", "02:00"),
        ("Sitcoms", "02:00", "05:00"),
        ("Off-Air", "05:00", "06:00"),
    ],
    # Continue with the rest of the days...
    # ... (similar format)
}

# Timezone offset (PST is UTC -8)
timezone_offset = "-0800"

def create_programme_xml(title, start_time, end_time, channel="1", desc=""):
    """Generate the <programme> tag for XMLTV."""
    start_str = start_time.strftime("%Y%m%d%H%M%S") + " " + timezone_offset
    end_str = end_time.strftime("%Y%m%d%H%M%S") + " " + timezone_offset
    
    programme_xml = f"""
    <programme start="{start_str}" stop="{end_str}" channel="{channel}">
        <title>{title}</title>
        <desc>{desc}</desc>
    </programme>
    """
    return programme_xml.strip()

def generate_xmltv(schedule, start_date):
    """Generate the XMLTV file content for a given schedule starting from a start_date."""
    xmltv_content = """<?xml version="1.0" encoding="UTF-8"?>
    <tv>
        <channel id="1">
            <display-name>Channel 1</display-name>
        </channel>
    """
    
    current_date = start_date
    for day, blocks in schedule.items():
        for block in blocks:
            title, start_time_str, end_time_str = block
            
            # Parse start and end times for each block
            start_time = datetime.strptime(f"{current_date} {start_time_str}", "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(f"{current_date} {end_time_str}", "%Y-%m-%d %H:%M")
            
            # Generate programme XML
            desc = f"{title} block from {start_time_str} to {end_time_str}."
            programme_xml = create_programme_xml(title, start_time, end_time, desc=desc)
            xmltv_content += programme_xml + "\n"
        
        # Move to the next day
        current_date = (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    
    # Close the XML file
    xmltv_content += "</tv>"
    
    return xmltv_content

# Example usage
start_date = "2024-09-22"  # Set the start date of the week (Sunday)
xmltv_output = generate_xmltv(schedule, start_date)

# Write to file
with open("tv_schedule.xml", "w") as f:
    f.write(xmltv_output)

print("XMLTV file generated as 'tv_schedule.xml'")
