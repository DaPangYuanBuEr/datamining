

from numpy import *

import operator
from matplotlib.pyplot import axis
from fileinput import filename
from frequentItemsets.apriori.test import dataset



def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines= len(arrayOLines)
    returnMat = zeros(numberOfLines,3)
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector


def autoNorm(dataset):
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataset))
    m= dataset.shape[0]
    normDataSet = dataset - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet,ranges,minVals





def classify0(inX,DataSet,labels,k):
    dataSetSize = DataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - DataSet
    sqDifMat = diffMat ** 2
    sqDistances = sqDifMat.sum(axis = 1)
    distances = sqDistances * 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]
    
    

