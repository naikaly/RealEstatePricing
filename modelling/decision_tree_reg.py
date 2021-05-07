#DR
tree_model = DecisionTreeRegressor()

scores = cross_val_score(tree_model, train_prepared, 
                         train_label, scoring = "neg_mean_squared_error", cv = 10) 

tree_rmse_scores = np.sqrt(-scores)

print("Mean:", tree_rmse_scores.mean(), 
                      "\nStandard deviation:", tree_rmse_scores.std())
