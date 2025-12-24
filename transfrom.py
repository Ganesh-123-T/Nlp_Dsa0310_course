import nltk
from nltk.tag import RegexpTagger

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ly$', 'RB'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

sentence = "The dog is running fast"
tokens = sentence.split()
tagged = tagger.tag(tokens)

print(tagged)
