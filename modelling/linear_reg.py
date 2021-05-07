#LR
linear_model = LinearRegression()

scores = cross_val_score(linear_model, train_prepared, 
                         train_label, 
                         scoring = "neg_mean_squared_error", cv = 10)

linear_rmse_scores = np.sqrt(-scores)

print("Mean:", linear_rmse_scores.mean(), 
      "\nStandard deviation:", linear_rmse_scores.std())
