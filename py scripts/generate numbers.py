letter = ""
start = 0
amount = 0

file2 = open("**path to letters folder**" + "/words-" + letter + "W.txt", "w")

# finalCount = 508300

index = 0

for i in range(0, 256):
    for j in range(0, 256):
        for l in range(0, 256):
            if start <= index < start + amount - 1:
                num1 = str(format(i, '#010b')[::-1])[:-1][:-1][::-1]
                num2 = str(format(j, '#010b')[::-1])[:-1][:-1][::-1]
                num3 = str(format(l, '#010b')[::-1])[:-1][:-1][::-1]
                file2.write(num1 + num2 + num3 + "\n")
                print(num1 + num2 + num3)
            index += 1
file2.close()
