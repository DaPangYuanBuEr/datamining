# -*- coding: UTF-8 -*-    或者  #coding=utf-8
'''
Created on 2016-8-23
https://www.kaggle.com/c/titanic/details/getting-started-with-python
@author: XiaoYuan1
'''

import csv as csv
import numpy as np

csv_file_object = csv.reader(open("data/train.csv"))
header = csv_file_object.next()
data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)

print data
print data[0]  #获取data第一行
print data[-1]  #获取data最后一行
print data[1:4]  #获取data第2到第5行
print data[0,3]  #获取第1行，第4列
print data[0::,4]  #获取所有的行第4列

data[0::,2].astype(np.float)   #将所行第3列字符格式转换为float格式

'计算泰坦尼克号所有人数、幸存者数量、幸存率'
number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(float))
proportion_survived = number_survived / number_passengers
print proportion_survived

women_only_stats = data[0::,4] == "female"  #筛选出只有女性的数据
men_only_stats = data[0::,4] != "memale"  #筛选出只有男性的数据
women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print 'Proportion Of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived


test_file = open("data/test.csv")
test_file_object = csv.reader(test_file)
header = test_file_object.next()
prediction_file = open("genderbasedmodel.csv","wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerID","Survived"])
for row in test_file_object:
    if(row[3] == "female"):
        prediction_file_object.writerow([row[0],"1"])
    else :
        prediction_file_object.writerow([row[0],"0"])
test_file.close()
prediction_file.close()













