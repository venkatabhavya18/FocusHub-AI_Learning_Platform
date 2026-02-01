# FocusHub - Model Selection & Evaluation
This document describes the Machine Learning models used in FocusHub and the metrics used to evaluate them.

## 1. Memory Decay Prediction.
**Purpose:** Predict when a student is likely to forget a topic.
- Model used:
  - Linear Regression / Logistic Regression.
- Reason:
  -Simple , explainable and effective for time-based patterns.
-Evaluation:
  - Mean Absolute Error (MAE)
  - Accuracy (for classification version).

## 2. Focus Score Classification.
  **Purpose:** Classifu focus level during study sessions.
  - Model used:
    - Logistic Regression / Random forest.
  -Reason:
    - Handles behavioural features well.
  - Evaluation Metrics:
    - Accuracy.
    - Precision.
    - Recall.

## 3. Adaptive Quiz Difficulty.
**Purpose:** Adjust Quiz difficulty dynamically.
- Model used:
    - Decision Tree Classifier.
  -Reason:
    - Easy to interpret and fast.
  - Evaluation Metrics:
    - Accuracy.
    - Confusion Matrix.

## 4. Learning Style Clustering.
**Purpose:** Group students by learning behaviour.
- Model used:
    - K-Means Clustering.
  -Reason:
    - Simple and suitable for behavioural segmentation.
  - Evaluation Metrics:
    - Silhoutte Score.
    - Inertia.

## 5. Recommendation Engine.
**Purpose:** Suggest next best learning content.
- Model used:
    - Collaborative filtering.
  -Reason:
    - Personalized based on user behaviour.
  - Evaluation Metrics:
    - Precision@K.
    - Recall@K.
   
## Model Selection Summary
FocusHub prioritizes explainable and lightweight ML models to ensure transparency , performance and scalability.
