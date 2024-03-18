from urllib.request import urlopen

def countWords(url):
    data = urlopen(url)
    count = 0
    for line in data:
        lst = line.decode('ASCII')
        count += len(lst.split())
    return count

def countChars(url):
    data = urlopen(url)
    count = 0
    for line in data:
        for word in line.decode('ASCII').split():
            count += len(word)
    return count

# __main__
print("No. of Words = ", countWords(r"https://drive.google.com/uc?id=174j_vNuky_shWV1ggwa5uFjv3ItxtYA2"))
print("No. of Characters = ", countChars(r"https://drive.google.com/uc?id=174j_vNuky_shWV1ggwa5uFjv3ItxtYA2"))
