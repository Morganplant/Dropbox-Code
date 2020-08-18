import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import json
import tflearn
import tensorflow
import random
import json
import pickle

import argparse

from termcolor import colored
import pprint
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--train', help='re-train the bot', action='store_true')
args = parser.parse_args()

pickle_path = "/Users/Morgan/Dropbox/Personal/Code/Python/Projects/Chat_bot/pickle/data.pickle"
model_path = "/Users/Morgan/Dropbox/Personal/Code/Python/Projects/Chat_bot/model/model.tflearn"


with open("intents.json") as file:
    data = json.load(file)

if args.train:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)

    with open(pickle_path, 'wb') as fh:
        pickle.dump((words, labels, training, output), fh)
else:
    with open(pickle_path, 'rb') as fh:
        words, labels, training, output = pickle.load(fh)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

if args.train:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save(model_path)
else:
    model.load(model_path)

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(w.lower()) for w in s_words]

    for word in s_words:
        for i, w in enumerate(words):
            if w == word:
                bag[i] = 1
    return numpy.array(bag)

def chat():
    for x in range(1000):
        print()
    print("Bot is Prepared to Talk")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        results = model.predict([bag_of_words(user_input, words)])[0]
        result_index = numpy.argmax(results)
        tag = labels[result_index]

        if results[result_index] > 0.7:
            for tg in data["intents"]:
                if tg["tag"] == tag:
                    responses = tg["responses"]

            print(colored("Bot: %s" %(random.choice(responses)), 'red'))
        else:
            print(colored("I'm sorry I didn't Quite understand", 'red'))
chat()











