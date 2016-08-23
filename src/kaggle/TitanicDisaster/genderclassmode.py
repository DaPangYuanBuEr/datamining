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


fare_ceiling = 40
data[data[0::,9].astype(np.float) > fare_ceiling,9] = fare_ceiling -1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling/fare_bracket_size








