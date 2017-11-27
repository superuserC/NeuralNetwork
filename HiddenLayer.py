import os
import random
from Layer import Layer
from Neuron import Neuron

class HiddenLayer(Layer):
    def __init__(self):
        super(HiddenLayer,self).__init__()
        self.numberOfNeuronsInLayer = random.randint(1,3)
        self.listOfNeurons = []
        self.initNeuronsInLayer()
        
    def initNeuronsInLayer(self):
        i=0
        while i < self.numberOfNeuronsInLayer:
            self.listOfNeurons.append(Neuron())
            i += 1

    def printLayer(self):
        print('Hidden layer: ')
        print('number of neurons: {}'.format(self.numberOfNeuronsInLayer))
        for neuron in self.listOfNeurons:
            neuron.printNeuron()
        print('###############')
