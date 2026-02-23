import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def train_decision_tree(data_path):
  df = pd.read_csv(data_path)
  X = df[['watch_time', 'quiz_score' , 'completion_rate']]
  y = df['engagement_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

model = DecisionTreeRegressor()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
score = r2_score(y_test, predictions)

print("Decision Tree R2 Score:", score)
return model
