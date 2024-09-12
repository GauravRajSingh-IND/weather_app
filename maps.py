import requests
import math

from weather_function import get_location


key = "04081e17627f601aa461ea47e4ec87e9"

def lat_lon_to_tile(zoom):
    """Convert latitude and longitude to tile coordinates."""
    lat, lon = get_location()
    lat_rad = math.radians(lat)
    n = 2 ** zoom
    x = int((lon + 180) / 360 * n)
    y = int((1 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2 * n)
    return x, y


def get_cloud_map(zoom, api_key=key):
    """Fetch the cloud map image from OpenWeatherMap API."""
    x, y = lat_lon_to_tile(zoom)
    layer = 'temp_new'
    url = f"https://tile.openweathermap.org/map/{layer}/{zoom}/{x}/{y}.png?appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        with open('cloud_map.png', 'wb') as f:
            f.write(response.content)
        print("Map saved as 'cloud_map.png'")
    else:
        print(f"Error fetching map: {response.status_code}")


zoom_level = 5  # Zoom level

get_cloud_map(zoom_level)