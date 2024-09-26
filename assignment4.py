import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("physics.csv")
x=df.iloc[10:20,1].values
y=df.iloc[10:20,2].values
plt.bar(x,y)
plt.show()
