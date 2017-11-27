import os
import random
from Layer import Layer
from Neuron import Neuron
class InputLayer(Layer):
    
    def __init__(self):
        super(InputLayer,self).__init__()
        self.numberOfNeuronsInLayer = random.randint(1,3)
        self.listOfNeurons = []
        self.initNeuronsInLayer()
        
    def initNeuronsInLayer(self):
        i=0
        while i < self.numberOfNeuronsInLayer:
            self.listOfNeurons.append(Neuron())
            i += 1
            
    def printLayer(self):
        print('Input layer: ')
        print('number of neurons: {}'.format(self.numberOfNeuronsInLayer))
        for neuron in self.listOfNeurons:
            neuron.printNeuron()
        print('###############')
