import random
def getRandDimensionList(dimension):
    numElements = 10
    output = []
    for i in xrange(numElements):
        output += [random.sample(range(1,100),dimension)]
    return output

def emptyList(length):
    return [[] for i in xrange(length)]

stockData = getRandDimensionList(4)
numElements = 10

print 'stockData'
print stockData

indexValues = emptyList(numElements)
highValues = emptyList(numElements)
lowValues = emptyList(numElements)
numDataPerPacket = 5

for stockIndex in xrange(len(stockData)):
    for packet in xrange(numDataPerPacket):
        if stockIndex - packet >= 0:
            stockDay = stockData[stockIndex]
            indexValues[stockIndex - packet] += [stockDay[1]]
            highValues[stockIndex - packet]  += [stockDay[2]]
            lowValues[stockIndex - packet]   += [stockDay[3]]

indexValues = indexValues[:-4]
highValues  =  highValues[:-4]
lowValues   =   lowValues[:-4]

print 'indexValues'
print indexValues

print 'highValues'
print highValues

print 'lowValues'
print lowValues

