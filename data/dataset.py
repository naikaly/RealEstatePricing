#dataset
import pandas as pd
import numpy as np

#exploratory data analysis
import matplotlib.pyplot as plt
import plotly.express as px
%matplotlib inline
import matplotlib

#modelling
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

!unzip california_housing.zip

housing = pd.read_csv('housing.csv')
housing.describe()

df = housing.groupby('ocean_proximity').mean().reset_index()
