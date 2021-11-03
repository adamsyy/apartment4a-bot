import requests
import json
def notifications():
    final_message=""
    final_message_list=[]
    res=json.loads(requests.get("http://ktu.amith.ninja/").text)
    i=res["notifications"][0]
    # final_message_list.append(f"{i['title']}\n{i['description']}\nLink : {i['links'][0]['url']}")
    final_message=f"{i['title']}\n{i['description']}\nLink : {i['links'][0]['url']}"
    # print(len(final_message))
    
    return final_message
