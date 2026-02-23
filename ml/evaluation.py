from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_model(y_test, predictions):
  mae = mean_absolute_error(y_test, predictions)
  rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("MAE:", mae)
print("RMSE:", rmse)
