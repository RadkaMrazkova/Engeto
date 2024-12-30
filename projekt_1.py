"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Radka Mrázková
email: radkamrazkova4@seznam.cz
"""
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


def select_text():
    try:
        text_number = int(input("Enter a number btw. 1 and 3 to select: "))
        print("------------------------------------------")

        if text_number < 1 or text_number > 3:
            print("The number must be between 1 and 3")
            return -1
        return text_number

    except ValueError:
        print("Please enter a valid integer.")
        return -1
    

def create_graph(selected_text):
    text = TEXTS[selected_text - 1]
    words = [word.strip(".,!?'\"") for word in text.split()]
    lengths = {}
    for word in words: 
        length = len(word)
        if length in lengths:
            lengths[length] += 1
        else:
            lengths[length] = 1

    max_occurence = max(lengths.values())

    for key in sorted(lengths.keys()):
        count = lengths[key]
        print(f"{str(key).rjust(3)}|{'*' * count}{' ' * (max_occurence - count + 2)}|{count}")


def count_statistics(selected_text):
    text = TEXTS[selected_text - 1]
    words = [word.strip(".,!?'\"") for word in text.split()]
    print(f"There are {len(words)} words in the selected text.")
    
    titlecase_words = [word for word in words if word[0].isupper()]
    print(f"There are {len(titlecase_words)} titlecase words.")

    uppercase_words = [word for word in words if word.isalpha() and word.isupper()]
    print(f"There are {len(uppercase_words)} uppercase words.")

    lowercase_words = [word for word in words if word.islower()]
    print(f"There are {len(lowercase_words)} lowercase words.")

    numeric_words = [word for word in words if word.isnumeric()]
    print(f"There are {len(numeric_words)} numeric strings.")

    total_sum = 0
    for word in numeric_words:
        total_sum += int(word)
    print(f"The sum of all the numbers {total_sum}")


def login(username, password):
    return username in registered_users and registered_users[username] == password


def main():
    username = input("username:")
    password = input("password:")

    if not login(username, password):
        print("unregistered user, terminating the program..")
        return 1
    
    print("------------------------------------------")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("------------------------------------------")

    selected_text = select_text()
    if selected_text == -1:
        return 1

    count_statistics(selected_text)

    print("------------------------------------------")
    print("LEN|  OCCURENCES  |NR.")
    print("------------------------------------------")

    create_graph(selected_text)
    return 0


if __name__ == "__main__":
    main()