import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_absolute_error

# 1.Load Dataset
data = pd.read_csv("https://github.com/venkatabhavya18/FocusHub-AI_Learning_Platform/blob/main/dataset/student_engagement_dataset.csv.xlsx")
print("Dataset Loaded Successfully")
print("Total Records:", len(data))

# 2.Focus Score Classification
# creating a simple focus label
data["focus_label"] = data["quiz_score"].apply(lambda x: 1 if x>=75 else 0)

X_focus = data[["watch_time_minutes", "pause_count" , "rewind_count", "stress_level"]]
y_focus = data["focus_label"]

X_train, X_test, y_train, y_test = train_test_split(X_focus, y_focus, test_size=0.2, random_state=42)

focus_model = LogisticRegression()
focus_model.fit(X_train, y_train)

focus_predictions = focus_model.predict(X_test)

focus_accuracy = accuracy_score(y_test, focus_predictions)

print("\n Focus Model Accuracy:", focus_accuracy)

# 3. Memory Decay Prediction
X_memory = data[["days_since_last_revision", "watch_time_minutes", "quiz_score"]]
y_memory = data["quiz_score"]

X_train, X_test, y_train_m, y_test_m = train_test_split(X_memory, y_memory, test_size=0.2, random_state=42)

memory_model = LinearRegression()
memory_model.fit(X_train_m, y_train_m)

memory_predictions = memory_model.predict(X_test_m)

memory_mae = mean_absolute_erro(y_test_m, memory_predictions)

print("Memory Decay Model MAE:", memory_mae)

print("\n Training Pipeline Completed Successfully")
