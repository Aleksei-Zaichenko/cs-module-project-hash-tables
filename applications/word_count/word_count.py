
ignoredCharacters = ('":;,.-+=/\\|[]{}()*^&')

def word_count(s):
    dictionary = {}
    # Your code here
    listOfWords = s.lower().split()

    for word in listOfWords:
        for i in ignoredCharacters:
            if word.endswith(i):
                word = word[:len(word) - 1]
            if word.startswith(i):
                word = word[1:len(word)]
        if word != '' and word != " ":
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))