#Bar Plot
housing['ocean_proximity'].value_counts().plot(kind = 'barh', color = '#C8A2C8', 
                                               title = 'Ocean Proximity', figsize = (12, 8))

#Line Plots
fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (15, 12))
df.plot(ax = axes[0, 0], kind = 'line', x = 'ocean_proximity', y = 'housing_median_age', 
        color = '#9AAB89', linewidth = 6.5, title = 'Median Age of Residents')

df.plot(ax = axes[0, 1], kind = 'line', x = 'ocean_proximity', y = 'total_rooms', 
        color = '#FD5E53', linewidth = 6.5, 
   title = 'Total Rooms')

df.plot(ax = axes[1, 0], kind = 'line', x = 'ocean_proximity', y = 'population', 
        color = '#FFD700', linewidth = 6.5, 
      title = 'Population')

df.plot(ax = axes[1, 1], kind = 'line', x = 'ocean_proximity', y = 'median_income', 
        color = '#AEC6CF', linewidth = 6.5, 
    title = 'Median Income of Residents')

#Pie Plot
my_explode = (0, 0, 0.1, 0, 0)
colors_list = ['#fad6a5', '#FBCEB1', '#e9967a', '#fd5e53', '#e34234']

plt = df['median_house_value'].plot.pie(startangle = 45, autopct = '%1.1f%%', explode = my_explode, 
                                        figsize = (12, 8), colors = colors_list, labels = df.ocean_proximity, 
                                        title = 'Median Cost of House')

px.scatter(housing, x = 'longitude', y = 'latitude', 
                 color = 'ocean_proximity')
