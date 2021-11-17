import requests
import json
def news():
    res = json.loads(requests.get("https://ktu-news-apis.herokuapp.com/ktu").text)
    return res
