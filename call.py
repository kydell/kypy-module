import requests, os
from dotenv import load_dotenv

load_dotenv()

def wordDef(word):
    '''basic API call function to retrieve word definition from Merriam Webster'''
    dicttoken = os.environ["DICT_KEY"]
    base_url = os.environ["DICT_URL"]
    call_url = base_url + word + "?key=" + dicttoken
    r = requests.get(url=call_url)
    try:
        r.raise_for_status()
    except:
        print(f"Error in request: {r.status_code}")
    response = r.json() # list
    otherresponse = r.text # string
    print(response)
    #print(otherresponse)

if __name__ == "__main__":
    word = input("Pick a word to define: ")
    #word = "greetings"
    wordDef(word)