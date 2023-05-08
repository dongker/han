import akshare as ak
import pandas as pd
from datetime import datetime

# 下载沪深300历史行情数据
df = ak.stock_zh_index_daily(symbol="sh000300")

# 更改列名
df.rename(columns={"date": "trade_date"}, inplace=True)

# 选取指定时间段内的数据
start_date = datetime.strptime("2010-01-01", "%Y-%m-%d").date()
end_date = datetime.strptime("2022-01-01", "%Y-%m-%d").date()
df = df[(df["trade_date"].apply(lambda x: datetime.strptime(str(x), "%Y-%m-%d").date()) >= start_date) & (df["trade_date"].apply(lambda x: datetime.strptime(str(x), "%Y-%m-%d").date()) < end_date)]

# 数据保存到 csv 文件
df.to_csv("hs300.csv", index=False)
