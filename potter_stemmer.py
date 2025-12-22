import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "connected", "fishing", "easily", "happiness"]

for word in words:
    print(word, "→", stemmer.stem(word))
