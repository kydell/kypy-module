import requests, os
from dotenv import load_dotenv

load_dotenv()

def pickit():
    '''choice option function to choose what you want to do here'''
    print("Welcome!\nLet's look at words!\n")
    choice = input("To define, press '1'.\nTo thesaur, press '2'.\nyour selection: ")
    if choice == "1":
        word = input("Pick a word to define: ")
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
            return response
        answer = wordDef(word)
    elif choice == "2":
        word = input("Pick a word to thesaur: ")
        def wordThes(word):
            '''basic API call function to retrieve Thesaurus entry'''
            thestoken = os.environ["THES_KEY"]
            base_url = os.environ["THES_URL"]
            call_url = base_url + word + "?key=" + thestoken
            r = requests.get(url=call_url)
            try:
                r.raise_for_status()
            except:
                print(f"Error in request: {r.status_code}")
            response = r.json() # list
            print(response)
            return response
        answer = wordThes(word)
    else:
        print("You chose not a choice. :-(\nQuitting...")
        quit()
    return answer


if __name__ == "__main__":
    pick = pickit()