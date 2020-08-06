
ingoredCharacters = ('":;,.-+=/\\|[]{}()*^&')
sentenceEnding = ('.?!')


def word_count(s):
    dictionary = {}
    # Your code here
    word = ''  # a temp variable to collect letters and make up a word

    for i in range(len(s)):
        # check if the variable should be ingored or not

        isIngored = ingoredCharacters.count(s[i])

        if isIngored == 0 and s[i] != '' and s[i] != ' ':
            word += s[i].lower()
            print('word',word,'end')
        if word != '' and word != ' ':
            if s[i] == ' ' or sentenceEnding.count(s[i]) or i == (len(s) - 1) or s[i] == '':
                print(word)
                if word in dictionary.keys():
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
                word = ''

    return dictionary


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    # print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('\ta'))
    # print('a a\ra\na\ta \t\r\n')