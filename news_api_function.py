import requests
import dotenv
import os

# the gotenv, use to extra key and end points of the news.
dotenv.load_dotenv()

def get_current_news(api_key: str=os.getenv('news_api_key'), endpoint: str=os.getenv('news_end_point')) -> dict:

    if not api_key or not endpoint:
        print("Invalid or None api_key or end_points")
        return {}

    # Set parameters for API end points.
    params = { 'apiKey': api_key, 'q':'en'}

    try:
        response = requests.get(url=os.getenv('news_end_point'), params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return {}

