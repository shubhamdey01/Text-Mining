# Implement inverted index for boolean retrieval.

import os

def getFiles():
    lst = []
    for f in os.listdir():      # gives list of files in current directory
        if f.endswith('.txt'):  # taking only .txt files from current directory
            lst.append(f)
    return lst

# create inverted index
def index(files):
    fp = []     # index of this list work as documentID
    for file in files:
        f = open(file, 'r')
        fp.append(f)
    dix = {}    # dictionary: key= terms & value= postings
    for i, f in enumerate(fp):
        dat = f.read().split()
        for word in dat:
            try:
                flag = True # doc not listed for the term
                for j in range(len(dix[word])):
                    if dix[word][j] == i:
                        flag = False # doc already listed for the term
                        break
                    elif dix[word][j] > i:
                        dix[word].insert(j, i)
                        flag = False
                        break
                if flag:
                    dix[word].append(i)
            except KeyError:
                dix[word] = [i] # inserting new term
    return dix

# perform AND Query
def andQuery(dix, w1, w2):
    try:    # get posting for word-1, else error
        l1 = dix[w1]
    except KeyError:
        return -1
    try:    # get posting for word-2, else error
        l2 = dix[w2]
    except KeyError:
        return -2

    # intersection of the two postings
    i, j = 0, 0
    lst = []
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            lst.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return lst

# perform OR Query
def orQuery(dix, w1, w2):
    try:    # get posting for word-1, else works with word-2 only
        l1 = dix[w1]
    except KeyError:
        print(f'{w1} Not Found')
        l1 = []
    try:    # get posting for word-2, else works with word-1 only
        l2 = dix[w2]
    except KeyError:
        print(f'{w2} Not Found')
        l2 = []

    # union of the two postings
    i, j = 0, 0
    lst = []
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            lst.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            lst.append(l1[i])
            i += 1
        else:
            lst.append(l2[j])
            j += 1
    while i < len(l1):
        lst.append(l1[i])
        i += 1
    while j < len(l2):
        lst.append(l2[j])
        j += 1
    return lst

# perform NOT Query
def notQuery(dix, w, N): 
    try:    # get posting for word
        l = dix[w]
    except KeyError:
        l = []
    lst = [i for i in range(N) if i not in l]
    return lst

if __name__ == '__main__':
    files = getFiles()
    idx = index(files)
    print('\nInverted Index:')
    for i in idx:
        print(i, ':', idx[i])
    print('\nVocabulary')
    for i in idx:
        print(i, end=', ')
    print()

    print('\nTerms in lowercase & Operator in uppercase')
    query = input('Enter query: ').split()

    if len(query) == 3:
        if query[1] == 'AND':
            ans = andQuery(idx, query[0], query[2])
            if ans == -1:
                print(f'{query[0]} Not Found.')
            elif ans == -2:
                print(f'{query[2]} Not Found.')
            elif not ans:
                print(f'{query[0]} AND {query[2]} Not Available.')
            else:
                print(f'{query[0]} AND {query[2]} are Available in :')
                for i in ans:
                    print(files[i])

        elif query[1] == 'OR':
            ans = orQuery(idx, query[0], query[2])
            if ans:
                print(f'{query[0]} OR {query[2]} are Available in :')
                for i in ans:
                    print(files[i])
        else:
            print("Invalid Query")
                        
    elif len(query) == 2 and query[0] == 'NOT':
        ans = notQuery(idx, query[1], len(files))
        if ans:
            print(f'{query[1]} is NOT Available in :')
            for i in ans:
                print(files[i])
        else:
            print(f'\n{query[1]}Available in ALL Docs.')
    else:
        print("Invalid Query")
