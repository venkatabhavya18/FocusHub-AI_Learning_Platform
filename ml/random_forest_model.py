import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_random_forest(data_path):

    # Load dataset
    data = pd.read_csv(data_path)

    # Features and target
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Random Forest Accuracy:", accuracy)

    return model
    
