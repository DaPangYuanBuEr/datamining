'''
Created on 2016-8-19
http://blog.csdn.net/dream_angel_z/article/details/46120867
@author: XiaoYuan1
'''


from numpy import *
from numpy.core.numeric import ones
from math import log

'创建数据集'
def createDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]    
    classVec = [0,1,0,1,0,1]
    return postingList,classVec


'创建词库'
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


'统计每个样本在词库中的出现情况'
'将单个样本映射到词库中，统计单个样本在词库中出现的情况，1，表示出现过，0，表示未出现'
def setOfWords2Vex(vocabList,inputSet):
    returnVec = [0] * len(inputSet)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary" % word 
    return returnVec

def bagOfWords2VecMn(vocablist,inputset):#有的词出现多次，单个样本映射到词库的时候需要多次统计
    returnVec = [0] * len(vocablist)
    for word in inputset:
        if word in vocablist:
            returnVec[vocablist.index(word)] += 1
        return returnVec


'计算条件概率和类标签概率'
def tranNBO(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs) #某个类发生的概率
    p0Num = ones(numWords)
    p1Num = ones(numWords) #初始样本个数为1，防止条件概率为0，影响结果       
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive
    
    
'训练贝叶斯分类算法' 
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0-pClass1)
    if p1> p0 :
        return 1;
    else:
        return 0;
    



    
    
    




