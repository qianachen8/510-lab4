import streamlit as st
from datetime import datetime
import pytz

# List of time zones with different cities
timezones = {
    'Brasilia': 'America/Sao_Paulo',
    'Istanbul': 'Europe/Istanbul',
    'Cape Town': 'Africa/Johannesburg',
    'Moscow': 'Europe/Moscow',
    'Beijing': 'Asia/Shanghai',
    'New Delhi': 'Asia/Kolkata',
    'Sydney': 'Australia/Sydney',
    'Tokyo': 'Asia/Tokyo',
    'London': 'Europe/London',
    'New York': 'America/New_York',
    'Bangkok': 'Asia/Bangkok',
    'Nairobi': 'Africa/Nairobi',
    'Buenos Aires': 'America/Argentina/Buenos_Aires',
    'Toronto': 'America/Toronto',
    'Madrid': 'Europe/Madrid',
    'Rome': 'Europe/Rome',
    'Lagos': 'Africa/Lagos',
    'Jakarta': 'Asia/Jakarta',
    'Dublin': 'Europe/Dublin',
    'Zurich': 'Europe/Zurich',
    # Add more time zones as needed
}

# Function to get the current time in a time zone
def get_time_in_timezone(timezone):
    tz = pytz.timezone(timezone)
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

# New function to display the current UNIX timestamp
def show_unix_timestamp():
    st.write("Current UNIX Timestamp:", int(datetime.now().timestamp()))

# New function to convert UNIX timestamp to human-readable time
def unix_to_human():
    st.title("UNIX Timestamp Converter")
    unix_input = st.number_input("Enter UNIX Timestamp:", step=1)
    if unix_input:
        human_time = datetime.fromtimestamp(unix_input).strftime('%Y-%m-%d %H:%M:%S')
        st.write("Human-readable Time:", human_time)

# Main function
def world_clock_app():
    st.title('World Clock')

    # Define your default selections, ensuring they exist in the timezones
    default_selections = ['New York', 'London']  # Example defaults

    # Ensure default selections are in the available options
    validated_defaults = [tz for tz in default_selections if tz in timezones.keys()]

    # Dropdown menu for selecting up to 4 locations
    selected_timezones = st.multiselect(
        'Select up to 4 locations:', list(timezones.keys()), default=validated_defaults
    )

    if len(selected_timezones) > 4:
        st.error('You can select up to 4 locations.')
        st.stop()

    # Display the current time in each selected location
    for city in selected_timezones:
        st.write(f"Time in {city}: {get_time_in_timezone(timezones[city])}")

    # Update the time every second
    st.button('Refresh Time')

    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page:", ["World Clock", "UNIX Converter"], key='page_select')
    
    if page == "World Clock":
        st.title('World Clock')
        # Your code to display the world clock should be here
        # For example, the multiselect widget and time display loop
        show_unix_timestamp()  # Displays the UNIX timestamp

    elif page == "UNIX Converter":
        unix_to_human()  # Handles UNIX timestamp conversion

# Run the app
if __name__ == "__main__":
    world_clock_app()
