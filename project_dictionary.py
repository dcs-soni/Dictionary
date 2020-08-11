import json
from difflib import get_close_matches
data = json.load(open("project_dictionary_original.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
         return data[word.upper()]
    elif len(get_close_matches(word,data.keys())[0]) > 0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        user_decision = input("Enter y for Yes and n for No\n")
        if user_decision == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif user_decision == "n":
            print("Ooops I didn't have this word in my database\n")
        else:
            print("Please enter y or n\n")
    else:
        print("Ooops I don't have this word in my database\n")




word = input("Enter the word you want to search\n")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)