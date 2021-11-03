import requests
import json
def notifications():
    final_message=""
    final_message_list=[]
    res=json.loads(requests.get("http://ktu.amith.ninja/").text)
    for i in res["notifications"]:
        final_message_list.append(f"{i['title']}\n{i['description']}\nLink : {i['links'][0]['url']}")
    final_message="\n-------------------------------------------\n".join(final_message_list)
    
    return final_message
