 # -*- coding: utf-8 -*- 

'''
Created on 2016年6月22日

@author: xiaoyuan
'''


import fpGrowth


# create a tree datastructor
rootNode = fpGrowth.treeNode('pyramid',9,None)
rootNode.children['eye'] = fpGrowth.treeNode('eye',13,None)
rootNode.children['phoenix'] = fpGrowth.treeNode('phoenix',3,None)
rootNode.disp()


simDat = fpGrowth.loadSimpDat()
initSet = fpGrowth.createInitSet(simDat)
myFPtree,myHeaderTab = fpGrowth.createTree(initSet,3)
myFPtree.disp()
