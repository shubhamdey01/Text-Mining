# read from a '.txt' file and count the number of sentences, words, and characters in the file.

# count no. of sentences
def countLines(file):
    f = open(file, 'r')
    dat = f.read().split('.')
    f.close()
    dat.pop()
    count = len(dat)
    return count

# count no. of words
def countWords(file):
    f = open(file, 'r')
    count = 0
    line = f.readline()
    while line:
        count += len(line.split())
        line = f.readline()
    f.close()
    return count

# count no. of characters
def countChars(file):
    f = open(file, 'r')
    count = 0
    line = f.readline()
    while line:
        for word in line.split():
            for i in word:
                if i.isalnum():
                    count += 1
        line = f.readline()
    f.close()
    return count

print('\nReading from ".txt" file.')
print('No. of Sentences = ', countLines(r'../Files/data.txt'))
print('No. of Words = ', countWords(r'../Files/data.txt'))
print('No. of Characters = ', countChars(r'../Files/data.txt'))