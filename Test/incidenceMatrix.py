import os

def getFiles():
    lst = []
    for f in os.listdir():
        if f.endswith('.txt'):
            lst.append(f)
    return lst

def createMatrix(files):
    fp = []
    for file in files:
        f = open(file, 'r')
        fp.append(f)
    words = []
    matrix = []
    for i, f in enumerate(fp):
        dat = f.read().split()
        for word in dat:
            if word not in words:
                words.append(word)
                matrix.append([0 for _ in range(len(fp))])
            matrix[words.index(word)][i] = 1
    return matrix, words

def printMatrix(matrix, words, files):
    print('\t', end='\t')
    for i in files:
        print(i, end='\t')
    print()
    for i in range(len(words)):
        print(words[i], ' '*(16-len(words[i])) ,end='')
        for j in range(len(files)):
            print(matrix[i][j], end='\t\t')
        print()

def andQuery(w1, w2, matrix, words, files):
    l1 = matrix[words.index(w1)]
    l2 = matrix[words.index(w2)]
    l1 = bin(int(''.join(map(str, l1)), 2))
    print(l1)

def orQuery(w1, w2, matrix, words, files):
    pass

def notQuery():
    pass

if __name__ == '__main__':
    files = getFiles()
    matrix, words = createMatrix(files)
    # printMatrix(matrix, words, files)
    
    print(words)
    query = input('Enter query: ').split()
    if query[1] == 'AND':
        ans = andQuery(query[0], query[2], matrix, words, files)
    elif query[1] == 'OR':
        ans = orQuery(query[0], query[2], matrix, words, files)
    # elif query[1] == 'NOT':
    #     ans = notQuery()
    else:
        print("Invalid")
    