# FocusHub - Model Design & Feature Engineering
## 1. Overview
This document describes the Machine Learning model architecture and feature engineering strategy used in FocusHub.
The goal of Phase 4 is to clearly define how user interaction data is transformed into intelligent learning recommendations using explainable ML models.

## 2. High-Level ML Architecture
The overall ML flow in FocusHub is structured as follow:
Student Interaction Data
- Data Preprocessing
- Feature Engineering
- ML models
- Recommendation Engine
- Personalized Learning Output
The system processes engagement , quiz and revision data to generate focus analysis, memory predictions and adaptive recommendations.

## 3. Feature Engineering Strategy
Feature Engineering is based on behavioural and cognitive learning indicators.

**Feature**                   |   **Used In**                      |   **Purpose**
watch_time_minutes            |   Focus Model                      |  Measures engagement duration 
pause_count                   |   Focus Model                      |  Indicates possible confusion
rewind_count                  |   Focus Model                      |  Detects learning difficulty
stress_level                  |   Performance Model                |  Affects retention & accuracy
quiz_score                    |   Performance & Adaptive Model     |  Measures understanding
days_since_last_revision      |   Memory Model                     |  Predicts forgetting probability

All numerical features are normalized before model training.
Data is split using an 80:20 train-test ratio to ensure generalization.

## 4 . Machine Learning Models Designed

### 4.1 Focus Score Model
**Type :** Logistic Regression / Rule-Based Scoring
**Purpose :** Classify student focus level during a study session.
**Input features :**
- watch_time_minutes
- pause_count
- rewind_count
- stress_level
**Output :**
- Focus Score (0-100)
- Focus Category (Low / Medium / High)
This model quantifies learner engagement behaviour.

### 4.2 Memory Decay Prediction Model
**Type :** Linear Regression
**Purpose :** Predict when a learner is likely to forget a topic
**Input Features :**
- days_since_last_revision
- quiz_score
- revision_count
**Output :**
- Forgetting probability
- Suggested revision timing
This model supports intelligent revision scheduling.

### 4.3 Performance Prediction Model
**Type :** Random Forest Regression / Decision Tree Regression
**Purpose :** Predict expected quiz performance based on engagement behaviour
**Input Features :**
- watch_time_minutes
- stress_level
- pause_count
- rewind_count
**Output :**
- Predicted quiz score
Random Forest is used for improved robustness and reduced overfitting, while Decision Tree provides interpretability for comparision.

### 4.4 Learning Behaviour Clustering Model
**Type :** K-Means Clustering
**Purpose :** Segment learners based on engagement patterns.
**Input Features :**
- watch_time_minutes
- stress_level
- pause_count
- rewind_count
**Output :**
- Learner category (e.g., High focus / Moderate / At-Risk)
This enables personalized recommendation strategies.

### 4.5 Recommendation Engine (Hybrid Logic)
**Approach :** Collaborative Filtering + Model Outputs
The recommendation engine combines:
- Focus score
- Memory decay prediction
- Performance prediction
- Learner cluster
**Output :**
- Recommended learning content
- Adaptive quiz difficulty
- Revision scheduling

## 5. Design Principles
FocusHub prioritizes:
- Explainable models
- Lightweight ML suitable for academic prototype
- Behaviour-driven personalization
- Ethical data usage (no biometric tracking)
The selected models balance performance, interpretability and academic clarity.

