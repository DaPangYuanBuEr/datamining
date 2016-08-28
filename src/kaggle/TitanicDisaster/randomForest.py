# -*- coding: UTF-8 -*-    或者  #coding=utf-8
'''
Created on 2016年8月28日
https://www.kaggle.com/c/titanic/details/getting-started-with-random-forests
@author: xiaoyuan
'''

#引入pandas
import pandas as pd
from pandas import  Series,DataFrame

#引入numpy,matplotlib,seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import dtype

sns.set_style("whitegrid")

#引入机器学习算法
from sklearn.linear_model import LogisticRegression
from sklearn.svm import  SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


#将训练数据和测试数据转换成dataframe
titanic_df = pd.read_csv("data/train.csv",dtype={"Age":np.float64},)
test_df = pd.read_csv("data/test.csv",dtype={"Age":np.float64},)

print titanic_df.head()

print titanic_df.info()
print ("______________________________")
print test_df.info()



titanic_df = titanic_df.drop(['PassengerId','Name','Ticket'],axis=1)
test_df = test_df.drop(['Name','Ticket'],axis=1)

titanic_df["Embarked"] = titanic_df[""]








