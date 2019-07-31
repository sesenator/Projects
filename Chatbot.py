def main():
    answer = input("\n" + "What's your name? ")
    print("\n" + "Nice to meet you, " + answer + ".")
    sport()

def sport():
    print("\n")

    answer = input("Do you play sports?" + "\n")
    if answer == "yes":
        input("Which sports do you play?" + "\n")
        print("\n" + "That's great.")

    elif answer == "no":
        print("\n" + "That's a shame." + "\n")
        music()

    answer2 = input("Are you on a team?" + "\n")
    if answer2 == "yes":
        input("\n" + "What's the name of your team? ")
        print("\n" + "That's so cool!")
        music()
    elif answer2 == "no":
        print("\n" + "That's a shame." + "\n")
        music()


def music():
        input("What kind of music do you listen to?" + "\n")
        print("\n" + "That's nice!")

        input("Who do you listen to? " + "\n")
        print("\n" + "That's so cool!" + "\n")

        input("What you like about their music?" + "\n")
        print("\n" + "That's amazing!" + "\n")
        food()

def food():
    input("What type of food do you like?" + "\n")
    print("\n" + "That sounds yummy!" + "\n")

    input("Why do you like that food?" + "\n")
    print("\n" + "That's nice!" + "\n")

    input("What restaurant do you go to eat that?" + "\n")
    print("\n" + "Oh, I go there all the time!" + "\n")

    print("Thank you for talking to Chatbutt!")
    exit()

if __name__ == "__main__":
    main()
    sport()
    food()
