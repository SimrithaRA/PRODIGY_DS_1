import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset 
data = pd.read_csv('/content/Real estate.csv')

# To Create a histogram
plt.hist(data['Y house price of unit area'], bins=40) 
plt.xlabel('House Price of Unit Area in Lakhs')
plt.ylabel('Frequency')
plt.title('Histogram of House Price of Unit Area ')
plt.show()