import math, random, string

# calculate a random number a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

class Neuron:
	def __init__(self):
		self.sumOfWeightedInputNodes = 0
		self.inputs = []
		self.weights = []
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


class Layer:
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

class NeuralNetwork
{
	double[] testInputs;
	Layer hiddenLayer1;
	Layer hideenLayer2;
	Layer outputLayer;

	def __init__(self):
		self.hiddenLayer1 = Layer(20);
		self.hiddenLayer2 = Layer(20);
		self.outputLayer = Layer(4);
		self.testInputs = zeros(20);

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


