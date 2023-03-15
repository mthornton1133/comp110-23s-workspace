"""EX06 - Create Your Own Adventure - A buzzfeed quiz for one's harry potter house."""

__author__ = "730546472"

points: int = 0
player: str = ""
FROWN_FACE: str = "\U0001F620"


def main() -> None:
    """Main function that orchestrates my adventure/quiz."""
    global points
    global player
    greet()
    #Enter into experience.
    print(f"Well {player}, now that you have been accepted into Hogwarts School of Witchcraft and Wizardry, it is time for you to get sorted into your house.")
    i: int = 0
    #This is the loop that allows player to choose other options.
    while i < 4:
        choice: str = input(f"You now have the ability to choose in what order you want to prodeed. This statement will be repeated after each test. 1) Take the character test. 2) Takle the physical test. 3) Answer a series of imformative questions. 4) Just do not play {FROWN_FACE}. Note you can choose the same test up to 4 times but this will greatly impact where you are placed. Also quitting before completion of other 3 tests will impact you placement. It is recommended you quit as the fourth choice. Say 1, 2, 3, or 4 to choose: ")
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            choice = input("Just say 1, 2, 3, or 4 to continue. ")
        if choice == "1":
            intital_character_test()
        if choice == "2":
            sub_total: int = physical_test(points)
            points += sub_total
        if choice == "3":
            print(f"Your current score is {points}.")
            print("These questions will imform us greatly about your personal preferences.")
            answer1: str = input("Do you prefer the sun or the moon? ")
            while answer1 != "sun" and answer1 != "moon":
                answer1 = input("Pick \"sun\" or \"moon\". ")
            if answer1 == "sun":
                print("Interesting.")
                points += 3
            if answer1 == "moon":
                print("Hmm interesting.")
                points += 1
            answer2: str = input("Do you prefer dogs or cats? ")
            while answer2 != "dogs" and answer2 != "cats":
                answer2 = input("Pick \"dogs\" or \"cats\". ")
            if answer2 == "dogs":
                print("Hmm interesting.")
                points += 3
            if answer2 == "cats":
                print("Okay.")
                points += 1
            answer3: str = input("Do you prefer red or blue? ")
            while answer3 != "red" and answer3 != "blue":
                answer3 = input("Pick \"red\" or \"blue\". ")
            if answer3 == "red":
                print("Interesting.")
                points += 3
            if answer3 == "blue":
                print("Hmm okay.")
                points += 1
            answer4: str = input("Do you prefer pens or pencils? ")
            while answer4 != "pens" and answer4 != "pencils":
                answer4 = input("Pick \"pens\" or \"pencils\". ")
            if answer4 == "pens":
                print("Hmm interesting.")
                points += 3
            if answer4 == "pencils":
                print("Facinating.")
                points += 1
            answer5: str = input("Do you prefer checkers or chess? ")
            while answer5 != "checkers" and answer5 != "chess":
                answer5 = input("Pick \"checkers\" or \"chess\". ")
            if answer5 == "checkers":
                print("Hmm.")
                points += 3
            if answer5 == "chess":
                print("Hmm how curious.")
                points += 1
            print(f"Thank you {player} for answering these questions, now we must continue on.")
        if choice == "4":
            farewell()
        i += 1


def greet() -> None:
    global player
    player = input("What is your name: ")
    print(f"Greetings {player}, this adventure will determine what harry potter house you belongs to out of: Gryffindor, Ravenclaw, Hufflepuff, and Slytherin. These houses may be a bit different to the ones you know.")


def intital_character_test() -> int:
    global points
    global player
    print(f"Currently you total amount of points are {points}.")
    answer: str = input(f"Which of these characterics do you, {player} think best describe you: brave, patient, wise, or ambitious?: ")
    characteristics: list[str] = ["brave", "patient", "wise", "ambitious"]
    while answer != characteristics[0] and answer != characteristics[1] and answer != characteristics[2] and answer != characteristics[3]:
        answer = input(f"Not one of the choices {FROWN_FACE}, try again: ")
    if answer == "brave":
        print("Hmmm okay")
        points += 15
        return points
    if answer == "patient":
        print("Hmmm okay")
        points += 10
        return points
    if answer == "wise":
        print("Hmmm okay")
        points += 5
        return points
    if answer == "ambitious":
        print("Hmmm okay")
        points += 0
        return points


