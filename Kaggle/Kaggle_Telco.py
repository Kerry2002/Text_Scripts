import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:\\Users\\DM\\Desktop\\WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)
pd.set_option('display.max_columns', None)
# print(df.head(1))

"""
Index(['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'],
      dtype='object')
"""

df.drop(columns = ['customerID'],axis=1, inplace= True)
# print(df.head(1))

# Churn_dis = df['Churn'].value_counts()
# print(Churn_dis)
# No     5174 Yes    1869

# _____________________________________________________________________
# gender_filter = (df['gender']=='Female')
# Female_Churn = df[gender_filter]['Churn'].value_counts()
# 用户流失性别分布分析 -- bar chart 可视化 --- 与性别关系不大
# df['Churn'] = df['Churn'].map(lambda s:1 if s=='Yes' else 0)
# df['gender'] = df['gender'].map(lambda s:1 if s=='Male' else 0)
# sns.factorplot(y='Churn',x='gender',data = df, kind = 'bar')
# plt.show(block = True)
# _____________________________________________________________________
# sns.barplot(x='SeniorCitizen', y='Churn',data = df)
# plt.show(block = True)
# 老年人的流失率明显高
# _____________________________________________________________________
# 用户使用时长分析
# print(df['tenure'].describe())
# g = sns.kdeplot(df.tenure[(df['Churn']== 'Yes')],color ='Red',shade = True)
# g = sns.kdeplot(df.tenure[(df['Churn']== 'No')],color ='Grey',shade = True)
# g.set_xlabel('Tenure')
# g.set_ylabel('Frequency')
# plt.title('Tenure vs Churn')
# g=g.legend(['Churn','NotChurn'])
# plt.show(block = True)
# 流失率在20月之前是最高的


# df['MultipleLines'].replace('No phone service','No',inplace=True)
# print(df['Contract'].value_counts())


# sns.catplot(x='Churn',y='MonthlyCharges',data = df, kind = 'box')
# plt.show(block = True)

# df['TotalCharges']= df['TotalCharges'].replace(" ",0).astype('float32')
# sns.catplot(x='Churn', y='TotalCharges',data=df, kind='boxen')
# plt.show(block = True)
# 大多数客户流失在2000元以内


# print('Both ', df.loc[(df['PhoneService']=='Yes')&(df['InternetService']!='No')].shape[0])
# print('Phone ',df.loc[(df['PhoneService']=='Yes')&(df['InternetService']=='No')].shape[0])
# print('Internet ',df.loc[(df['PhoneService']=='No')&(df['InternetService']!='No')].shape[0])

# sns.countplot(x='InternetService', hue='Churn',data = df)
# plt.show(block = True)
# 结论 -- Internet Service --> Fiber optic --> Churn

sns.countplot(x='SeniorCitizen', hue='Churn',data = df)
plt.show(block = True)

