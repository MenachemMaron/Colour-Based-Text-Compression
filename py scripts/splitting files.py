updatedWords = open("**path to updated words")
updatedLines = updatedWords.readlines()

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]

for l in letters:
    lettersFile = open("**path to letters folder**" + "/words-" + l + ".txt", "w")
    for i in updatedLines:
        if i[0] == l:
            lettersFile.write(i)
    lettersFile.close()