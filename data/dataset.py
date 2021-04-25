!unzip california_housing.zip

housing = pd.read_csv('housing.csv')
housing.describe()

df = housing.groupby('ocean_proximity').mean().reset_index()
