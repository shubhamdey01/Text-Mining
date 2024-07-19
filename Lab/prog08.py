# Rocchio classification using scikit-learn.

import pandas as pd
from sklearn.neighbors import NearestCentroid
from sklearn.feature_extraction.text import TfidfVectorizer

# documents
doc1 = 'Chinese Beijing Chinese'
doc2 = 'Chinese Chinese Shanghai'
doc3 = 'Chinese Macao'
doc4 = 'Tokyo Japan Chinese'

docs = [doc1, doc2, doc3, doc4]    # doc list
y = [1, 1, 1, 0]                # labels: 1=> chinese, 0=> not chinese

# displaying the training dataset
d = {'Documents': docs, 'Labels': y}
df = pd.DataFrame(d)
print('\n1=> chinese, 0=> not chinese')
print('\nTraining Dataset:\n', df)

# converting text to numeric using tf-idf
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(docs).toarray()
print('\nAfter tf-idf :\n', X)
print('\nFeatures:\n', tfidf.get_feature_names_out())

# training rocchio classifier
rocchio = NearestCentroid()
rocchio.fit(X, y)

# classifying new document
doc5 = ['Chinese Chinese Chinese Tokyo Japan']
a = tfidf.transform(doc5).toarray()

print('\nNew document: ', doc5[0])
print('Prediction: ', rocchio.predict(a)[0])