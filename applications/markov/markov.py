import random
import math

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

listOfWords = words.split()
# TODO: analyze which words can follow other words
# Your code here


startingWords = []
middleWords = []
endingWords = []

endingCharacters = ('.?!')

for word in listOfWords:
    if endingCharacters.count(word[len(word) -1]) or endingCharacters.count(word[len(word) -2]):
        endingWords.append(word)
    elif word[0].isupper() or (len(word) > 1 and word[1].isupper()):
        startingWords.append(word)
    else:   middleWords.append(word)

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    print(startingWords[random.randint(0,(len(startingWords) -1)) ], end =' ')
    for j in range (random.randint(0,(len(middleWords) -1))):
        print(middleWords[random.randint(0,(len(middleWords) -1)) ], end =' ')
    print(endingWords[random.randint(0,(len(endingWords) -1)) ])
    print('\n')
