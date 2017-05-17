import quandl

print 'Successfully Imported Library'

stockData = quandl.get("NASDAQOMX/COMP", authtoken="8ReosziHmAyZE-zPB7zQ", returns='numpy')
print 'Successfully Retrieved Stock Data'

def getColumn(arr, index):
    col = []
    for i in xrange(len(arr)):
        if i % 50 == 0:
            print i
        col += [arr[i][2]]
    print 'done with for loop'
    return col

highData = getColumn(stockData, 2)
print highData[0]

