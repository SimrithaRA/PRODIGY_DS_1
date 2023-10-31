# Real Estate Data Analysis with Python

This repository contains Python code for analyzing real estate data using the Pandas and Matplotlib libraries. The code loads a dataset from a CSV file and creates a histogram to visualize the distribution of house prices per unit area.

## Prerequisites

To run this code, you'll need the following software installed on your system:

- Python (version 3.0 or higher)
- Jupyter Notebook or an IDE of your choice
- Required Python libraries: Pandas and Matplotlib

## Installation

1. Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/real-estate-analysis.git
   ```

2. Navigate to the project directory:

   ```
   cd real-estate-analysis
   ```

3. Install the required Python libraries using pip:

   ```
   pip install pandas matplotlib
   ```

## Usage

1. Place your real estate data in a CSV file and save it in the project directory. Ensure that the CSV file has a column named "Y house price of unit area."
2. Ensure that the CSV file includes relevant columns, including "Y house price of unit area," "X2 house age," "X3 distance to the nearest MRT station," "X4 number of convenience stores," "X5 latitude," and "X6 longitude."
3. Open the Jupyter Notebook or your preferred IDE and run the `real_estate_analysis.ipynb` file.
4. The code will load the dataset, create a histogram, and display it in your IDE.
5. Customize the plot as needed by adjusting the number of bins, axis labels, and title.
