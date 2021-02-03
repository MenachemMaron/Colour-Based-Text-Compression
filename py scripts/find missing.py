import string

wordsV1 = open("**path to words V1**")
wordsV2 = open("**path to words V2")
linesV1 = wordsV1.readlines()
linesV2 = wordsV2.readlines()
updatedWords = open("**path to updated words**")
updatedLines = updatedWords.readlines()

testing = "**testing text goes here**"


def findValue(file, value):
    j = 0
    for i in file:
        if value == " ".join(i.split()):
            return j
        j += 1


def testList(wordsList, wordsList2, wordsList3, text):
    exclude = set(string.punctuation)
    text = "".join(ch for ch in text if ch not in exclude)
    for word in text.split():
        print(word.lower())
        if (findValue(wordsList, word.lower())) is None:
            if (findValue(wordsList2, word.lower())) is None:
                print(False)
            else:
                print(True)
        else:
            print(True)
        if findValue(wordsList3, word.lower()) is None:
            print(False)
        else:
            print(True)


testList(linesV1, linesV2, updatedLines, testing)
