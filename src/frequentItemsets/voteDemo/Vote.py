#-*-coding:utf-8-*-
'''
Created on 2016年6月21日

@author: xiaoyuan
'''



from votesmart import  votesmart


# votesmart.apikey = ""

bills = votesmart.votes.getBillsByStateRecent()


for bill in bills:
    print bill.title,bill.bid
    
