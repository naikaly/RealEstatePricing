num_pipeline = Pipeline([('imputer', 
                          SimpleImputer(strategy = "median")),
    ('attribs_adder', pipe_f()), 
                         ('std_scaler', StandardScaler()),])

num_attribs = list(train_data_nums)

cat_attribs = ["ocean_proximity"]

full_pipeline = ColumnTransformer([("num", 
                                    num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs),])

train_prepared = full_pipeline.fit_transform(train_data)

test_prepared = full_pipeline.fit_transform(test_data)
