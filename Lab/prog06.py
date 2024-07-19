# Using NLTK perform Tokenization, Normalization, Stemming & Lemmetization.

import nltk
nltk.download('punkt')      # download resources for tokenization & puntuations
nltk.download('stopwords')  # download resources for stopwords
nltk.download('wordnet')    # download resources for lemmetization

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from truecase import get_true_case
import string

# document
text = "Mr. Smith is feeling Relaxed today, as The weather in USA is awesome. Did something troubled Him in U.S.A.? The birds are flying."
print('\nDocument:\n', text)

# Sentence Tokenization
tokenized_sent = sent_tokenize(text)
print('\nSentence Tokenization:\n', tokenized_sent)

# Word Tokenization
tokenized_word = word_tokenize(text)
print('\nWord Tokenization\n', tokenized_word)

# Frequency Distribution
fdist = FreqDist(tokenized_word)
print('\nMost frequent 5 words:\n', fdist.most_common(5))

# Lowercasing
lower_token = []
for token in tokenized_word:
    lower_token.append(token.lower())
print('\nLowercasing:\n', lower_token)

# Truecasing Sentences
true_text = []
for text in tokenized_sent:
    true_text.append(get_true_case(text))
print('\nTruecasing Sentences:\n', true_text)

# Tokenize Truecase Words
true_token = []
for token in true_text:
    true_token.extend(word_tokenize(token))
print('\nTruecase Words\n', true_token)

# Removing Punctuations
punctuations = list(string.punctuation)
tokens = []
for i in lower_token:
    if i not in punctuations:
        tokens.append(i)
print('\nAfter removing Punctuations:\n', tokens)

# Removing Stopwords
stopwords_english = stopwords.words("english")
filtered_tokens=[]
for w in tokens:
    if w not in stopwords_english:
         filtered_tokens.append(w)
print('\nAfter removing Stopwords:\n', filtered_tokens)

# Stemming
ps = PorterStemmer()
stem_words=[]
for w in filtered_tokens:
     stem_words.append(ps.stem(w))
print('\nAfter Stemming:\n', stem_words)

# Lemmetization
lem = WordNetLemmatizer()
lem_words=[]
for w in filtered_tokens:
     lem_words.append(lem.lemmatize(w))
print('\nAfter Lemmetization:\n', lem_words)