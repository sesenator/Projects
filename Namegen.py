name = input("Hi! Whats your name? ")
print("Nice to meet you " + name + "!")
print("I see that youre struggling to name your new dog, I think I can help with that!")
print('\n')
gender = input("Lets start off with the first question, is your dog 'boy' or a 'girl'? ")
if gender == 'boy':
    print('\n')
    print("Okay lets move on to the next question")
    height = input("Is your dog 'tall' or 'short'? ")
    if height == 'tall':
        print('\n')
        import random
        print("Big doggie! Okay im generating names")
        tallmale = [" Avalanche ", " Bandit ", " Bane ", " Blaze ", " Bruiser ", " Brutus ", " Caesar "]
        print("You got the name" + random.choice(tallmale) + "for your doggy!!!")
    if height == 'short':
        print('\n')
        import random
        print("Aww small doggie! Okay im generating names")
        smallmale = [" Max ", " Charlie "," Buddy "," Cooper "," Jack "," Rocky "," Bear "," Duke "]
        print("You got the name" + random.choice(smallmale) + "for your doggy!!!")
if gender == 'girl':
    print('\n')
    print("Cool on to the next question")
    height = input("Is your dog 'tall' or 'short'? ")
    if height == 'tall':
        print('\n')
        import random
        print("Big doggie! Okay im generating names")
        tallfemale =[" Alfalfa ", " Archie ", " Boots ", " Bubbles ", " Clover ", " Cuddles ", " Dimples "]
        print("You got the name" + random.choice(tallfemale) + "for your doggy!!!")
    if height == 'short':
        print('\n')
        import random
        print("Aww small doggie! Okay im generating names")
        smallfemale = [" Bella ", " Lucy ", " Daisy ", " Luna ", " Lola ", " Sadie ", " Molly ", " Bailey ", " Maggie ", " Sophie "]
        print("You got the name" + random.choice(smallfemale) + "for your doggy!!!")
