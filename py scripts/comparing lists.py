wordsV1 = open("**path to words file V1**")
wordsV2 = open("**path to words file V2**")
linesV1 = wordsV1.readlines()
linesV2 = wordsV2.readlines()
updatedWords = open("**path to updated words**")
updatedLines = updatedWords.readlines()


def update(l):
    for j in updatedLines:
        if (" ".join(l.split())).lower() == (" ".join(j.split())).lower():
            return True
    else:
        return False


for i in linesV1:
    if not update(i):
        print((" ".join(i.split())).lower())

