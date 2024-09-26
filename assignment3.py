import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("physics.csv")
x=df.tail().iloc[:,1]
y=df.tail().iloc[:,2]
plt.bar(x,y)
plt.show()
