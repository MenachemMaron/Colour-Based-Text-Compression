wordsV1 = open("**path to words file v1**")
wordsV2 = open("**path to words file v2**")
linesV1 = wordsV1.readlines()
linesV2 = wordsV2.readlines()
updatedWordsW = open("**path to updated words file**", "w")
updatedWords = open("**path to updated words file**")
updatedLines = updatedWords.readlines()


def update(value):
    for j in updatedLines:
        if " ".join(value.split()) != " ".join(j.split()):
            print(" ".join(value.split()))
            return True
    else:
        return False


for i in linesV2:
    if not update(i):
        updatedWordsW.write(i.lower())

for i in linesV1:
    if not update(i):
        updatedWordsW.write(i.lower())

updatedWordsW.close()
