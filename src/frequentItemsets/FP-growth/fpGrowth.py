 # -*- coding: utf-8 -*- 
'''
Created on 2016年6月22日

@author: xiaoyuan
'''





class treeNode:
    def __init__(self,namevalue,numOccur,parentnode):
        self.name = namevalue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentnode
        self.children = {}
            
    def inc(self,numOccur):
        self.count += numOccur
        
    def disp(self,ind=1):
        print  '' * ind,self.name,' ',self.count
        for child in self.children.values():
            child.disp(ind + 1)
            
            
#create fp tree     
def createTree(dataset,minSup=1):
    headerTable = {}
    #第一次遍历数据集，创建头指针表
    for trans in dataset:
        for item in trans:
            headerTable[item] = headerTable.get(item,0) + dataset[trans]
    #删掉不满足最小值尺度的元素项
    for k in headerTable.keys():
        if headerTable[k] < minSup:
            del(headerTable[k])  #remove k index item
    freqItemset = set(headerTable.keys())
    #空元素集，返回空
    if(len(freqItemset) == 0):
        return None,None
    #增加一个数据项，存放指向相似元素项指针
    for k in headerTable:
        headerTable[k] = [headerTable[k],None]
    retTree = treeNode('Null Set',1,None)#根节点
    #第二次遍历数据集，创建fp树
    for tranSet ,count in dataset.items():
        localD = {}
        for item in tranSet:
            if item in freqItemset:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(),key=lambda p:p[1],reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)
    return retTree,headerTable
            
     
     
     
     
def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat      
    
def createInitSet(dataset):
    retDict = {}
    for trans in dataset:
        retDict[frozenset(trans)]=1
    return retDict    
    
    
    
def updateTree(items,inTree,headerTable,count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]] = treeNode(items[0],count,inTree)
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]] 
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)
    
        

def updateHeader(nodeToTest,targetNode):
    while(nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
                    
    
    
    
    
    
    
    
    
    