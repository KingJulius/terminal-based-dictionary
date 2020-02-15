import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word =  word.lower()
    if word in data: #For Improper Nouns
        return data[word]
    elif word.title() in data: #For Proper Nouns
        return data[word.title()]
    elif word.upper() in data: #For Acronyms
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        result = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word ,data.keys())[0])
        if result == "Y":
            return data[get_close_matches(word ,data.keys())[0]] # Based on similarity index and gets the most similar one
        elif result == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
