import os
import random
from Layer import Layer
from OutputLayer import OutputLayer
from InputLayer import InputLayer
from HiddenLayer import HiddenLayer

class NeuralNetwork:
    def __init__(self):
        self.inputLayer = InputLayer()
        self.outputLayer = OutputLayer()
        self.hiddenLayer = []
        self.nbHiddenLayer = random.randint(1,3)
        self.learningrate = 1
        i=0
        while i < self.nbHiddenLayer:
            self.hiddenLayer.append(HiddenLayer())
            i+=1
        self.printNeuralNetwork()


    def printNeuralNetwork(self):
        self.inputLayer.printLayer()
        self.outputLayer.printLayer()

        i=0
        while i < self.nbHiddenLayer:
            print('########Hidden layer {}'.format(i))
            self.hiddenLayer[i].printLayer()
            i+=1
            
            
