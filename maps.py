import folium
import math
from weather_function import get_location

# Replace with your actual OpenWeatherMap API key
api_key = "04081e17627f601aa461ea47e4ec87e9"


def lat_lon_to_tile(lat, lon, zoom):
    """Convert latitude and longitude to tile coordinates."""
    lat_rad = math.radians(lat)
    n = 2 ** zoom
    x = int((lon + 180) / 360 * n)
    y = int((1 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2 * n)
    return x, y


def create_map_with_weather_layer(zoom= 3, api_key=api_key):
    # Get latitude and longitude
    lat, lon = get_location()

    # Create a base map centered at the specified latitude and longitude
    base_map = folium.Map(location=[lat, lon], zoom_start=zoom)

    # Calculate tile coordinates
    x, y = lat_lon_to_tile(lat, lon, zoom)

    # Define the OpenWeatherMap tile layer for temperature
    layer = f"https://tile.openweathermap.org/map/temp_new/{zoom}/{{x}}/{{y}}.png?appid={api_key}"

    # Add the tile layer to the base map
    folium.TileLayer(
        tiles=layer,
        attr='OpenWeatherMap',
        name='Temperature Layer',
        overlay=True,
        control=True
    ).add_to(base_map)

    # Add layer control to toggle layers
    folium.LayerControl().add_to(base_map)

    # Save the map to an HTML file
    base_map.save('weather_map.html')


# Create the map with the weather layer
create_map_with_weather_layer()