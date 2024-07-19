# Perform Parts-Of-Speech (POS) Tagging using NLTK

from nltk import word_tokenize, pos_tag

import nltk
nltk.download('averaged_perceptron_tagger')     # download resources for POS tagger

# document
sent = "Albert Einstein was born in Ulm Germany in 1879"

# tokenizing the document
tokens = word_tokenize(sent)
print('Tokens:\n', tokens)

# POS tagging
pos = pos_tag(tokens)

print('\nPOS tagging of the tokens:')
for i in pos:
    print(i)