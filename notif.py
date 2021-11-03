import requests
import json
def notifications(no=1):
    try:
        no=int(no)
    except:
        print("ERR:Couldnt convert into interger")
    final_message=""
    final_message_list=[]
    res=json.loads(requests.get("http://ktu.amith.ninja/").text)
    if(no>5 or no<1):
        return "I can do only the Last 5 Sorry for letting you down"
    i=res["notifications"][no-1]
    # final_message_list.append(f"{i['title']}\n{i['description']}\nLink : {i['links'][0]['url']}")
    final_message=f"{i['title']}\n{i['description']}\nLink : {i['links'][0]['url']}"
    # print(len(final_message))
    
    return final_message
