import random
import string

def generate_passwrd(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_lenght = int(input("What's the password's minimum lenght?: "))
has_number = (input("Does it need to have numbers? (y/n): ")).lower() == "y"
has_special = (input("Does it need to have a special character? (y/n): ")).lower() == "y"

pwd = generate_passwrd(min_lenght, has_number, has_special)
print(pwd)