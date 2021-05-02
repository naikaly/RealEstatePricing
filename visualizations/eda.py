#Bar Plot
housing['ocean_proximity'].value_counts().plot(kind = 'barh', color = '#C8A2C8', 
                                               title = 'Ocean Proximity', 
                             figsize = (12, 8))

#Line Plots
fig, axes = plt.subplots(nrows = 2, ncols = 2, 
                         figsize = (15, 12))
df.plot(ax = axes[0, 0], kind = 'line', 
        x = 'ocean_proximity', y = 'housing_median_age', 
                color = '#9AAB89', linewidth = 6.5, 
        title = 'Median Age of Residents')

df.plot(ax = axes[0, 1], kind = 'line', 
        x = 'ocean_proximity', y = 'total_rooms', 
                  color = '#FD5E53', linewidth = 6.5, 
   title = 'Total Rooms')

df.plot(ax = axes[1, 0], kind = 'line', 
        x = 'ocean_proximity', y = 'population', 
                  color = '#FFD700', linewidth = 6.5, 
      title = 'Population')

df.plot(ax = axes[1, 1], kind = 'line', x = 'ocean_proximity', y = 'median_income', 
               color = '#AEC6CF', linewidth = 6.5, 
    title = 'Median Income of Residents')

#Pie Plot
my_explode = (0, 0, 0.1, 0, 0)
colors_list = ['#fad6a5', '#FBCEB1', '#e9967a', '#fd5e53', '#e34234']

plt = df['median_house_value'].plot.pie(startangle = 45, 
                               autopct = '%1.1f%%', explode = my_explode, 
                                        figsize = (12, 8), colors = colors_list, labels = df.ocean_proximity, 
                                        title = 'Median Cost of House')

corr_plot = housing.corr()

# Upper triangle
mask = np.triu(np.ones_like(corr_plot, dtype = bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize = (12, 8))

sns.heatmap(corr_plot, annot = True, 
            mask = mask, cmap = 'bone')

px.scatter(housing, x = 'longitude', y = 'latitude', 
                 color = 'ocean_proximity')

# Set up the matplotlib figure
f, ax = plt.subplots(figsize = (12, 8))

sns.heatmap(pd.DataFrame(housing.isna().sum()), annot = True, 
            fmt = 'd', cmap = 'Pastel1')

plt.title('Amount Of Missing Values')
plt.show()

def calc_categorical_median(x):
    unique_colums_ocean_proximity = x['ocean_proximity'].unique()
    for i in unique_colums_ocean_proximity:
        median = x[x['ocean_proximity'] == i]['total_bedrooms'].median()
        x.loc[x['ocean_proximity'] == i,'total_bedrooms'] =  x[x['ocean_proximity'] == i]['total_bedrooms'].fillna(median)
calc_categorical_median(housing)

housing = housing.loc[df['median_house_value'] < 500001,:]
housing = housing[housing['population'] < 25000]

# converting ocean_proximity to dummies
housing = pd.concat([pd.get_dummies(housing['ocean_proximity'], 
                   drop_first = True), housing], 
        axis = 1).drop('ocean_proximity', axis = 1)

housing['income per working population'] = housing['median_income']/(housing['population'] - housing['households'])
housing['bed per house'] = housing['total_bedrooms']/housing['total_rooms']
housing['h/p'] = housing['households']/housing['population']

def type_building(x):
    if x <= 10:
        return 'new'
    
    elif x <= 30:
        return 'mid old'
    
    else:
        return 'old'

housing = pd.concat([housing, 
                     pd.get_dummies(housing['housing_median_age'].apply(type_building), 
                                             drop_first = True)], axis = 1)

x = housing.drop('median_house_value',axis=1).values
y = housing['median_house_value'].values

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.3, random_state = 0)
