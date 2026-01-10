# FocusHub - Training Pipeline & Data Flow
This document explains how data flows through FocusHub from user interaction to ML-driven insights.

## 1. Data Collection
- User study sessions.
- Quiz attempts and scores.
- Revision activity.
- Focus related signals (idle time , tab switching).
   Data is collected in real time during learning sessions.

## 2. Data Storage
- User Profile Dataset.
- Study Session Dataset.
- Quiz Performance Dataset.
- Revision History Dataset.

## 3.Data Processing
- Handling missing values.
- Normalizing numerical features.
- Encoding categorical variables.
- Removing noise and outliers.

## 4. Feature Engineering
- Focus score calculation.
- Memory strength estimation.
- Learning speed metrics.
- Performance trend analysis.

## 5. Model Training
Models are trained using historical learning data:
- Memory Decay Predictor.
- Focus Classification Model.
- Adaptive Difficulty Model.
- Recommendation Engine.
Training is performed periodically using batch data.

## 6. Model Evaluation
Each model is evaluated using predefined metrics:
- Accuracy , Precision , Recall.
- MAE
- Silhoutte Score
- Precision@K

## 7. Model Deployment (Prototype Level)
- Trained models are saved.
- Predictions are generated during study sessions.
- Outputs are sent to the recommendation engine.

## 8. Feedback Loop
- User interactions after recommendations are tracked.
- New data is fed back into datasets.
- Models are retrained to improve performance.

## Summary
FocusHub follows a continuous learning pipeline where user behaviour improves system intelligence over time.
