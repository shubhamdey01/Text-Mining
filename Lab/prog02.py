# read from a '.pdf' file and count the number of sentences, words, and characters in the file.

from pypdf import PdfReader

# count no. of sentences
def countLines(file):
    f = PdfReader(file)
    count = 0
    for page in f.pages:
        dat = page.extract_text().split('.')
        dat.pop()
        count += len(dat)
    return count

# count no. of words
def countWords(file):
    f = PdfReader(file)
    count = 0
    for page in f.pages:
        dat = page.extract_text().split(' ')
        for i in dat:
            if i != '':
                count += 1
    return count

# count no. of characters
def countChars(file):
    f = PdfReader(file)
    count = 0
    for page in f.pages:
        dat = page.extract_text()
        for i in dat:
            if i.isalnum():
                count += 1
    return count

print('\nReading from ".pdf" file.')
print('No. of Sentences = ', countLines(r'../Files/data.pdf'))
print('No. of Words = ', countWords(r'../Files/data.pdf'))
print('No. of Characters = ', countChars(r'../Files/data.pdf'))