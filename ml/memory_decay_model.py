# FocusHub - Memory Decay Prediction Model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Dummy Dataset
data = {
  "days_since_last_revision": [1,2,3,5,7,10,14],
  "revision_count": [5,4,4,3,2,1,1],
  "quiz_score": [90,85,80,70,65,50,45],
  "memory_strength": [95,90,85,70,60,45,40]
}
df = pd.DataFrame(data)

# 2. Features & Target
X = df[["days_since_last_revision", "revision_count", "quiz_score"]]
y = df["memory_strength"]

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)

# 4. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate Model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", mae)

# 6. Sample Prediction
sample = [[4,3,75]]
predicted_memory = model.predict(sample)

print("Predicted Memory Strength :", predicted_memory[0])
