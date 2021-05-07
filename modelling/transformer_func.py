#train set - 80%
train_set, test_set = train_test_split(housing, 
                                       test_size = 0.2, random_state = 42)

train_data = train_set.drop('median_house_value', 
                            axis = 1)

test_data = test_set.drop('median_house_value', 
                          axis = 1)

train_label = train_set['median_house_value'].copy()

test_label = test_set['median_house_value'].copy()

imputer = SimpleImputer(strategy = "median")

train_data_nums = train_data.drop("ocean_proximity", axis = 1)

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6
