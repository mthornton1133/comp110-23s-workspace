"""EX02 - One Shot Wordle - a one chance wordle game."""

__author__= 730546472

SECRETWORD: str = "python"
guess: str = input(f"What is your {len(SECRETWORD)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(SECRETWORD):
    guess = input(f"That was not {len(SECRETWORD)}-letters! Try again: ")

i: int = 0
emoji_result: str = ""


while i < len(SECRETWORD):
    alt_idx_of_secret: int = 0
    guessed_charcater: bool = False
    if guess[i] == SECRETWORD[i]:
        emoji_result = emoji_result + GREEN_BOX
    else:
        while alt_idx_of_secret < len(SECRETWORD) and guessed_charcater == False:
            if SECRETWORD[alt_idx_of_secret] == guess[i]:
                guessed_charcater = True
            alt_idx_of_secret = alt_idx_of_secret + 1
        if guessed_charcater == True:
            emoji_result = emoji_result + YELLOW_BOX
        else:
            emoji_result = emoji_result + WHITE_BOX
    i = i + 1

print(emoji_result)

if guess == SECRETWORD:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

