import pandas as pd
# from poem import models

import pymysql

# 查询
# 连接数据库
# conn = pymysql.connect(host='localhost',
#                        user='root',
#                        passwd='sj123',
#                        db='poem_web',
#                        port=8000,
#                        charset='utf8')


data=pd.read_csv('E:\djangoProject\myweb\poem\poem.csv',header=None)
for i in data:
    print(data.iloc[i,3])