def physical_test(current_state: int) -> int:
    """This fn makes the user fight through a hypothetical battle and further sorts the user."""
    global player
    print(f"The current score is {current_state}.")
    from random import randint
    print(f"{player}, this test will see how you would react in a hypothetical battle between 4 random creatures. They will be decided on by a random number.")
    random_number: int = randint(1, 4)
    points_accumulated: int = 0
    print(f"Your random number is {random_number}.")
    if random_number == 1:
        print(f"{player}, you will be fighting a gorilla.")
        points_accumulated += gorilla_fight()
        return points_accumulated
    if random_number == 2:
        print(f"{player}, you will be fighting a tiger.")
        points_accumulated += tiger_fight()
        return points_accumulated
    if random_number == 3:
        print(f"{player}, you will be fighting a giant spider.")
        points_accumulated += giant_spider_fight()
        return points_accumulated
    if random_number == 4:
        print(f"{player}, you will be fighting a dragon.")
        points_accumulated += dragon_fight()
        return points_accumulated
    

def gorilla_fight() -> int:
    """This fn simulates the players brief fight with a gorilla."""
    points_total: int = 0
    decision1: str = input("You find yourself in a jungle with a hostile gorilla dead ahead. Do you grab a \"flute\" or a \"sword\"?: ")
    while decision1 != "flute" and decision1 != "sword":
        decision1 = input("Say \"flute\" or \"sword\" to continue. ")
    if decision1 == "flute":
        points_total += 0
        decision2: str = input("The gorilla charges at you. Do you \"play flute\" or \"throw flute\"?: ")
        while decision2 != "play flute" and decision2 != "throw flute":
            decision2 = input("Say \"play flute\" or \"throw flute\" to continue. ")
        if decision2 == "play flute":
            print("The gorilla collapses and falls asleep congrats you beat it.")
            points_total += 0
        if decision2 == "throw flute":
            print("The flute bouces off of the 800 pound gorilla and you hurt his feelings. He crys and walks away.")
            points_total += 5
    if decision1 == "sword":
        points_total += 5
        decision3: str = input("The gorilla charges at you. Do you \"swing sword\" or \"surrender\"?: ")
        while decision3 != "swing sword" and decision3 != "surrender":
            decision3 = input("Say \"swing sword\" or \"surrender\" to continue. ")
        if decision3 == "swing sword":
            print("You made the 800 pound gorilla angry and you got one shot.")
            points_total += 5
        if decision3 == "surrender":
            print("The gorilla comes and hugs you. He just wanted a friend.")
            points_total += 0
    return points_total


def tiger_fight() -> int:
    """This fn simulates the fight between the player and a tiger."""
    points_total: int = 0
    decision1: str = input("You encounter a hostile tiger in the wild. Do you \"grab gun\" or \"grab shoes\"?: ")
    while decision1 != "grab gun" and decision1 != "grab shoes":
        decision1 = input("Say \"grab gun\" or \"grab shoes\" to continue. ")
    if decision1 == "grab gun":
        points_total += 5
        decision2: str = input("The tiger charges at you. Do you \"shoot gun\" or \"throw gun\"?: ")
        while decision2 != "shoot gun" and decision2 != "throw gun":
            decision2 = input("Say \"shoot gun\" or \"throw gun\" to continue. ")
        if decision2 == "shoot gun":
            print("This is a tiger that can run 45 mph and you are not the best shot. You lose :(.")
            points_total += 5
        if decision2 == "throw gun":
            print("The tiger jumps onto the gun and starts to play with it like a toy. You are then able to slip away.")
            points_total += 0
    if decision1 == "grab shoes":
        points_total += 0
        decision3: str = input("These shoes look like you could run fast in them. The tiger rushes at you. Do you \"wear shoes\" or \"ditch shoes\"?: ")
        while decision3 != "wear shoes" and decision3 != "ditch shoes":
            decision3 = input("Say \"wear shoes\" or \"ditch shoes\" to continue. ")
        if decision3 == "wear shoes":
            print("You are imbued with super speed and can run away safely.")
            points_total += 0
        if decision3 == "ditch shoes":
            points_total += 5
            print("You slowly run away and the grown tiger catches you.")
    return points_total


