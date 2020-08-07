# Your code here
ignoredCharacters = ('":;,.-+=/\\|[]{}()*^&')

with open('robin.txt') as f:
    words = f.read()

listOfWords = words.lower().split()
newListOfWords = {}

listForWordsThatOnlyOccurOnce = {}
listForWordsThatOnlyOccurMore = {}

longestWord = 0

for word in listOfWords:
    if len(word) > longestWord:
        longestWord = len(word)
    if ignoredCharacters.count(word[0]):
        word = word[1:len(word)]
    if ignoredCharacters.count(word[len(word) - 1]):
        word = word[0:(len(word) - 1)]
    if ignoredCharacters.count(word[len(word) - 1]):
        word = word[0:(len(word) - 1)]
    if word in newListOfWords:
        newListOfWords[word] += 1
    else:
        newListOfWords[word] = 1

for item in newListOfWords.items():
    if item[1] == 1:
        listForWordsThatOnlyOccurOnce[item[0]] = item[1]
    else:
        listForWordsThatOnlyOccurMore[item[0]] = item[1]

resultOfMoreThanOnce = list(listForWordsThatOnlyOccurMore.items())
resultOfMoreThanOnce.sort(key=lambda x: x[1], reverse=True)
resultOfOnce = sorted(list(listForWordsThatOnlyOccurOnce.items()))

for item in resultOfMoreThanOnce:
    print(item[0].ljust(longestWord), '\t\t', end=' ')
    for i in range(item[1]):
        print('#', end=' ')
    print('')

for item in resultOfOnce:
    print(item[0].ljust(longestWord), '\t\t', '#')
