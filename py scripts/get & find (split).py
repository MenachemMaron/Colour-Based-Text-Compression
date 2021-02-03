import string

text = ""
exclude = set(string.punctuation)
text = "".join(ch for ch in text if ch not in exclude)


def findValue(inputFile, value):
    j = 0
    for l in inputFile:
        if value == " ".join(l.split()):
            return j
        j += 1


for i in text.split():
    file = open("**path to letters folder**"+"words-"+i[0]+".txt")
    lines = file.readlines()
    findValue(lines, i)
