import os

def getFiles():
    lst = []
    for f in os.listdir():
        if f.endswith('.txt'):
            lst.append(f)
    return lst

def index(files):
    fp = []
    for file in files:
        f = open(file, 'r')
        fp.append(f)
    dix = {}
    for i, f in enumerate(fp):
        dat = f.read().split()
        for word in dat:
            try:
                flag = True
                for j in range(len(dix[word])):
                    if dix[word][j] == i:
                        flag = False
                        break
                    elif dix[word][j] > i:
                        dix[word].insert(j, i)
                        flag = False
                        break
                if flag:
                    dix[word].append(i)
            except KeyError:
                dix[word] = [i]
    return dix

def andQuery(dix, w1, w2):
    try:
        l1 = dix[w1]
    except KeyError:
        return -1
    try:
        l2 = dix[w2]
    except KeyError:
        return -2

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

def orQuery(dix, w1, w2):
    try:
        l1 = dix[w1]
    except KeyError:
        print(f'{w1} Not Found')
        l1 = []
    try:
        l2 = dix[w2]
    except KeyError:
        print(f'{w2} Not Found')
        l2 = []

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


if __name__ == '__main__':
    files = getFiles()
    idx = index(files)
    # for i in idx:
    #     print(i, ':', idx[i])
    for i in idx:
        print(i, end=', ')
    print()

    query = input('\nEnter query: ').split()
    query[0] = query[0].lower()
    query[1] = query[1].upper()
    query[2] = query[2].lower()

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
        if not ans:
            print(f'{query[0]} OR {query[2]} Not Available.')
        else:
            print(f'{query[0]} OR {query[2]} are Available in :')
            for i in ans:
                print(files[i])
    else:
        print("Invalid")