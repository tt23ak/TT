# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 05:18:27 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Read the Dataframe a csv file

df = pd.read_csv("C:/Users/User/Downloads/full_data_clean.csv")

#For AVG

specific_category = 'transport_type'

filtered_data = df[df['transport_type'] == specific_category]
average_value = filtered_data['transport_type'].mean()
print(average_value)

# Extract the Data from the DataFrame

x = df["transport_type"]

y =df["value"]




# Create a plot 

plt.plot(x, y, marker="o", linestyle='-', color='b', label='Data Points')

plt.title('CSV Data Plot')
plt.xlabel('TRANSPORT TYPE')
plt.ylabel('Value')

plt.legend()
plt.grid(True)

plt.show()