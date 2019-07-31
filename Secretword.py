print('Welcome to "Guess the Word Game!"')
print('You have 7 attempts at guessing letters in a word')
print('Let\'s begin!')
print('\n')

current_word = ["p", "r", "i", "n", "c", "e", "s", "s", "j", "a", "s", "m", "i", "n", "e"]
guesses = []
right_letters = 0
maxfails = 7
fails = 0
store_letter = ''
word_guess = "princess jasmine"
final = "princess jasmine"


print("There are 15 letters in the word")


while fails < maxfails:
    print('Youve guessed these letters so far: ', store_letter,  )
    letter_guess = input("Guess a letter ")
    if letter_guess == word_guess:
            print('Congrats you guessed the word!')
            break
    if letter_guess in current_word:
        right_letters = right_letters + 1
        store_letter += letter_guess
        print("Nice Job! You have ", len(current_word) - right_letters , " letters left!")
        print('\n')
    if letter_guess not in current_word:
        fails = fails + 1
        print("So close. You have " + str(maxfails - fails) + " tries left!")
        print('\n')
    if fails == 4:
        Clue = input("Would you like a clue? 'yes' or 'no'?")
        if Clue == "yes":
            print("She is a Disney Princess..")
            print('\n')
        if Clue == "no":
            print("Youre very brave!")
            print('\n')
    if fails == 7:
        final = input("Try to guess the word!: ")
        if final == word_guess:
            print ("You did it! Great job!")
        else:
            print ("Sorry. My word was ",word_guess, " better luck next time!")
    if fails == 1:
        print ("________      ")
        print ("|      |      ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
    if fails == 2:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
    if fails == 3:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /       ")
        print ("|             ")
        print ("|             ")
    if fails == 4:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|      ")
        print ("|             ")
        print ("|             ")
    if fails == 5:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|             ")
        print ("|             ")
    if fails == 6:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|     /       ")
        print ("|             ")
    if fails == 7:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|     / \     ")
        print ("|             ")
        print ("GAME OVER!")        
