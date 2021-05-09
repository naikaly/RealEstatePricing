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

class pipe_f(BaseEstimator, TransformerMixin):
    def __init__(self, bedrooms = True):
        self.bedrooms = bedrooms
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_house = X[:, population_ix] / X[:, households_ix]
        
        if self.bedrooms:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_house,
                         bedrooms_per_room]
        
        else:
            return np.c_[X, rooms_per_household, population_house]
