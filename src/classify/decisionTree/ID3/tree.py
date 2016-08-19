# -*- coding: UTF-8 -*-    或者  #coding=utf-8
'''
Created on 2016-8-19

@author: XiaoYuan1
'''
from math import log


'创建数据集'
def createDataSet():
    dataset = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataset,labels

'计算信息熵'
def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelCount = {}
    for featvec in dataset:
        currentLabel = featvec[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCount:
        prob = float(labelCount[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt
        
        
'划分数据集'
def splitDataSet(dataset,axis,value):
    retDataSet = []
    for featVec in dataset:
        if featVec[axis] == value :
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


'选择最好的数据集划分方式'
def chooseBestFeatureToSplit(dataset):
    numFeatures = len(dataset[0])-1
    baseEntropy = calcShannonEnt(dataset)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataset]
        uniquevals = set(featList)
        newEntropy = 0.0
        for value in uniquevals:
            subDataSet = splitDataSet(dataset, i, value)
            prob = len(subDataSet)/float(len(dataset))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain) :
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

'递归创建树'
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),classCount[2],reverse = True)


'创建树'
def createTree(dataset,labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featvalues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featvalues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataset, bestFeat, value),subLabels)
    return myTree
                
        
        
        
        
        
        
        
        
        
            