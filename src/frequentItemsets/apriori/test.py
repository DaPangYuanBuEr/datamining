'''
Created on 2016-6-12

@author: XiaoYuan1
'''





import prior

dataset = prior.loadDataSet()
L,supportData = prior.apriori(dataset, 0.5)
print L


rules = prior.generateRules(L, supportData, 0.5)
