import json
import time
import difflib

data = json.load(open("data.json"))


def closest_word(w):
    return difflib.get_close_matches(w, data.keys(), 2, 0.8)


def search(w):

    if data.get(w.lower()):
        return data[w.lower()]
    elif len(closest_word(w)) > 0:
        if input(f"Did you mean in {closest_word(w)[0]} instead ? Enter y or n: ") == "y":
            return data[closest_word(w)[0].lower()]
    return [f":( Sorry. No word found. Please double check it"]


print("Starting ...")
time.sleep(2)
print(" *** Type -1 to leave ***")

word = ""
while True:
    word = input("\nEnter a word: ")

    if word == "-1":
        print("Closing ... ")
        time.sleep(1)
        break

    results = search(word)

    for meaning in results:
        print(meaning)
