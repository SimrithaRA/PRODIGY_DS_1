import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset 
data = pd.read_csv('/content/Real estate.csv')

#to know the dataset
data.describe
data.sample(5)

#check if there are any null values
data.isnull().sum()

# To Create a histogram
plt.hist(data['Y house price of unit area'], bins=40) 
plt.xlabel('House Price of Unit Area in Lakhs')
plt.ylabel('Frequency')
plt.title('Histogram of House Price of Unit Area ')
plt.show()

sns.histplot(data['X2 house age'])
plt.title('House Age')
plt.xlabel('House Age')
plt.ylabel('Frequency')
plt.show()

sns.histplot(data['X3 distance to the nearest MRT station'], kde=True, color='green')
plt.title('Distance to MRT Station')
plt.xlabel('Distance to MRT Station')
plt.ylabel('Frequency')
plt.show()


sns.histplot(data['X4 number of convenience stores'], kde=True, color='red')
plt.title('Number of Convenience Stores')
plt.xlabel('Number of Convenience Stores')
plt.ylabel('Frequency')
plt.show()

sns.histplot(data['X5 latitude'], kde=True, color='purple')
plt.title('Latitude')
plt.xlabel('Latitude')
plt.ylabel('Frequency')
plt.show()

sns.histplot(data['X6 longitude'], kde=True, color='orange')
plt.title('Longitude')
plt.xlabel('Longitude')
plt.ylabel('Frequency')
plt.show()

sns.histplot(data['Y house price of unit area'], kde=True, color='magenta')
plt.title('House Price of Unit Area')
plt.xlabel('House Price of Unit Area')
plt.ylabel('Frequency')
plt.show()