def giant_spider_fight() -> int:
    """This fn simulates the fight between the player and a giant spider."""
    points_total: int = 0
    decision1: str = input("You find yourself in some cave and encounter a terrifying giant spider. Do you grab a \"torch\" or \"perfume\"?: ")
    while decision1 != "torch" and decision1 != "perfume":
        decision1 = input("Say \"torch\" or \"perfume\" to continue. ")
    if decision1 == "torch":
        points_total += 5
        decision2: str = input("The spider grawls towards you. Do you \"throw torch\" or \"drop torch\"?: ")
        while decision2 != "throw torch" and decision2 != "drop torch":
            decision2 = input("Say \"throw torch\" or \"drop torch\" to continue. ")
        if decision2 == "throw torch":
            print("You miss as you were standing far away. Now you are spider food.")
            points_total += 5
        if decision2 == "drop torch":
            print("Dropping the torch starts a fire in the cave. The spider is scared of fire and you escape.")
            points_total += 0
    if decision1 == "perfume":
        points_total += 0
        decision3: str = input("The spider crawls towards you. Do you \"spray perfume\" or \"throw perfume\"?: ")
        while decision3 != "spray perfume" and decision3 != "throw perfume":
            decision3 = input("Say \"spray perfume\" or \"throw perfume\" to continue. ")
        if decision3 == "spray perfume":
            print("The strong smell of the perfume repels the spider and you are able to walk out easily.")
            points_total += 0
        if decision3 == "throw perfume":
            print("The perfume breaks on the ground and just makes the spider angry. You do not last 3 seconds.")
            points_total += 5
    return points_total


def dragon_fight() -> int:
    """This fn simulates a fight between the player and a dragon."""
    points_total: int = 0
    decision1: str = input("You find yourself in an open field with a dragon swooping down in front of you. Do you \"grab shield\" or \"wear helmet\"?: ")
    while decision1 != "grab shied" and decision1 != "wear helmet":
        decision1 = input("Say \"grab shield\" or \"wear helmet\" to continue. ")
    if decision1 == "grab shield":
        points_total += 5
        decision2: str = input("The dragon looks as if he is about the breath fire. Do you \"use shield\" or \"throw shield\"?: ")
        while decision2 != "use shield" and decision2 != "throw shield":
            decision2 = input("Say \"use shield\" or \"throw shield\" to continue. ")
        if decision2 == "use shield":
            print("This dinky looking shield turns out to be magical and repels the dragon.")
            points_total += 0
        if decision2 == "throw shield":
            print("The dragon chews it up and spits it back out at you. The force of him spitting knocks you unconscience.")
            points_total += 5
    if decision1 == "wear helmet":
        points_total += 0
        decision3: str = input("The helmet gives you magical abilities. Do you \"tame dragon\" or \"defeat dragon\"?: ")
        while decision3 != "tame dragon" and decision3 != "defeat dragon":
            decision3 = input("Say \"tame dragon\" or \"defeat dragon\" to continue. ")
        if decision3 == "tame dragon":
            print("The dragon submits to your commands. You fly away on the dragon.")
            points_total += 0
        if decision3 == "defeat dragon":
            print("For whatever reason you decide to take down the dragon. It would have been cooler to have a domesticated dragon.")
            points_total += 5
    return points_total
        


def farewell() -> None:
    """This will serve as the goodbye function."""
    global player
    global points
    print(f"Thank you {player} for playing, play agian another time for possibly different results.")
    print(f"The total amount of points accumulated is {points}.")
    if points < 10:
        print(f"Well {player} you have been placed into Slytherin. You are shrewd and ambitious or you quit the game early {FROWN_FACE}.")
    if points > 10 and points < 20:
        print(f"Well {player} you have been placed into Ravenclaw. You are very intelligent and cunning.")
    if points > 20 and points < 30:
        print(f"Well {player} you have been placed into Hufflepuff. You are humble and kind.")
    if points > 39:
        print(f"Well {player} you have been placed into Gryffindor. You are brave, daring, and possibly the main character.")
    quit()

if __name__ == "__main__":
    main()