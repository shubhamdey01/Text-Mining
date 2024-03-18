def countWords(file):
    f = open(f"{file}", 'r')
    count = 0
    line = f.readline()
    while line:
        count += len(line.split())
        line = f.readline()
    f.close()
    return count

def countChars(file):
    f = open(f"{file}", 'r')
    count = 0
    line = f.readline()
    while line:
        for word in line.split():
            count += len(word)
        line = f.readline()
    f.close()
    return count

# __main__
print("No. of Words = ", countWords(r"data.txt"))
print("No. of Characters = ", countChars(r"data.txt"))
