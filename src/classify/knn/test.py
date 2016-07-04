
import kNN
from classify.knn.kNN import file2matrix, autoNorm, classify0
from array import array

group,labels = kNN.createDataSet()
print kNN.classify0([0,0], group, labels, 3)







'test2'
resultList = ['not at all','in small doses','in large doses']
percentTats = float(raw_input('percentage of times spent playing video games?'))
ffMiles = float(raw_input('frequent flier miles earned per year?'))
iceCream = float(raw_input('liters of ice cream consumed per year?'))
datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
norMat,ranges,minVals = autoNorm(datingDataMat)
inArr = array([ffMiles,percentTats,iceCream])
classifierResult = classify0((inArr-minVals)/ranges,norMat,datingLabels,3)
print 'You will probably like this person:' + resultList[classifierResult - 1]



