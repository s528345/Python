import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow as tf
import pickle
import random
import json

with open("intents.json") as file:
	data = json.load(file)

try:
	with open("data.pickle", "rb") as file:
		words, labels, training, output = pickle.load(file)

except:
	words = []
	labels = []
	docs_x = []
	docs_y = []

	# Iterating through json file
	for intents in data["intents"]:
		for patterns in intents["patterns"]:
			wrds = nltk.word_tokenize(patterns)
			words.extend(wrds)
			docs_x.append(wrds)
			docs_y.append(intents["tag"])

		if intents["tag"] not in labels:
			labels.append(intents["tag"])

	# Words sorted and to lower case in json
	words = [stemmer.stem(w.lower()) 
				for w in words 
					if w != "?"
			]
	words = sorted(List(set(words)))

	lablels = sorted(labels)

	training = []
	output = []

	out_empty = [0 for _ in range(len(labels))]

	for x, doc in enumerate(docs_x):
		bag = []

		wrds = [stemmer.stem(w) for w in doc]

		for w in words:
			if w in wrds:
				bag.append(1)
			else:
				bag.append(0)

		output_row =  out_empty[:]
		output_row[labels.index(docs_y[x])] = 1

		training.append(bag)
		ouput.append(output_row)

	training = numpy.array(training)
	output = np.array(output)

	with open("data.pickle", "wb") as file:
		pickle.dump(words, labels, training, output, file)

tf.reset_default_graph()

# Neuron Layers / Neural Network
net = tflearn.input_data(shape=[none, len(training[0])]) 					# Input data / training data
net = tflearn.fully_connected(net, 8) 					 					# Hidden layer
net = tflearn.fully_connected(net, 8)									    # Hidden layer
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")    # Output layer
net = tflearn.regression(net)

#Model to be trained
model = tflearn.out(net) 

try: 
	model.load("model.tflearn")
except:
	model.fit(training, output, n_epoch = 1000, batch_size = 8, show_metric = True)
	model.save("model.tflearn")

def bag_of_words(s, words):
	bag = [0 for _ in range(len(words))]

	s_words = nltk,word_tokenize(s)
	s_words = [stemmer.stem(word.lower()) for word in s_words]

	for x in s_words:
		for i, j in enumerate(words):
			if j == x:
				bag[i] = (1)

	return numpy.array(bag)

def chat():
	print();
	print("Start talking with the bot!")
	while True:

		you = input("You: ")
		if you.lower() == "quit":
			break

		results = model.predict([bag_of_words(you, words)])[0]
		results_index = numpy.argmax(results)
		tag = labels[results_index]

		if results[results_index] > 0.7:

			for tg in data["intents"]:
				if tg["tag"] == tag:
					responses = tg["responses"]
			print("Chatbot Response: ", random.choice(responses))

		else:
			print("I don't understand? Try again! ")

chat()