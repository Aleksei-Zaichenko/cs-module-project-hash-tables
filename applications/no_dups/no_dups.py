def no_dups(s):
    # Your code here
    if len(s) > 0:
        listVersion = s.split(' ')
        noDuplicates = {}

        for word in listVersion:
            if word  in noDuplicates.keys():
                noDuplicates[word] += 1
            else:
                noDuplicates[word] = 1
        return (" ".join(noDuplicates.keys()))
    else:
        return ''

    # if len(s) > 0:
    #     listVersion = s.split(' ')
    #     noDuplicates = []

    #     for word in listVersion:
    #         if noDuplicates.count(word) == 0:
    #             noDuplicates.append(word)
    #     return (" ".join(noDuplicates))
    # else:
    #     return ''


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
