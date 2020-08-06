def no_dups(s):# a string
    # Your code here
    if len(s) > 0:
        listVersion = s.split(' ')#change to list
        noDuplicates = {}

        for word in listVersion: #iterate through the list 
            if word  in noDuplicates.keys():
                noDuplicates[word] += 1
            else:
                noDuplicates[word] = 1
        return (" ".join(noDuplicates.keys()))# change back to string
    else:
        return ''


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
