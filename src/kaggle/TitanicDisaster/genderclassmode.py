# -*- coding: UTF-8 -*-    或者  #coding=utf-8

'''
Created on 2016-8-23
https://www.kaggle.com/c/titanic/details/getting-started-with-python
@author: XiaoYuan1
'''
import csv as csv
import numpy as np


#读取训练数据源
csv_file_object = csv.reader(open("data/train.csv"))
header = csv_file_object.next()
data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)

#将价格分为0-10，10-20，20-30，30-40 4个区间，将价格高于40的统一成39，放在30-40范围内
fare_ceiling = 40
data[data[0::,9].astype(np.float) > fare_ceiling,9] = fare_ceiling -1.0

#计算价格区间段数
fare_bracket_size = 10
number_of_price_brackets = fare_ceiling/fare_bracket_size #共4个区间段

#计算船票类别数
number_of_classes = len(np.unique(data[0::,2]))

#构造性别、票价类别、座位类别三维数据表
survival_table = np.zeros((2,number_of_classes,number_of_price_brackets))

#按座位类别，票价范围对数据进行整理
for i in xrange(number_of_classes):
    for j in xrange(number_of_price_brackets):
        women_only_stats = data[(data[0::,4] == "female")
                                &(data[0::,2].astype(np.float) == i+1)
                                &(data[0::,9].astype(np.float)>= j * fare_bracket_size)
                                &(data[0::,9].astype(np.float)<(j+1)*fare_bracket_size)
                                ,1]
        
        men_only_stats = data[(data[0::,4] != "female")
                              &(data[0::,2].astype(np.float) == i+1)
                              &(data[0::,9].astype(np.float) >= j*fare_bracket_size)
                              &(data[0:,9].astype(np.float)<(j+1) * fare_bracket_size)
                              ,1]
        survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))
        survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))


survival_table[survival_table != survival_table] = 0


#0维表示性别、1维表示座位类别、2维表示票价格
print survival_table

survival_table[survival_table <0.5] = 0
survival_table[survival_table>0.5] =1

print survival_table


test_file = open("data/test.csv",'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()
prediction_file = open("data/genderclassmodel1.csv","wb")
p = csv.writer(prediction_file)
p.writerow(["PassengerId","Survived"])

#根据性别、座位类别、价格预计存活率
for row in test_file_object:
    for j in xrange(number_of_price_brackets):
        try:
            row[8] = float(row[8])
        except:
            bin_fare = 3- float(row[1])
            break
        if row[8] > fare_ceiling:
            bin_fare = number_of_price_brackets -1
        if( row[8] >= j* fare_bracket_size 
            and row[8] >= j*fare_bracket_size
            and (j+1) * fare_bracket_size ):
            bin_fare = j
            #break
        if(row[3] == "female"):
            p.writerow([row[0], int(survival_table[0,float(row[1]) -1,bin_fare])])
        else:
            p.writerow([row[0] , int(survival_table[1,float(row[1])-1,bin_fare])])
test_file.close()
prediction_file.close()
            
            
            
            


