import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("physics.csv")
x=df.head().iloc[:,1]
y=df.head().iloc[:,2]
plt.bar(x,y)
plt.show()



