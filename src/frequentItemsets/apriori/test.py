'''
Created on 2016-6-12

@author: XiaoYuan1
'''





import aprior

dataset = aprior.loadDataSet()
L,supportData = aprior.apriori(dataset, 0.5)
print L


rules = aprior.generateRules(L, supportData, 0.5)
