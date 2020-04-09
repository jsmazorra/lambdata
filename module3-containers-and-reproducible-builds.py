# DS-Unit-3-Sprint-1-Software-Engineering/module3-containers-and-reproducible-builds/

"""
File to test Docker functionality for Unit3/module3 assignment.
Set up within Docker/Ubuntu executed in python.
Simple import of a DataFrame from Unit1 and running check_null and df_splits functions.
"""

# # Installing test.pypi package
# pip install - i https: // test.pypi.org/simple / lambdata-climberalex

# Imports
#import pandas_profiling
import pandas as pd
import warnings
import sys
from functions.check_null import check_null
from functions.df_splits import df_splits
import numpy as np

# # import DataFrame
# %% capture

# # If you're on Colab:
# if 'google.colab' in sys.modules:
#     DATA_PATH = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-2-Applied-Modeling/master/data/'
#     !pip install category_encoders == 2.*

# # If you're working locally:
# else:
#     DATA_PATH = '../data/'

# # Ignore this Numpy warning when using Plotly Express:
# # FutureWarning: Method .ptp is deprecated and will be removed in a future version. Use numpy.ptp instead.
# warnings.filterwarnings(
#     action='ignore', category=FutureWarning, module='numpy')


# Read New York City property sales data
# df = pd.read_csv(DATA_PATH+'condos/NYC_Citywide_Rolling_Calendar_Sales.csv')
df = pd.read_csv('https://raw.githubusercontent.com/LambdaSchool/DS-Unit-2-Applied-Modeling/master/data/condos/NYC_Citywide_Rolling_Calendar_Sales.csv')

# Change column names: replace spaces with underscores
df.columns = [col.replace(' ', '_') for col in df]

# SALE_PRICE was read as strings.
# Remove symbols, convert to integer
df['SALE_PRICE'] = (
    df['SALE_PRICE']
    .str.replace('$', '')
    .str.replace('-', '')
    .str.replace(',', '')
    .astype(int)
)

# BOROUGH is a numeric column, but arguably should be a categorical feature,
# so convert it from a number to a string
df['BOROUGH'] = df['BOROUGH'].astype(str)

# Reduce cardinality for NEIGHBORHOOD feature

# Get a list of the top 10 neighborhoods
top10 = df['NEIGHBORHOOD'].value_counts()[:10].index

# At locations where the neighborhood is NOT in the top 10,
# replace the neighborhood with 'OTHER'
df.loc[~df['NEIGHBORHOOD'].isin(top10), 'NEIGHBORHOOD'] = 'OTHER'

print(df.shape)
df.head()


# Running check_null function
print(check_null(df))

print("------------------------")

# Running check_null function
print(df_splits(df))
