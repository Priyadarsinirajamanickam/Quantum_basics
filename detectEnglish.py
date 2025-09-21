# Author: Vivek Shangari

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictwords.txt')
    
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word.upper()] = None
    dictionaryFile.close()
    #print("No. of words in dictionary",len(englishWords))
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    # if possibleWords == []:
    #     return 0.0 # No words at all, so return 0.0.

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=95):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    if len(ENGLISH_WORDS) >= 400000:
        letterPercentage = 85
        lettersMatch = messageLettersPercentage >= letterPercentage
        #print("letter '%' calculated")
        return wordsMatch and lettersMatch
    else:
        #print("letter '%'  not calculated")
        return wordsMatch
    
#print(isEnglish('Me encantan las computadoras.', 95))