import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "Ganesh is learning artificial intelligence"
words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)

print(tags)
