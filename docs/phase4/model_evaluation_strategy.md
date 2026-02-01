# Model Evaluation Strategy - FocusHub
**Overview**
This document describes how the Machine Learning models used in **FocusHub** will be evaluated.
The evaluation strategy ensures that each model is accurate, reliable, explainable and suitable for an academic learning platform.
FocusHub prioritizes **lightweight and interpretable models** so that results can be clearly explained to students, faculty and reviewers.

## 1. Memory Decay Prediction Model
**Purpose**
To predict when a student is likely to forget a learned concept so that timely revision can be scheduled.
**Model Used**
- Linear Regression (time-to-forget prediction)
- Logistic Regression (forget / not-forget classification)
**Evaluation Metrics**
- **Mean Absolute Error(MAE) :** It measures how close the predicted forgetting time is to the actual forgetting time.
- **Accuracy** (for classification version) : It measures correct prediction of whether a student needs revision.
**Reason for Metric Selection**
- MAE is easy to interpret and suitable for time-based predictions.
- Accuracy provides a simple correctness measure fro binary outcomes.

## 2. Focus Score Classification Model
**Purpose**
To classify the focus level of a student during a study session(Low/Medium/High).
**Model Used**
- Logistic Regression
- Random Forest Classifier
**Evaluation Metrics**
  - **Accuracy**: Overall correctness of focus classification
  - **Precision** : It measures how many predicted focused sessions were truly focused.
  - **Recall** : It measures how many actual focused sessions were correctly identified.
**Reason for Metric Selection**
- Precision is important to avoid falsely assuming a student is focused.
- Recall ensures distracted sessions are not missed.
- Accuracy gives an overall performance mesaure.

## 3. Adaptive Quiz Difficulty Model
**Purpose**
To dynamically adjust quiz difficulty based on student performance and confidence.
**Model Used**
- Decision Tree Classifier
**Evaluation Metrics**
- Accuracy
- Confusion Matrix
**Reason for Metric Selection**
- Accuracy shows correct difficulty classification.
- Confusion Matric helps analyze incorrect difficulty transitions and model bias.

## 4. Learning Style Clustering Model
**Purpose** : To group students based on learing and engagement patterns.
**Model Used** : K-Means Clustering
**Evaluation Metrics**:
- **Silhouette Score** : It measures how well students are grouped within clusters.
- **Inertia** : It measures compactness of clusters.
**Reason for Metric Selection** :
- Silhouette Score indicates clustering quality.
- Inertia helps determine optimal number of clusters.

# 5. Recommendation Engine Evaluation
**Purpose** : To recommend the next best learning content based on user behaviour and history.
**Model Used** : Collaborative Filtering
**Evaluation Metrics** 
- **Precision@K** : It measures relevance of recommended content.
- **Recall@K** : It measures how relevant items were successfully recommended.
**Reason for Metric Selection**
- Precision@K ensures recommendations are useful.
- Recall@K ensures important learing content is not missed.

## Model Evaluation Summary
           **Model Component**          |       **Evaluation Metrics
           Memory Decay Prediction      |     MAE, Accuracy
           Focus Classification         |     Accuracy, Precision, Recall
           Quiz Difficulty Engine       |     Accurcay, Confusion Matrix
           Learning Style Clustering    |     Silhouette score, Inertia
           Recommendation Engine        |     Precision@K, Recall@K

## Conclusion
The evaluation strategy of FocusHub ensures reliable learning predictions, explainable model behaviour, academic transprency and scalable performance.
This structured evaluation framework validates the effectiveness of FocusHub's AI driven learning intelligence and prepares the system for model implementation and testing in the next phase.
