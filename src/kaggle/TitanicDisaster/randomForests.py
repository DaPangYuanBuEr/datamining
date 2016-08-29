# -*- coding: UTF-8 -*-    或者  #coding=utf-8
'''
Created on 2016-8-29
https://www.kaggle.com/jeffd23/titanic/scikit-learn-ml-from-start-to-finish
@author: XiaoYuan1
'''
#思路：随机选择训练数据子集训练不同的数据集，形成森林后，对测试数据集的数据进行测试

#引入pandas
import  pandas as pd
from pandas import Series,DataFrame

#引入numpy，matplotlib，seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.pylabtools import figsize
sns.set_style("whitegrid")

#引入机器学习包
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


#导入训练数据和测试数据
titanic_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")
print titanic_df.head(2)  #返回前2行数据

print titanic_df.info()
print test_df.info()



#删除无用的列
titanic_df = titanic_df.drop(['PassengerId','Name','Ticket'],axis=1)
print titanic_df.head(1)

#分析Embarked字段
#使用众数S填充Embarked列空值,Embarked表示上船的位置
titanic_df["Embarked"] = titanic_df["Embarked"].fillna("S")

sns.factorplot('Embarked', 'Survived',data=titanic_df,  size = 4, aspect=3)
fig,(axis1,axis2,axis3) = plt.subplots(1,3,figsize=(15,5))

sns.countplot(x="Embarked", data=titanic_df,  ax=axis1)
sns.countplot(x="Survived",hue="Embarked",data=titanic_df,order=[1,0],ax = axis2)

embark_perc = titanic_df[["Embarked","Survived"]].groupby(['Embarked'],as_index=False).mean()
sns.barplot(x='Embarked', y='Survived', data=embark_perc,order=['S','C','Q'],ax=axis3)


embark_dummies_titanic = pd.get_dummies(titanic_df['Embarked'])#将Embarked的C\Q\S变为1,0,0\0,1，0\0，0,1的形式
print embark_dummies_titanic.head(5)
embark_dummies_titanic.drop(["S"],axis=1,inplace=True)


embark_dummies_test = pd.get_dummies(titanic_df["Embarked"])
embark_dummies_test.drop(["S"],axis=1,inplace=True)

titanic_df = titanic_df.join(embark_dummies_titanic)
test_df = test_df.join(embark_dummies_test)

print test_df.head(5)

titanic_df.drop(["Embarked"],axis=1,inplace=True)
test_df.drop(["Embarked"],axis=1,inplace=True)

#————————————————————————————————————————————————————————————————————————
#分析Fare字段
test_df['Fare'].fillna(test_df["Fare"].median(),inplace = True)#将测试数据源中的空值使用中位数进行填充
titanic_df["Fare"] = titanic_df["Fare"].astype(int) #将float类型转为int类型
test_df["Fare"] = test_df["Fare"].astype(int)

fare_not_survived = titanic_df["Fare"][titanic_df["Survived"]==0]
fare_survived = titanic_df["Fare"][titanic_df["Survived"] == 1]

avgerage_fare = DataFrame([fare_not_survived.mean(),fare_survived.mean()])#计算存活/未存活乘客票价平均数和标准差
std_fare = DataFrame([fare_not_survived.std(),fare_survived.std()])
plt.figure(1)

plt.figure(2)

titanic_df['Fare'].plot(kind='hist', figsize=(15,3),bins=100, xlim=(0,50))

avgerage_fare.index.names = std_fare.index.names = ["Survived"]
avgerage_fare.plot(yerr=std_fare,kind="bar",legend = False)




plt.show()



#-----------------------------随机决策树————————————————————

X_train = titanic_df.drop("Survived",axis =1)
Y_train = titanic_df["Survived"]
X_test = test_df.drop("PassengerId",axis =1).copy()

#Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_test,Y_train)
Y_pred = logreg.pre(X_test)
print logreg.score(X_train, Y_train)

#Support Vector Machines
svc = SVC()
svc.fit(X_test,Y_train)
Y_pred = svc.predict(X_test)
print svc.score(X_train,Y_train)

#Random Forests
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train,Y_train)
Y_pred = random_forest.predict(X_test)
print random_forest.score(X_train,Y_train)

coeff_df = DataFrame(titanic_df.columns.delete(0))
coeff_df.columns = ["Features"]
coeff_df["Coefficient Estimate"] = pd.Series(logreg.coef_[0])

print coeff_df







































