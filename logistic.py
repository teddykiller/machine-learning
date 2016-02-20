from numpy import *

def sigmod(inX):
	return 1.0/(1+exp(inX))

def loadData():
	dataMat = []
	labelMat = []
	f = open('testSet.txt')
	for line in f.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat, labelMat

def gradAscend(dataMatIn, labelMatIn):
	dataMatrix = mat(dataMatIn)
	labelMat = mat(labelMatIn).transpose()
	m,n = shape(dataMatrix)

	alpha = 0.001
	maxCycle = 300
	weight = ones((n,1))

	for i in range(maxCycle):
		h = sigmod(dataMatrix * weight)
		error = labelMat - h
		weight = weight - alpha * dataMatrix.transpose() * error
	return weight
def plotBestFit(weight):
	weight = [float(x) for x in weight]
	print "----",weight
	import matplotlib.pyplot as plt
	dataMat, labelMat = loadData()
	dataArr = array(dataMat)
	# print 'dataArr:' , dataArr
	n = shape(dataMat)[0]
	x1 = []; y1 = []
	x0 = []; y0 = []
	for i in range(n):
		if int(labelMat[i]) == 1:
			x1.append(dataArr[i,1]), y1.append(dataArr[i,2])
		else:
			x0.append(dataArr[i,1]), y0.append(dataArr[i,2])
	print x1,y1,x0,y0
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(x1, y1, s=30, c='red')
	ax.scatter(x0, y0, s=30, c='green')
	x = arange(0, 10.0, 0.1)
	y = (-weight[0]-weight[1]*x)/weight[2]

	
	ax.plot(x,y)
	plt.show()


data, label = loadData()
weight = gradAscend(data, label)
print weight
plotBestFit(weight)



