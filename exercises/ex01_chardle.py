"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730546472"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(five_character_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(single_character) < 1:
    print("Error: Character must be a single character.")
    exit()
amount_of_matching_characters: int = 0

print("Searching for " + single_character + " in " + five_character_word)

if five_character_word[0] == single_character:
    print(single_character + " found at index 0")
    amount_of_matching_characters = amount_of_matching_characters + 1
if five_character_word[1] == single_character:
    print(single_character + " found at index 1")
    amount_of_matching_characters = amount_of_matching_characters + 1
if five_character_word[2] == single_character:
    print(single_character + " found at index 2")
    amount_of_matching_characters = amount_of_matching_characters + 1
if five_character_word[3] == single_character:
    print(single_character + " found at index 3")
    amount_of_matching_characters = amount_of_matching_characters + 1
if five_character_word[4] == single_character:
    print(single_character + " found at index 4")
    amount_of_matching_characters = amount_of_matching_characters + 1

if amount_of_matching_characters == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
else:
    print(str(amount_of_matching_characters) + " instances of " + single_character + " found in " + five_character_word)