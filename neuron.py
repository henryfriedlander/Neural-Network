import math, random, string

# calculate a random number a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

class Neuron(object):
	def __init__(self):
		self.sumOfWeightedInputNodes = 0
		self.inputs = [0] * 20
		self.weights = [0] * 20
		self.gradients = [0] * 20
		for i in xrange(20):
			weights.append(rand(-0.2, 0.2))

	# Sums the values and weights them
	def setWeightedInputs(self, inputs):
		self.inputs = inputs
		for i in xrange(len(inputs)):
			# dot products the inputs with the weights
			self.sumOfWeightedInputNodes += inputs[i] * weights[i]

	def synapse(self):
		return signoid(self.sumOfWeightedInputNodes)

	def setWeights(newWeights):
		self.weights = newWeights

	def setGradients(newGradients):
		this.

	def getSumOfWeightedInputesNodes():
		return self.sumOfWeightedInputNodes

class Layer(object):
	def __init__(self, numNeurons):
		self.neuronList = []
		self.numNeurons = numNeurons
		for i in xrange(numNeurons):
			neuronList.append(Neuron())

	def setInputs(self, layerInputs):
		for neuron in self.neuronList:
			neuron.setInputs(layerInputs)

	def setWeightMatrix(self, layerWeightMatrix):
		for i in xrange(len(self.neuronList)):
			self.neuronList[i].setWeights(layerWeightMatrix[i])

	def setNeuronWeight(self, weights, i):
		self.neuronList[i].setWeigts(weights)

	def propogate(self):
		results = []
		for i in xrange(self.numNeurons):
			tempNeuron = self.neuronList[i]
			tempSynapse = self.neuronList[i].synapse()
			results[i] = tempSynapse
		return results

class NeuralNetwork(object):
	def __init__(self):
		self.hiddenLayer1 = Layer(20);
		self.hiddenLayer2 = Layer(20);
		self.outputLayer = Layer(4);
		self.testInputs = [0] * 20;

	def read():
		# read stock data from KitBot as in the other githuh
		# implementation

	def run(self):
		self.selhiddenLayer1.setInputs(testInputs);
		output1 =  hiddenLayer1.propogate();
		self.hiddenLayer2.setInputs(output1);
		output2 = hiddenLayer2.propogate();
		self.outputLayer.setInputs(output2);
		results = outputLayer.propogate();

		return results

	def costFunction():
		output = 0 
		yHat = outputLayer.propogate()
		for i in xrange(4):
			output += (self.correctResults[i] - yHat[i])**2
		output/=2
		return output

	def computeOutputLayerGradients():
		output = [[]]
		y = self.correctResults
		yHat = self.outputLayer.propogate()
		y2 = self.hiddenLayer2.propogate()
		y1 = self.hiddenLayer1.propogate()
		i = self.testInputs
		for i in xrange(4):
			tempNeuron = self.outputLayer.getNeuron(i)
			tempGradients = [[]]
			for j in xrange(20):
				tempInput = tempNeuron.getInputs()
				temp = (y[i] - yHat[i]) * signoidprime(tempNeuron.getSum()) * tempInput[j]
			tempNeuron.setGradients(tempGradients)

	def computeHiddenLayer2Gradients():
		output = [[]]
		y = self.correctResults
		yHat = self.outputLayer.propogate()
		y2 = self.hiddenLayer2.propogate()
		y1 = self.hiddenLayer1.propogate()
		i = self.testInputs
		for i in xrange(20):
			tempNeuron = y2.getNeuron(i)
			tempGradients = []
			for j in xrange(20):
				for k in xrange(4):
					tempOutputLayerNeuron = self.outputLayer.getNeuron(k)
					w3 = tempOutputLayerNeuron.getWeights()
					temp = (y[k] - yHat[k]) * signoidPrime(tempOutputLayerNeuron.getSum()) * w3[k] * signoidPrime(tempNeuron.getSum()) * y1(j)
				tempGradients[j] += temp
			tempNeuron.setGradients(tempGradients)
