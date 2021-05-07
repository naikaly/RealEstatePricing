#RF
forest_model = RandomForestRegressor()

scores = cross_val_score(forest_model, train_prepared, 
                         train_label, scoring = "neg_mean_squared_error", 
                                                    cv = 10)

forest_rmse_scores = np.sqrt(-scores)

print("Mean:", forest_rmse_scores.mean(), 
                          "\nStandard deviation:", forest_rmse_scores.std())
