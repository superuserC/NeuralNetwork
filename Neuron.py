import os
import random

class Neuron:

    def __init__(self):
        self.listOfWeightIn = []
        self.listOfWeightOut = []

        self.nbWeightIn = random.randint(1,3)
        self.nbWeightOut = random.randint(1,3)
        i=0
        while i < self.nbWeightIn:
            self.listOfWeightIn.append(random.random())
            i+=1
        i=0
        while i < self.nbWeightOut:
            self.listOfWeightOut.append(random.random())
            i+=1

    def setListOfWeightIn(self,listOfWeightIn):
        self.listOfWeightIn = listOfWeightIn

    def setListOfWeightOut(self,listOfWeightOut):
        self.listOfWeightOut = listOfWeightOut
    
    def getListOfWeightIn(self):
        return self.listOfWeightIn
    
    def getListOfWeightOut(self):
        return self.listOfWeightOut

    def printNeuron(self):
             print('nombre entrées: {}'.format(self.nbWeightIn))
             for elem in self.listOfWeightIn:
                 print('in: {}'.format(elem))
             
             print('nombre sorties: {}'.format(self.nbWeightOut))
             for elem in self.listOfWeightOut:
                 print('out: {}'.format(elem))
