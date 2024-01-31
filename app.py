from datetime import datetime
import pytz

def world_clock():
    # List of timezones you want to display
    timezones = ['UTC', 'America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']

    # Current time in UTC
    utc_now = datetime.now(pytz.utc)

    # Print time for each timezone
    for tz in timezones:
        timezone = pytz.timezone(tz)
        local_time = utc_now.astimezone(timezone)
        print(f"Time in {tz}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    world_clock()
