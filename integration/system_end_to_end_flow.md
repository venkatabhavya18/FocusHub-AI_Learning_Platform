# FocusHub - End_to_End System Flow
This document explains the complete working of the FocusHub system from content creation to personalized learning output.

## 1. Content Ingestion (Verified Sources only)
- Learning videos are uploaded only by verified faculty members or approved educators
- Student-generated or unverified content upload is not allowed
- This ensures content quality, accuracy and prevents learner confusion

## 2. User Entry into the System
- Student accesses the FocusHub website
- User can:
  - Log in(for personalized learning and progress tracking)
  - Continue as guest(limited, non-persistent learning)

## 3. Learning Interaction (Video-Based Learning)
- Student searches and selects a learning video
- During video playback, the system tracks:
  - Watch duration
  - Pause and skip frequency
  - Idle time
  - Tab Switching behaviour

## 4. Focus Analysis
- Tracked interaction data is passed to the Focus Score model
- The model computes the learner's focus level
- Output :
  - Focus score (0-100)
  - Focus category (Low/Medium/High)

## 5. Knowledge Evaluation
- After learning, the student attempts a quiz
- Quiz performance data is collected:
  - Accuracy
  - Time taken
  - Attempts
- Evaluation module analyzes understanding level

## 6. Memory Decay Prediction
- Learning history and quiz performance are used
- Memory Decay model predicts:
  - Forgetting probability
  - Optimal revision time

## 7. Recommendation Generation
- Recommendation engine combines:
  - Focus score
  - Memory decay output
  - Performance evaluation
- System recommends:
  - Revision videos
  - Next learning topic
  - Adaptive quiz difficulty

## 8. Analytics & Feedback
- Results are displayed on the dashboard:
 - Focus trends
 - Memory retention indicators
 - Learning progress
-Gamification elements encourage consistent learning

## 9. Security & Integrity (Conceptual)
- Login behavior is monitored
- Suspicious patterns can be flagged
- Cross-device learning continuity is supported

## 10. System Scope
- ML logic and integration are implemented at prototype level
- Backend services and deployment are planned as future enhancements


  FocusHub functions as a congintive learning intelligence system, not merely a content delivery platform.
