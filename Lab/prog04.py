# Implement term-document incidence matrix for boolean retrieval.

import os
import pandas as pd

def getFiles():
    lst = []
    for f in os.listdir():      # gives list of files in current directory
        if f.endswith('.txt'):  # taking only .txt files from current directory
            lst.append(f)
    return lst

# create term-document matrix
def createMatrix(files):
    fp = []     # index of this list work as documentID
    for file in files:
        f = open(file, 'r')
        fp.append(f)
    words = []  # to store unique words which acts as rows
    matrix = []
    for i, f in enumerate(fp):
        dat = f.read().split()
        for word in dat:
            if word not in words:
                words.append(word)
                matrix.append([0 for _ in range(len(fp))])
            matrix[words.index(word)][i] = 1
    return matrix, words

# display term-document matrix
def printMatrix(matrix, words, files):
    df = pd.DataFrame(matrix, columns=files, index=words)
    print(df)

# perform AND Query
def andQuery(w1, w2, matrix, words):
    try:    # gets row of word-1 if available, else error
        l1 = matrix[words.index(w1)]
        l1 = int(''.join(map(str, l1)), 2)
    except ValueError:
        return -1
    try:    # gets row of word-2 if available, else error
        l2 = matrix[words.index(w2)]
        l2 = int(''.join(map(str, l2)), 2)
    except ValueError:
        return -2
    return bin(l1 & l2)[2:]     # bitwise and

# perform OR Query
def orQuery(w1, w2, matrix, words):
    try:    # gets row of word-1 if available, else works with word-2 only
        l1 = matrix[words.index(w1)]
        l1 = int(''.join(map(str, l1)), 2)
    except ValueError:
        print(f'{w1} Not Found')
        l1 = 0
    try:    # gets row of word-2 if available, else works with word-1 only
        l2 = matrix[words.index(w2)]
        l2 = int(''.join(map(str, l2)), 2)
    except ValueError:
        print(f'{w2} Not Found')
        l2 = 0
    return bin(l1 | l2)[2:]     # bitwise or

# perform NOT Query
def notQuery(w, matrix, words):
    try:    # gets row of word if available, else gives all 0's
        l = matrix[words.index(w)]
        l = ''.join(map(str, l))
    except:
        l = '0' * len(matrix[0])
    return ''.join(['0' if i=='1' else '1' for i in l])     # complementing


if __name__ == '__main__':
    files = getFiles()
    matrix, words = createMatrix(files)

    print('\nTerm-Document Incidence Matrix: ')
    printMatrix(matrix, words, files)

    print('\nVocabulary:')
    print(words)

    print('\nTerms in lowercase & Operator in uppercase')
    query = input('Enter query: ').split()

    if len(query) == 3:
        if query[1] == 'AND':
            ans = andQuery(query[0], query[2], matrix, words)
            if type(ans) == 'str':
                ans = ans.zfill(len(matrix[0]))
            if ans == -1:
                print(f'\n{query[0]} Not Found.')
            elif ans == -2:
                print(f'\n{query[2]} Not Found.')
            elif ans == '0'*len(matrix[0]):
                print(f'\n{query[0]} AND {query[2]} Not Available.')
            else:
                print(f'\n{query[0]} AND {query[2]} are Available in :')
                for i in range(len(ans)):
                    if ans[i] == '1':
                        print(files[i])

        elif query[1] == 'OR':
                ans = orQuery(query[0], query[2], matrix, words)
                ans = ans.zfill(len(matrix[0]))
                if ans != '0'*len(matrix[0]):
                    print(f'\n{query[0]} OR {query[2]} are Available in :')
                    for i in range(len(ans)):
                        if ans[i] == '1':
                            print(files[i])                
        else:
            print("Invalid Query")
            
    elif len(query) == 2 and query[0] == 'NOT':
        ans = notQuery(query[1], matrix, words)
        if ans == '0'*len(matrix[0]):
            print(f'\n{query[1]} Available in ALL Docs.')
        else:
            print(f'\n{query[1]} is NOT Available in :')
            for i in range(len(ans)):
                if ans[i] == '1':
                    print(files[i])
    else:
        print("Invalid Query")