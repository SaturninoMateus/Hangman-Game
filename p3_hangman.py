# MITx 6.00 Problem Set 3
# 
# Author: Saturnino Mateus
# Contact: s.nataniel0@gmail.com
#	   saturninonataniel@gec.inatel.br

# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
	
    for i in secretWord:
		if not(i in lettersGuessed):
			return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = ''
    for i in secretWord:
		if not(i in lettersGuessed):
			result += ' _'
		else:
			result += str(i)
    return result



def getAvailableLetters(lettersGuessed):
	import string
	'''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
	result = ''
	for letter in  string.ascii_lowercase:
		if not(letter in lettersGuessed):
			result += letter
	return result
    

def hangman(secretWord):
    import string
    numOfGuesses = 8
    lettersGuessed = []
    mistakesMade = 0
    availableLetters = list(string.ascii_lowercase)
	
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    print '-------------'	
	
    while numOfGuesses - mistakesMade != 0:
        print 'You have '+str(numOfGuesses - mistakesMade)+' guesses left.'
        print 'Available letters: '+''.join(availableLetters)
        guessLetter = str(raw_input('Please guess a letter: '))
        guessLetter = guessLetter.lower()
        if guessLetter in availableLetters:
            if guessLetter in secretWord:
		lettersGuessed.append(guessLetter)
		availableLetters.remove(guessLetter)
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
                print '------------'
                if isWordGuessed(secretWord,lettersGuessed):
                    print 'Congratulations, you won!'
                    break
            else:
                availableLetters.remove(guessLetter)
                print 'Oops! That letter is not in my word: '+getGuessedWord(secretWord, lettersGuessed)
                print '------------'
                mistakesMade += 1
                if mistakesMade == numOfGuesses:
                    print 'Sorry, you ran out of guesses. The word was ' + secretWord
        else:
		  print "Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed)+"\n-------------"         

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
