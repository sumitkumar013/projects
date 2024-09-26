import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("physics.csv")
highest_value = df['Percentage of Lectures Attended upto 31 Aug 23'].max()
highest_value_row = df[df['Percentage of Lectures Attended upto 31 Aug 23'] == highest_value]
plt.figure(figsize=(10,6))
plt.plot(df['Percentage of Lectures Attended upto 31 Aug 23' ], label='Data')
plt.title('Data with Highest Point Highlighted')
plt.xlabel('no of students')
plt.ylabel('Percentage of Lectures Attended upto 31 Aug 23')
plt.legend()
plt.grid(True)
plt.show()
