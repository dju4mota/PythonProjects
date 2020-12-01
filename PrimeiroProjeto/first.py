import json
import time

data = json.load(open("data.json"))


def search(w):
    if data.get(w.lower()):
        return data[w.lower()]
    else:
        return ["Sorry :( No word found. Please check."]


print("Starting ...")
time.sleep(2)
print(" *** Type -1 to leave ***")

word = ""
while True:
    word = input("Enter a word: ")

    if word == "-1":
        print("Closing ... ")
        time.sleep(1)
        break

    results = search(word)

    for meaning in results:
        print(meaning)
