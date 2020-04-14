import json
from difflib import get_close_matches

data = json.load(open("abc.json"))

def function(word):
    word=word.lower();
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        print("Did you mean %s" %get_close_matches(word, data.keys())[0])
        dec=input("Press y for YES & n for NO:")
        if dec=="y":
            return data[get_close_matches(word, data.keys())[0]]
        elif dec=="n":
            print("No words found.")
        else:
            print("You have entered wrong input. Please just enter y or n.:")
    else:
        print("Poor choice of words. Please check your input again...('v')")
    return ""    



word=input("Enter your search: ")
output=function(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
