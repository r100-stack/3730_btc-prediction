import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../btc.csv")

# Draw scatter plots to find any variables that are correlated

# As "date" is of the form, "01/01/2009", it is not graphable
# Hence, we're converting it to a int which is graphable
X = data['date'].values
for i in range(0, len(X)):
    X[i] = i
print(X)

y = data['PriceUSD'].values

# To understand how X and y look like
print(X)
print(y)

# PriceUSD vs Date
plt.scatter(X, y)
plt.title('PriceUSD vs Date')
plt.ylabel('PriceUSD')
plt.xlabel('# days after 01/03/2009')
plt.show()

# PriceUSD vs CapRealUSD
X = data['CapRealUSD'].values

plt.scatter(X, y)
plt.title('PriceUSD vs CapRealUSD')
plt.ylabel('PriceUSD')
plt.xlabel('CapRealUSD')
plt.show()

# PriceUSD vs FeeMeanUSD
X = data['FeeMeanUSD'].values

plt.scatter(X, y)
plt.title('PriceUSD vs FeeMeanUSD')
plt.ylabel('PriceUSD')
plt.xlabel('FeeMeanUSD')
plt.show()

# PriceUSD vs FeeTotUSD
X = data['FeeTotUSD'].values

plt.scatter(X, y)
plt.title('PriceUSD vs FeeTotUSD')
plt.ylabel('PriceUSD')
plt.xlabel('FeeTotUSD')
plt.show()


# PriceUSD vs FeeTotNtv
X = data['FeeTotNtv'].values

plt.scatter(X, y)
plt.title('PriceUSD vs FeeTotNtv')
plt.ylabel('PriceUSD')
plt.xlabel('FeeTotNtv')
plt.show()

# PriceUSD vs FeeMedNtv
X = data['FeeMedNtv'].values

plt.scatter(X, y)
plt.title('PriceUSD vs FeeMedNtv')
plt.ylabel('PriceUSD')
plt.xlabel('FeeMedNtv')
plt.show()

# PriceUSD vs FeeMeanNtv
X = data['FeeMeanNtv'].values

plt.scatter(X, y)
plt.title('PriceUSD vs FeeMeanNtv')
plt.ylabel('PriceUSD')
plt.xlabel('FeeMeanNtv')
plt.show()

# PriceUSD vs FeeMedUSD
X = data['FeeMedUSD'].values

plt.scatter(X, y)
plt.title('PriceUSD vs FeeMedUSD')
plt.ylabel('PriceUSD')
plt.xlabel('FeeMedUSD')
plt.show()