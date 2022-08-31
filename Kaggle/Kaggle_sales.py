import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("C:\\Users\\DM\Desktop\\DA\\competitive-data-science-predict-future-sales\\sales_train.csv")
shops = pd.read_csv("C:\\Users\\DM\\Desktop\\DA\\competitive-data-science-predict-future-sales\\shops.csv")
test = pd.read_csv("C:\\Users\\DM\\Desktop\\DA\\competitive-data-science-predict-future-sales\\test.csv")
items = pd.read_csv("C:\\Users\\DM\\Desktop\\DA\\competitive-data-science-predict-future-sales\\items.csv")

# print(train.corr())

train[['day','month','year']] = train['date'].str.split('.',expand = True)
month_groups = train.groupby(['month'])
# Index(['date', 'date_block_num', 'shop_id', 'item_id', 'item_price',
#        'item_cnt_day', 'day', 'month', 'year'],
#       dtype='object')
# print(month_groups['item_id'].value_counts())

# print('Types of products sold = ' ,train['item_id'].unique().size,'\n'
#       ,'Num of Shops = ',train['shop_id'].unique().size)

# ----- Find Duplicate Address -----
# print(shops['shop_name'].str.contains('Жуковский ул').sum())

# 处理shops文件，拆分出城市&商场类型
# print(shops['shop_name'].unique())
shops['shop_city'] = shops['shop_name'].map(lambda x:x.split(' ')[0].strip('!'))
shop_types = ['ТЦ', 'ТРК', 'ТРЦ', 'ТК', 'МТРЦ']
shops['shop_type'] = shops['shop_name'].map(lambda x:x.split(' ')[1] if x.split(' ')[1] in shop_types else 'Others')
shops.loc[shops['shop_id'].isin([12, 56]), ['shop_city', 'shop_type']] = 'Online'  # 12和56号是网上商店
# print(shops.head(13))

# 测试集中没有包含同一商店的不同ID， 需要对训练集重复商店的不同ID进行修改，修改的ID则以测试集为准。
shop_id_map = {11:10,0:57,1:58,40:39}
train.loc[train['shop_id'].isin(shop_id_map), 'shop_id'] = train.loc[train['shop_id'].isin(shop_id_map), 'shop_id'].map(shop_id_map)
# train_1 = pd.merge(train,shops,left_on='shop_id',right_on='shop_id')
pd.set_option('display.max_columns', 20)
# print(train_1.head(1))

# 商品数据处理
items['item_name'] = items['item_name'].map(lambda x: ''.join(x.split(' ')))  # 删除空格
duplicated_item_name = items[items['item_name'].duplicated()] # 找出重复值
items_map = pd.Series(data=items['item_category_id'],index= items['item_id'])
# train.groupby(['date'])[['item_cnt_day']].sum().plot()
# plt.show(block= True)
print(train.groupby(['date'])[['item_cnt_day']].sum().head(2))
duplicated_item_name_rec = items[items['item_name'].isin(duplicated_item_name['item_name'])]
# print(duplicated_item_name_rec) # 找出是重复值的所有id编号

# test_rec = test[test['item_id'].isin(duplicated_item_name_rec['item_id'])]
# print(test_rec['item_id'])

# -----------------------------------------

