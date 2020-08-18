from gtts import gTTS 
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

from termcolor import colored

import json
import nltk
import pickle
import numpy

import os



class Training(object):

    def __init__(self, json):
        self.words = []
        self.labels = []
        self.docs_x = []
        self.docs_y = []
        self.json = json
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                self.words.extend(wrds)
                self.docs_x.append(wrds)
                self.docs_y.append(intent["tag"])

            if intent["tag"] not in self.labels:
                self.labels.append(intent["tag"])

        self.words = [stemmer.stem(w.lower()) for w in self.words if w not in "?"]
        self.words = sorted(list(set(self.words)))

        self.labels = sorted(self.labels)

        self.training = []
        self.output = []

        out_empty = [0 for _ in range(len(self.labels))]
        for x, doc in enumerate(self.docs_x):
            bag = []

            wrds = [stemmer.stem(w.lower()) for w in doc]
            for w in self.words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[self.labels.index(self.docs_y[x])] = 1

            self.training.append(bag)
            self.output.append(output_row)
    
    # def save_pickle(self):
    #     with open(os.path.join(pickle_path,"data.pickle"), 'wb') as fh:
    #         pickle.dump((words, labels, training, output), fh)

with open("intents.json") as file:
    data = json.load(file)

Obj = Training(data)


training = numpy.array(Obj.training)
output = numpy.array(Obj.output)















