import json
from difflib import get_close_matches 


data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    word = get_close_matches(word, data.keys())[0]
    print('result for: ' + word)
    return data[word]


word = "paranza"

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)