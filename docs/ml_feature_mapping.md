# FocusHub - ML Feature Mapping

This document explains how Machine Learning is applied to different features of the FocusHub platform.

## 1. Memory Decay Prediction.
**Goal:** Predict when a student is likely to forget a topic.
-Input Features:
  - Time since last revision.
  - Quiz accuracy.
  - Number of revisions.
-ML Approach:
  - Linear Regression / Logistic Regression.
-Output:
  - Forgetting probability.
  - Suggested revision time.

### 2. Focus Score Calculation.
-Input Features:
  - Session duration.
  - Idle time.
  - Tab switching frequency.
-ML / Logic Used:
  - Rule-based scoring + Calculation.
-Output:
  - Focus score(0-100)

### 3. Adaptive Quiz Difficulty
**Goal:** Adjust quiz difficulty based on student performance.
-Input Features:
  - Past quiz scores.
  - Response time.
  - Number of attempts.
-ML Approach:
  - Decision Trees / Classification.
-Output:
  -Easy / Medium / Hard question selection

### 4. Learning Style Detection.
**Goal:** Identify how a student learns best.
-Input Features:
  - Content interaction type.
  - Quiz performance patterns.
-ML Approach:
  - Clustering (K-Means)
-Output:
  -Learning style category

### 5. Recommendation Engine.
**Goal:** Suggest what the student should study next.
-Input Features:
  - Learning progress.
  - Focus score.
  - Memory decay output.
-ML Approach:
  - Collaborative Filtering.
-Output:
    Personalized study recommendations.

## Summary
FocusHub combines rule-based logic and classical ML models to create an intelligent and explainable learning system.
