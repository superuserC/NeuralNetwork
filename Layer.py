import os
class Layer:

    def __init__(self):
        self.listOfNeurons = []
        self.numberOfNeuronsInLayer = 0

    def getListOfNeurons(self):
        return self.listOfNeurons

    def setListOfNeurons(self, listOfNeurons):
        self.listOfNeurons = listOfNeurons

    def getNumberOfNeuronsInLayer(self):
        return self.numberOfNeuronsInLayer

    def setNumberOfNeuronsInLayer(self,numberOfNeuronsInLayer):
        self.numberOfNeuronsInLayer = numberOfNeuronsInLayer
