training_data = [
    ('Time', 'NN'),
    ('flies', 'VBZ'),
    ('like', 'IN'),
    ('an', 'DT'),
    ('arrow', 'NN')
]

prob_model = {}
for word, tag in training_data:
    if word not in prob_model:
        prob_model[word] = tag

sentence = ["Time", "flies"]

tagged = []
for word in sentence:
    tag = prob_model.get(word, 'NN')
    tagged.append((word, tag))

print(tagged)
