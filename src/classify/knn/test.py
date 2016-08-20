# -*- coding: UTF-8 -*-    或者  #coding=utf-8
'''
Created on 2016年8月20日

@author: xiaoyuan
'''
import knn

group,labels = knn.createDataSet()
print knn.classify0([0,0], group, labels, 3)