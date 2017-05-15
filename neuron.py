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
		# read stock data from KitBot as in the other github
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

	def costFunctionPrime():
		pass

	def computeOutputLayerGradients():
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
					tempGradients[j] += (y[k] - yHat[k]) * signoidPrime(tempOutputLayerNeuron.getSum())\
					 * w3[k] * signoidPrime(tempNeuron.getSum()) * y1(j)
			tempNeuron.setGradients(tempGradients)


	def computHiddenLayer1Gradients():
		y = self.correctResults
		yHat = self.hiddenLayer2.propogate()
		y2 = self.hiddenLayer1.propogate()
		inputs = self.testInputs
		HLiter = xrange(len(self.hiddenLayer1))
		for i in HLiter:
			tempHiddenLayer1Neuron = self.hiddenLayer1.getNeuron(i)
			for j in HLiter:
				tempGradient = 0
				for k in xrange(4):
					tempOutputLayerNeuron = self.outputLayer.getNeuron(k)
					w3 = tempOutputLayerNeuron.getWeights()
					for m in HLiter:
						tempHiddenLayer2Neuron = self.hiddenLayer2.getNeuron(m)
						w2 = tempHiddenLayer2Neuron.getWeights()
						tempGradient += (y[k] - yHat[k])* signoidPrime(tempOutputLayerNeuron.getSum())\
						 * w3[m] * signoidPrime(tempHiddenLayer2Neuron.getSum()) * w2[i]\
						   * signoidPrime(tempHiddenLayer1Neuron.getSum()) * inputs[j]
				#IS THE LINE BELOW CORRECT?????
				tempGradients[j] = tempGradient + tempHiddenLayer1Neuron.getWeights(j) * self.Lambda
				# SHOULD THIS LINE BE HERE OR OUTSIDE OF THE J FOR LOOP???
				tempHiddenLayer1Neuron.setGradients(tempGradients);

		def setParams(params):
			counter = 0
			# make it easier to change number of iterations
			for i in xrange(20):
				tempHiddenLayer1Neuron = self.hiddenLayer1.getNeuron(i)
				tempNewWeights = []
				for j in xrange(20):
					counter += 1
					tempNewWeights[j] = params[counter]
				tempHiddenLayer1Neuron.setWeights(tempNewWeights)
			for k in xrange(20):
				tempHiddenLayer2Neuron = self.hiddenLayer2.getNeuron(k)
				tempNewWeights = []
				for l in xrange(20):
					counter += 1
					tempNewWeights[l] = params[counter]
				tempHiddenLayer2Neuron.setWeights(tempNewWeights)
			for m in xrange(4):
				tempOutputLayerNeuron = self.outputLayer.getNeuron(m)
				tempNewWeights = []
				for n in xrange(20):
					counter += 1
					tempNewWeights[n] = params[counter]
				tempOutputLayerNeuron.setWeights(tempNewWeights)


		'''
		def setParam(layer, numNeurons, counter):
			for i in xrange(numNeurons):
				tempLayerNeuron = layer.getNeuron(i)
				tempNewWeights = []
				for j in xrange(20):
					counter += 1
					tempNewWeights[j] = params[counter]
				tempHiddenLayer1Neuron.setWeights(tempNewWeights)
		'''
