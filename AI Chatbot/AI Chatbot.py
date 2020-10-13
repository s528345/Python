import nltk
from nltk.sten.lancaster import LancasterStemmer
stemmer = lancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json

with open("intents.json") as file
	data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

# Iterating through json file
for intents in data["intents"]:
	for patterns in intents["patterns"]
		wrds = nltk.word_tokenize(patterns)
		words.extend(wrds)
		doc_x.append(patterns)
		docs_y.append(intents["tag"])

	if intents["tag"] not in labels:
		label.append(intents["tag"])

# Words sorted and to lower case in json
words = [stemmer.stem(w.lower()) for w in words]
words = sorted(List(set(words)))

lablels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(classes))]

for x, doc in enumerate(docs_x):
	bag = []

	wrds = [stemmer.stem(w) for w in doc]

	for w in words:
		if w in wrds:
			bag.append(1)
		else:
			bag.append(0)

	output_row =  out_empty[:]
	output_row = [labels.index(docs_y[x])] = 1

	training.append(bag)
	ouput.append(output_row)

training = numoy.array(training)
output = np.array(output)