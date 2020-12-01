import json
import time

data = json.load(open("data.json"))


def search(word):
    return data[word]


print("Starting ...")
time.sleep(2)

results = search(input("Enter a word: "))

for meaning in results:
    print(meaning)
