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
docs = []

for intents in data["intents"]:
	for patterns in intents["patterns"]
		wrds = nltk.word.tokenize(patterns)
		words.extend(wrds)
		doc.append(patterns)

	if intents["tag"] not in labels:
		label.append(intents["tag"])