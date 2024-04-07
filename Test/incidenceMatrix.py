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

def andQuery(w1, w2, matrix, words):
    try:
        l1 = matrix[words.index(w1)]
        l1 = int(''.join(map(str, l1)), 2)
    except ValueError:
        return -1
    try:
        l2 = matrix[words.index(w2)]
        l2 = int(''.join(map(str, l2)), 2)
    except ValueError:
        return -2
    return bin(l1 & l2)[2:]

def orQuery(w1, w2, matrix, words):
    try:
        l1 = matrix[words.index(w1)]
        l1 = int(''.join(map(str, l1)), 2)
    except ValueError:
        print(f'{w1} Not Found')
        l1 = 0
    try:
        l2 = matrix[words.index(w2)]
        l2 = int(''.join(map(str, l2)), 2)
    except ValueError:
        print(f'{w2} Not Found')
        l2 = 0
    return bin(l1 | l2)[2:]

def notQuery():
    pass

if __name__ == '__main__':
    files = getFiles()
    matrix, words = createMatrix(files)

    # printMatrix(matrix, words, files)
    # print(words)

    query = input('Enter query: ').split()
    query[0] = query[0].lower()
    query[1] = query[1].upper()
    query[2] = query[2].lower()

    if query[1] == 'AND':
        ans = andQuery(query[0], query[2], matrix, words)
        # print(ans)
        if ans == -1:
            print(f'{query[0]} Not Found.')
        elif ans == -2:
            print(f'{query[2]} Not Found.')
        elif ans == '0':
            print(f'{query[0]} AND {query[2]} Not Available.')
        else:
            print(f'{query[0]} AND {query[2]} are Available in :')
            for i in range(-1, -(len(ans)+1), -1):
                if ans[i] == '1':
                    print(files[i])
    elif query[1] == 'OR':
        ans = orQuery(query[0], query[2], matrix, words)
        if ans == '0':
            print(f'{query[0]} OR {query[2]} Not Available.')
        else:
            print(f'{query[0]} OR {query[2]} are Available in :')
            for i in range(-1, -(len(ans)+1), -1):
                if ans[i] == '1':
                    print(files[i])
    # elif query[1] == 'NOT':
    #     ans = notQuery()
    else:
        print("Invalid")
    