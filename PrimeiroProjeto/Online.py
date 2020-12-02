import mysql.connector
import difflib
import time

print("Starting ...")
print(" *** Type -1 to leave ***")

con = mysql.connector.connect(user="ardit700_student", password="ardit700_student", host="108.167.140.122",
                              database='ardit700_pm1database',)
cursor = con.cursor()
cursor.execute(f"SELECT Expression FROM Dictionary")
list_exp = cursor.fetchall()


def alter_list(aux):
    return aux[0]


list_expressions = list(map(alter_list, list_exp))  # list with all expressions to check the input grammar


def closest_word(w):
    return difflib.get_close_matches(w, list_expressions, 2, 0.8)


def request(w):
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{w}'")
    return cursor.fetchall()


def search(w):
    response = request(w)
    if response:
        return response
    else:
        closest = closest_word(w)
        if len(closest) > 0:
            if input(f"Did you mean in {closest[0]} instead ? Enter y or n: ") == "y":
                return request(closest[0])


word = ""
while True:
    word = input("\nEnter a word: ")

    if word == "-1":
        print("Closing ... ")
        time.sleep(1)
        break

    results = search(word)

    if results:
        for meaning in results:
            print(meaning[1])
    else:
        print(":( Sorry. No word found. please double check it")
