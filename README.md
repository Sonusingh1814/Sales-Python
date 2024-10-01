# Sales-python-Data-Science-Tasks

Set of real world data science tasks completed using the Python Pandas library.


# Environment Setup

To replicate and run the Sales Analysis project, the following tools and libraries are required:

Tools:
Python 3.8+: The project is written in Python, so make sure you have Python installed. 
Jupyter Notebook: A great environment for running and presenting data analysis projects. 

# Libraries:

Install the following libraries using pip:

# terminal :- pip install pandas numpy matplotlib seaborn scikit-learn

Pandas: For handling and manipulating the sales dataset

NumPy: For numerical operations

Matplotlib: For plotting graphs to visualize sales trends

Seaborn: To generate advanced visualizations

Scikit-learn: For any machine learning models you may include.

# Dataset:
Make sure the sales dataset is available in your working directory. The dataset should include fields like Order ID, Product, Quantity Ordered, Price Each, Order Date, and Purchase Address.

# Steps to Run:
1.Clone the project repository or download the project files

2.Open Jupyter Notebook and navigate to the project directory


## We start by cleaning our data. Tasks during this section include:

Drop NaN values from DataFrame

Removing rows based on a condition

Change the type of columns (to_numeric, to_datetime, astype)

## Once we have cleaned up our data a bit, we move the data exploration section. In this section we explore 5 high level business questions related to our data:

What was the best month for sales? How much was earned that month?

What city sold the most product?

What time should we display advertisemens to maximize the likelihood of customer’s buying product?

What products are most often sold together?

What product sold the most? Why do you think it sold the most?

## To answer these questions we walk through many different pandas & matplotlib methods. They include:

Concatenating multiple csvs together to create a new DataFrame (pd.concat)

Adding columns

Parsing cells as strings to make new columns (.str)

Using the .apply() method

Using groupby to perform aggregate analysis

Plotting bar charts and lines graphs to visualize our results

Labeling our graphs

