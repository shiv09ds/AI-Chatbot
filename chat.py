import json 
from typing import Optional
import requests

def chatbot(message : Optional[str] = None) -> None:
    api = f"http://api.brainshop.ai/get?bid=180356&key=6DRvcrqFlApaokis&uid=4&msg={message}"
    value = requests.get(api).text

    return json.loads(value)["cnt"]

if __name__ == "__main__":
    while True:
        me = input("You : ")
        print("Bot : " , chatbot(me))
