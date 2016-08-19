# -*- coding: UTF-8 -*-    或者  #coding=utf-8
'''
Created on 2016-8-19

@author: XiaoYuan1

'''

import tree
import classify
from copy import copy

'创建训练数据源'
mydat,labels = tree.createDataSet()
labels2 = copy(labels)

'构建决策树'
mytree = tree.createTree(mydat, labels)
print mytree

'使用决策树模型对数据进行分类'
result = classify.classify(mytree, labels2, [1,0])
print result






