import pandas as pd
from matplotlib import colors, pyplot as plt
# Opening Price closing price Highest price Lowest price
df = pd.read_excel("price_0050.xlsx",engine='openpyxl')
df.set_index('年月日',inplace = True)

'''
print(df.head(1)) # 查看第N列的資料
print(df.shape) #確認資料大小以tuple的型別回傳，(m, n) 表示 m 列觀測值，n 欄變數
'''

df =df.drop(columns='證券代碼',axis=1)
closing_price = df['收盤價(元)']

moving_average = closing_price.rolling(20).mean()
up = closing_price.rolling(20).mean()+closing_price.rolling(20).std()*2
down = closing_price.rolling(20).mean()-closing_price.rolling(20).std()*2

data = pd.concat([moving_average,up,down],axis=1)
data.columns = ['20MA','up','down'] 


size = df.shape[0] #取得資料長度
df = pd.concat([df,data],axis=1)
df.columns = ['open','high','low','close','20MA','up','down']



#繪圖
plt.figure()
width = 1
width2 = 0.1

#define up and down prices
up = df[df.close>=df.open]
down = df[df.close<df.open]

#define colors to use
col1 = 'red'
col2 = 'green'

#plot up prices
plt.bar(up.index,up.close-up.open,width,bottom=up.open,color=col1)
plt.bar(up.index,up.high-up.close,width2,bottom=up.close,color=col1)
plt.bar(up.index,up.low-up.open,width2,bottom=up.open,color=col1)

#plot down prices
plt.bar(down.index,down.close-down.open,width,bottom=down.open,color=col2)
plt.bar(down.index,down.high-down.open,width2,bottom=down.open,color=col2)
plt.bar(down.index,down.low-down.close,width2,bottom=down.close,color=col2)

#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')
plt.plot(df['20MA'],color='yellow')
plt.plot(df['up'],color='r')
plt.plot(df['down'],color='b')
#display candlestick chart
plt.show()