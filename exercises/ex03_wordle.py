"""EX03 - Structured Wordle - The final wordle"""

__author__ = "730546472"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(muli_char_str: str, single_char: str) -> bool:
    """This fn says whether the single character is anywhere within the multi character str"""
    assert len(single_char) == 1
    i: int = 0
    while i < len(muli_char_str):
        alt_i: int = 0
        bool_var: bool = False
        if muli_char_str[i] == single_char[0]:
            return True
        else:
            while alt_i < len(muli_char_str) and not bool_var:
                if muli_char_str[alt_i] == single_char[0]:
                    bool_var = True
                alt_i = alt_i + 1
            if bool_var:
                return True
            else:
                return False
        i = i + 1 

def emojified(guess: str, secret: str) -> str:
    """This fn tests to see which color corresponds to each character in the guess and secret parameters"""
    assert len(guess) == len(secret)
    box_emojis: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            box_emojis = box_emojis + GREEN_BOX
        else:
            if contains_char(secret, guess[i]) == True:
                box_emojis = box_emojis + YELLOW_BOX
            else:
                box_emojis = box_emojis + WHITE_BOX
        i = i + 1
    return box_emojis

def input_guess(expected_length: int) -> str:
    """This fn prompts the user for a word that is the length of the given parameter"""
    guessed_word: str = input(f"Enter a {expected_length} character word: ")
    while len(guessed_word) != expected_length:
        guessed_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guessed_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRETWORD: str = "codes"
    n: int = 1
    while n <= 6:
        print(f"=== Turn {n}/6 ===")
        guessed_word: str = input_guess(len(SECRETWORD))
        print(emojified(guessed_word, SECRETWORD))
        if guessed_word == SECRETWORD:
            return print(f"You won in {n}/6 turns!")
        n = n + 1
    if guessed_word != SECRETWORD:
        return print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()