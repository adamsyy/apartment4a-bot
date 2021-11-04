import requests
import json
def news():
    res = json.loads(requests.get("https://ktu-news-api.herokuapp.com/ktu").text)
    return res