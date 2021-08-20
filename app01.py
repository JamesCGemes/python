import json
from difflib import get_close_matches


data = json.load(open("dictionary/data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]    
    elif len(get_close_matches (w, data.keys())) > 0:  
        yes_or_no = input("Did you mean %s instead? Enter Y or N: " % get_close_matches(w, data.keys())[0])
        if yes_or_no == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yes_or_no == "N":
            return "The word does not exist. Please check it"
        else:
            return "We didnt understand your entry"    
    else: 
        return "That word dosnt exist"
        

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)       