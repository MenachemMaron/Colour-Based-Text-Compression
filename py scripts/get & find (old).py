words = open("**path to updated words list**")
lines = words.readlines()


def getLine(file, lineNum):
    return file[lineNum]


def findValue(file, value):
    j = 0
    for i in file:
        if value == " ".join(i.split()):
            return j
        j += 1


word = str(input("Enter a word: "))
result = findValue(lines, word)
print(result if result is not None else "The word you entered is invalid.")
if result is not None:
    print(getLine(lines, result))
