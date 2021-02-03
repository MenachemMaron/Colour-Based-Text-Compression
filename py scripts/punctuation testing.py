s = "hello, my name is menachem."
index = s.find(",")
if index != -1:
    s2 = list(s)
    s2 = s2[:]
    s2.insert(index, " ")
    s3 = "".join(s2)
    print(s3)

f = "hello , my name is menachem."
index2 = f.find(",")
if index != (-1 or 0):
    f2 = list(f)
    f2 = f2[:]
    f2.pop(index2-1)
    f2 = "".join(f2)
    print(f2)
