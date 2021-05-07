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

num_pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")),
    ('attribs_adder', pipe_f()), ('std_scaler', StandardScaler()),])

num_attribs = list(train_data_nums) 
cat_attribs = ["ocean_proximity"]

full_pipeline = ColumnTransformer([("num", num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs),])

train_prepared = full_pipeline.fit_transform(train_data)
test_prepared = full_pipeline.fit_transform(test_data)
