import pandas as pd
import numpy as np
import sklearn.linear_model as lin_reg
from sklearn.model_selection import train_test_split as split

import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../btc.csv")

## Get to know the data

# Type of data is a <class 'pandas.core.frame.DataFrame'>
print(type(data))
# First 5 rows
print(data.head(5))
# Data metrics
print(data.describe())



