import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../btc.csv")

# Draw trellis plots to find any variables that are correlated

data_subset = data[['FeeTotUSD', 'PriceUSD', 'CapMVRVCur', 'CapMrktCurUSD', 'CapRealUSD']]

sns.set(style="ticks")
g = sns.PairGrid(data_subset)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
plt.show()

data_subset = data[['HashRate', 'PriceUSD']]

sns.set(style="ticks")
g = sns.PairGrid(data_subset)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
plt.show()

data_subset = data[['BlkCnt', 'PriceUSD']]

sns.set(style="ticks")
g = sns.PairGrid(data_subset)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
plt.show()