import requests
import geocoder
from geopy.geocoders import Nominatim


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
