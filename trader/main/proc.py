import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("..")
from algorithm.algorithm_0 import *

# 读取 CSV 文件
df = pd.read_csv("hs300.csv")

# 提取 close 数据
close = df["close"].tolist()

# 绘制 close 曲线
#fig1 = plt.figure(1)
#plt.plot(close)
#plt.title("hs300 Curve")  # 添加标题

ONE_YEAR_TRADE_DAYS = 242

# 计算增长率并存储为文本文件
daily_grow_rata = [0] * len(close)
pos_day_cnt = 0
neg_day_cnt = 0
total_day_cnt = 0
principle_init = 100
principle_now = [0] * len(close)
win_len = ONE_YEAR_TRADE_DAYS
j=0
#for j in range(TRADE_DAYS*10):
total_money = [0] * len(close)
total_money[0] = principle_init

"""
for i in range(5*win_len, 8*win_len):
    daily_grow_rata[i] = (close[i]-close[i-1])/close[i-1] if i > 0 else 0
    principle_now[i] = algorithm_0(principle_init, daily_grow_rata[i])
    principle_init = principle_now[i]
    if(daily_grow_rata[i]>0):
        pos_day_cnt = pos_day_cnt + 1
    else:
        neg_day_cnt = neg_day_cnt + 1
    total_day_cnt = total_day_cnt + 1
"""
#income_rate = principle_now[2*win_len-1+j]/principle_now[win_len+j]
income_rate = principle_now[8*win_len-1]/((neg_day_cnt+1)*100)

#for i in range(len(close)):
#    daily_grow_rata = (close[i]-close[i-1])/close[i-1]
#    if(daily_grow_rata>0):
#            pos_day_cnt = pos_day_cnt + 1
#    else:
#        neg_day_cnt = neg_day_cnt + 1
#    total_day_cnt = total_day_cnt + 1


WINDOW_SIZE = ONE_YEAR_TRADE_DAYS
positive_ritio = (len(close)-WINDOW_SIZE-1) * [0]
for i in range(len(close)-WINDOW_SIZE-1):
    positive_ritio[i] = close[i+WINDOW_SIZE]/close[i]
    if(positive_ritio[i]>1):
            pos_day_cnt = pos_day_cnt + 1
    else:
        neg_day_cnt = neg_day_cnt + 1
    total_day_cnt = total_day_cnt + 1

fig1 = plt.figure(1)
plt.plot(positive_ritio)
plt.title("positive_ritio Curve")
plt.show()


print("positive days: %d\n" % pos_day_cnt)
print("negetive days: %d\n" % neg_day_cnt)

print("income_rate %f\n" % income_rate)
with open('../data/daily_grow_rata.txt', 'w') as f:
    for item in daily_grow_rata:
        f.write("%s\n" % item)

with open('../data/principle_now.txt', 'w') as f:
    for item in principle_now:
        f.write("%s\n" % item)

# 绘制增长率曲线，并根据值的正负选择颜色
#for i in range(len(daily_grow_rata)-1):
#    plt.plot([i,i+1], [daily_grow_rata[i], daily_grow_rata[i+1]],
#             color="green" if daily_grow_rata[i] < 0 else "red")

print("positive days ratio: %f\n" % (pos_day_cnt/total_day_cnt))
print("negetive days ratio: %f\n" % (neg_day_cnt/total_day_cnt))
# 显示图像

fig3 = plt.figure(3)
plt.plot(principle_now)
plt.title("principle_now Curve")  # 添加标题

#plt.show()
