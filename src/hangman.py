# Hangman game
import random
import string

WORD_LIST = "words.txt"

def loadWords():
    
    print("Loading word list from file...")
    # fhandle: file
    fhandle = open(WORD_LIST, 'r')
    # line: string
    line = fhandle.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
     choosing a random word
    """
    return random.choice(wordlist)

#  Store returned word list
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    x = 0
    for i in lettersGuessed:
        if i in secretWord:
            x +=1
    if x == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    s=[]
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans=''
    for i in secretWord:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def getAvailableLetters(lettersGuessed):  
    
    ans=list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in ans: # fix valueErorr
            ans.remove(i)
    return ''.join(ans)


def main(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    
    global lettersGuessed
    mistakeMade=0
    lettersGuessed=[]
    
    while (len(secretWord) + 5) - mistakeMade > 0: # loops run on number of guesses
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            # Number of guesses increased by len of secretWord plus 5 extra guesses
            print("You have",(len(secretWord) + 5) - mistakeMade,"guesses left.") 
            print("Available letters:",getAvailableLetters(lettersGuessed))
            guess=str(input("Please guess a letter: ")).lower()
            
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
                
            elif guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
                
            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
                
        if 8 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",secretWord)
            break
        
        else:
            continue


secretWord = chooseWord(wordlist).lower()
main(secretWord)