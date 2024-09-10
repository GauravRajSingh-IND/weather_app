import os
from datetime import datetime

import pytz
import dotenv
import requests
import geocoder

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


dotenv.load_dotenv()

def get_location(address: str= None) -> tuple:
    """
    Get the geographical coordinates (latitude and longitude) for a given address.
    If no address is provided, it retrieves the coordinates based on the user's IP address.

    Args:address (str): The address to geocode.
    Returns: tuple: A tuple containing latitude and longitude.
    """

    # Initialize the Nominatim geocoder.
    loc = Nominatim(user_agent="GetLoc")

    try:
        if address:
            # Attempt to geocode the provided address
            geo_loc = loc.geocode(address)
            if geo_loc:
                return geo_loc.latitude, geo_loc.longitude
            else:
                raise ValueError("Address not found.")
        else:
            # Retrieve geographical information based on IP
            geo_loc = geocoder.ip('me').geojson
            if geo_loc and geo_loc['features']:
                latitude = geo_loc['features'][0]['properties']['lat']
                longitude = geo_loc['features'][0]['properties']['lng']
                return latitude, longitude
            else:
                raise ValueError("Could not retrieve location from IP.")

    except Exception as e:
        print(f"Error occurred: {e}")
        return 26.9196, 75.7878

#TODO: get weather data using location of the user
def get_weather(latitude: float, longitude: float, mode: str="json", units: str="metric", lang: str="en") -> dict:
    """
    Get the weather data of a given (latitude and longitude) address.
    :param latitude: latitude of the location
    :param longitude: longitude of the location
    :param mode: output format, default is json format
    :param units: output temperature units, default is metric, i.e. Celsius.
    :param lang: language of output, default is english
    :return:
    """

    # prepare the parameters for the api request.
    params = {
        'lat':latitude,
        'lon':longitude,
        'appid': os.getenv('weather_api_key'),
        'mode':mode,
        'units':units,
        'lang':lang
            }

    # Handle the API endpoint retrieval
    endpoint = os.getenv('weather_end_point')
    if not endpoint:
        raise ValueError("Weather API endpoint is not set in environment variables.")

    try:
        # Call the API
        response = requests.get(url=endpoint, params=params)
        response.raise_for_status()  # Raise an error for bad responses

        # Return the JSON response
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching weather data: {e}")
        return {"error": str(e)}


def get_timezone_code(latitude: float, longitude: float) -> str:
    """
    Get the name of the timezone using latitude and longitude.
    :param latitude: latitude of the location.
    :param longitude: longitude of the location
    :return: name of timezone
    """

    timezone = TimezoneFinder()
    try:
        # Retrieve the timezone name based on latitude and longitude
        timezone_name = timezone.timezone_at(lat=latitude, lng=longitude)

        # Check if a valid timezone name was found
        if timezone_name:
            return timezone_name
        else:
            return "Timezone not found for the specified coordinates."

    except Exception as e:
        return f"An error occurred: {e}"


def get_datetime(timezone: str) -> dict:
    """
    Get the current date and time for a specified timezone.

    Args:
        timezone (str): The name of the timezone (e.g., 'Asia/Kolkata').

    Returns:
        dict: A dictionary containing the formatted date, time, and year.
              Returns an error message if the timezone is invalid.
    """
    
    try:
        # Initialize the timezone
        tz = pytz.timezone(timezone)

        # Get the current date and time in the specified timezone
        today_now = datetime.now(tz)

        # Format the date and time
        formatted_date = today_now.strftime("%d, %B")
        formatted_time = today_now.strftime("%H:%M:%S")
        year = today_now.strftime("%Y")
        day = today_now.strftime("%A")# Use %Y for a four-digit year

        return {
            "date": formatted_date,
            "time": formatted_time,
            "year": year,
            "day":day
        }

    except pytz.UnknownTimeZoneError:
        return {"error": "Invalid timezone specified. Please provide a valid timezone."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
