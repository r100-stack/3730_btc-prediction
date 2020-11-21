import pandas as pd

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

data = pd.read_csv("../btc.csv")

X1 = data['HashRate']
X2 = data['FeeTotUSD']
y = data['PriceUSD']

fig = plt.figure(figsize=(8,8))
ax = Axes3D(fig)

ax.plot(X1,X2,y,zdir='z')
ax.set_xlabel("HashRate")
ax.set_ylabel("FeeTotUSD")
ax.set_zlabel("PriceUSD")
plt.show()
