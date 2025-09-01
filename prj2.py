import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
data=pd.read_csv("C:/Users/HOME/Downloads/apple_products.csv")
print(data)
print(data.isnull().sum())
print(data.describe())
print(data.head())
#TOP 10 HIGHEST RATED IPHONE
hi_rate=data.sort_values(by=['Star Rating'],ascending=False)
hi_rate=hi_rate.head(10)
print(hi_rate['Product Name'])
#NO.OF RATING
iphone=hi_rate['Product Name'].value_counts()
label=iphone.index
counts=hi_rate["Number Of Ratings"]
figure=px.bar(hi_rate,x=label,y=counts)
figure.show()
#NO.OF REVIEWS
iphone=hi_rate['Product Name'].value_counts()
label=iphone.index
counts=hi_rate["Number Of Reviews"]
figure=px.bar(hi_rate,x=label,y=counts)
figure.show()     
#RELATIONSHIP BETWEEN NO.OF RATING AND SALE PRICE BY SCATTER GRAPH
fig=px.scatter(data_frame=data,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",trendline="ols",title="relationship between discount prize and rating",error="coerce")
fig.show()