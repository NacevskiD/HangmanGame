class Hangman:
    #initiating the init method with the number of tries and the character list
    def __init__(self):
        self.tries = 6
        self.characterList = []
    #draws the hangman depending on the # of tries left
    def hangman(self):

        if self.tries == 6:
            print("\n\n\n  |---|\n  |\n  |\n  |")
            print("____________")
        elif self.tries == 5:
            print("\n\n\n  |---|\n  |   O\n  |\n  |")
            print("____________")
        elif self.tries == 4:
            print("\n\n\n  |---|\n  |   O\n  |   |\n  |")
            print("____________")
        elif self.tries == 3:
            print("\n\n\n  |---|\n  |   O\n  |   |\\\n  |")
            print("____________")
        elif self.tries == 2:
            print("\n\n\n  |---|\n  |   O\n  |  /|\\\n  |")
            print("____________")
        elif self.tries == 1:
            print("\n\n\n  |---|\n  |   O\n  |  /|\\\n  |    \\")
            print("____________")
        elif self.tries == 0:
            print("\n\n\n  |---|\n  |   O\n  |  /|\\\n  |  / \\")
            print("____________")
    #Introduction with the number of tries left
    def intro(self):
        print("\nGuess the word!\n"
              "Tries left: " + str(self.tries + 1),
              "\nEnter a letter: \n")
    #prints the dashes or if already entered, letters
    def dashLoop(self,word):
        dash = "_"
        for character in word:
            if character in self.characterList:
                print(character, end=" ")
            else:
                print(dash, end=" ")
    #tests the input from the user
    def inputTest(self):
        ok = True
        letter = input()
        while ok:
            try:
                alphaTest = False
                while letter.isdigit() or len(letter) > 1:
                    print("You entered a digit or more than 1 letter, please try again. \n")
                    letter = input()
                while ok:
                    if letter.isalpha():
                        ok = False
                    else:
                        print("Please enter a letter.\n")
                        letter = input()
            except AttributeError:
                print("You didn't enter a letter, please try again.\n")
                letter = input()
        return letter
    #gets a random word from the text file
    def getWord(self):
        import random
        words = []
        try:
            file = open("data.txt", "r")
        except FileNotFoundError:
            print("The data file was not found. Please restart and try again.")
            exit()
        for line in file:
            words.append(line.rstrip('\n'))

        # sample words

        # choose a random word, creating the list, number of tries, and the word length
        word = random.choice(words)
        return word
    #returns the number of tries
    def getTries(self):
        return self.tries
    #reduces the number of tries left by 1
    def subtractTries(self):
        self.tries -=1
    #addsa a letter to the list
    def listAdd(self,letter):
        self.characterList.append(letter)
    #removes a letter from the list
    def listRemove(self,letter):
        self.characterList.remove(letter)
    #checks if the conditions for winning have been met and returns the number
    def getWinCondt(self,word):
        winCondt = 0
        #compares every letter in the list to the times that letter is contained in the word and returns the result
        for character in self.characterList:
            for letter in word:
                if character == letter:
                    winCondt +=1
        return winCondt
    #ending screen that shows wether you won or lost
    def endScreen(self):
        if self.tries == 0:
            print("You lost, try again.\n")
        else:
            print("Congratulations, you won!")
#function for the methods called most often
def essentials(word):
    game.intro()
    game.dashLoop(word)
    game.hangman()
#function for the end screen
def end(word):
    game.dashLoop(word)
    game.hangman()
    game.endScreen()

game = Hangman()

word = game.getWord()
essentials(word)
wordLen = len(word)

# asking for a letter and initiating the winCondt and loseCondt
letter = game.inputTest()
winCondt = 0
loseCondt = 0
# a loop that keeps going until there are no more tries left or the word has been guessed
while game.getTries() != loseCondt:
    #adds the entered letter to the list
    game.listAdd(letter.lower())
    #if the entered letter is not in the word
    #subtracts 1 try, prints the essentials again, removes the letter from the list and asks for a new one
    if letter.lower() not in word:
        print("Wrong letter!")
        game.subtractTries()
        essentials(word)
        print()
        game.listRemove(letter)
        letter = game.inputTest()

    else:
        winCondt = game.getWinCondt(word)
        #checking if the winCondt is the same length as the word, if it is the loop breaks and you win
        if winCondt == wordLen:
            break

        essentials(word)
        letter = game.inputTest()

#ending screen
end(word)
