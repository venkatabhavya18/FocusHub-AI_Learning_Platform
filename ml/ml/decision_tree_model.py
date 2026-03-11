import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_decision_tree(data_path):
    # Load dataset
    data = pd.read_csv(data_path)

    # Features and target
    # Assuming the last column is the target as per your previous logic
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Decision Tree Accuracy:", accuracy)

    return model
