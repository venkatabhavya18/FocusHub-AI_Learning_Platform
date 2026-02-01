# FocusHub - Dataset Design
This document describes the structure of datasets used to train and evaluate ML models in FocusHub.

## 1. User Profile Dataset
Stores basic user learning information.

**Feature Name**    | **Description** 
    user_id         | Unique user identifier
  study_goal        | Daily learning target
  preferred_subject | Subject of interest
  experience_level  | Beginner / Intermediate / Advanced

## 2. Study Session Dataset
Captures user behavior during study sessions.

**Feature Name**    |  **Description**
  session_id        | Unique session identifier
  user_id           | Linked user
  topic_id          | Topic being studied
  session_duration  | Total study time
  idle_time         | Time without interaction
  tab_switch_count  | Number of tab switches
  focus_score       | Calculated focus metric

## 3. Quiz Performance Dataset
Stores quiz related performance data.

**Feature Name**    |  **Description**
quiz_id             | Quiz identifier
user_id             | Linked user
topic_id            | Topic assessed
score               | Quiz score
attempts            | Number of attempts
response_time       | Average response time

## 4. Revision History Dataset
Used for memory decay prediction
  **Feature Name**    |  **Description**
  revision_id         | Revision record ID
  user_id             | Linked user
  topic_id            | Revised topic
  last_revision_date  | Last revision time
  revision_count      | Total revisions

## Data usage summary
These datasets collectively support:
- Memory decay predictor.
- Focus score calculation.
- Adaptive learning.
- Personalized recommendations.

   
