import requests
import dotenv
import os
from typing import Dict, Any, List

# the dotenv, use to extra key and end points of the news.
dotenv.load_dotenv()

def fetch_news(api_key: str=os.getenv('news_api_key'), endpoint: str=os.getenv('news_end_point'), country: str="us") -> dict:
    """
    Fetch news articles from the specified endpoint using the provided API key and country code.
    Args:
        api_key (str): The API key for authentication.
        endpoint (str): The endpoint URL for the news API.
        country (str): The country code for news articles.

    Returns:
        dict: A dictionary containing the news articles or an empty dictionary in case of an error.
    """

    if not api_key or not endpoint:
        print("Invalid or None api_key or end_points")
        return {}

    # Set parameters for API end points.
    params = { 'apiKey': api_key, 'q':'en', 'country':country}

    try:
        response = requests.get(url=os.getenv('news_end_point'), params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return {}


def get_news_data() -> List[Dict[str, Any]]:
    """
    Get news articles by calling the fetch_news function.
    Returns: List[Dict[str, Any]]: A list of news articles or an empty list in case of an error.
    """
    response = fetch_news()

    # Check if the response contains articles
    if 'articles' in response and response['articles']:
        return response['articles']
    else:
        print("Error while accessing the data or no articles found.")
        return []


def get_current_article_data(articles: list, article_no: int = 0) -> Dict[str, Any]:
    """
    Retrieves the data for the specified article from the list of articles.

    Args:
        articles (list): A list of article dictionaries.
        article_no (int): The index of the article to retrieve (default is 0).

    Returns:
        dict: A dictionary containing the article data, or an empty dictionary if the article is not found.
    """
    if article_no < 0 or article_no >= len(articles):
        print("No article to show")
        return {}

    current_article = articles[article_no]

    article_data = {
        'source': current_article['source']['name'],
        'author': current_article['author'],
        'title': current_article['title'],
        'description': current_article['description'],
        'post': current_article['url'],
        'image': current_article['urlToImage'],
        'published': current_article['publishedAt'],
        'content': current_article['content']
    }

    return article_data
