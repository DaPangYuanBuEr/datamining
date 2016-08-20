# -*- coding: UTF-8 -*-    或者  #coding=utf-8
'''
Created on 2016年8月20日

@author: xiaoyuan
'''



from numpy import *
import operator
from Canvas import Group
from matplotlib.pyplot import axis


def createDataSet():
    Group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return Group,labels


def classify0(inX,dataset,labels,k):
    dataSetSize = dataset.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataset
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        classCount[votelabel] = classCount.get(votelabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

    