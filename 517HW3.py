import pandas as pd
import numpy as np
import scipy.stats as stats
import pylab
import matplotlib.pyplot as plt
from pandas import DataFrame
import seaborn as sns

data = pd.read_csv('/Users/maochenyi/Desktop/HY_Universe_corporate bond.csv')

#QQplot
coldata = data['LiquidityScore']
stats.probplot(coldata, dist="norm", plot=pylab)
pylab.show()

liquidity_column_index = data.columns.get_loc("LiquidityScore")
print("The 'LiquidityScore' column is at index:", liquidity_column_index)

#correlation 'LiquidityScore'and 'n_trades'
correlation = data['LiquidityScore'].corr(data['n_trades'])
print("The correlation between LiquidityScore and n_trades is:", correlation)
data.plot(kind='scatter', x='LiquidityScore', y='n_trades')
plt.title(f"Correlation: {correlation:.2f}")
plt.show()

#correlation 'LiquidityScore'and 'Coupon'
correlation = data['LiquidityScore'].corr(data['Coupon'])
print("The correlation between LiquidityScore and coupon is:", correlation)
data.plot(kind='scatter', x='LiquidityScore', y='Coupon')
plt.title(f"Correlation: {correlation:.2f}")
plt.show()

#heat map
corMat = DataFrame(data.corr())

#visualize correlations using heatmap
plot.pcolor(corMat)
plot.show()

#beeswarm plot
sns.swarmplot(x='Maturity Type',y='LiquidityScore',data = data)

print("My name is {Chenyi Mao}")
print("My NetID is: {chenyim2}")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")
