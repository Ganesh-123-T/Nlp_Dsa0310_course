import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = ["running", "better", "children", "mice"]

for word in words:
    print(word, "→", lemmatizer.lemmatize(word))
