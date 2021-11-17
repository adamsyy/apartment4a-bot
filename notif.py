import requests
import json
def notifications(no=1):
    try:
        no=int(no)
    except:
        return("please specify a number")
    final_message=""
    final_message_list=[]
    res=json.loads(requests.get("https://ktunotification.herokuapp.com/").text)
    if(no>10 or no<1):
        return "I can do only the Last 10 Sorry for letting you down"
    i=res["notifications"][no-1]
    # final_message_list.append(f"{i['title']}\n{i['description']}\nLink : {i['links'][0]['url']}")
    final_message=f"{i['title']}\n{i['description']}\nLink : {i['links'][0]['url']}"
    # print(len(final_message))
    
    return final_message
