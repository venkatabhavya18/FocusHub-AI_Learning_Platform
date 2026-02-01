# FocusHub - System Architecture

## Overview
FocusHub follows as modular AI-driven architecture where user behavior , learning data , and engagement signals are processed to generate personalized study guidance.

## High-Level Components

### 1.Frontend (User Interface)
- Web-based interface for students.
- Study sessions , quizzes , streaks and progress views.
- Displays focus score , revision reminders and rewards.

### 2.Data Collection layer
Collects non-instructive learning signals such as:
- Time spent on study sessions.
- Quiz responses and scores.
- Revision frequency.
- Focus behavior (idle time , tab switching).
  **Note : No camera , microphone or biometric data is used.

### 3.Intelligence Layer(ML + AI)
Responsible for decision-making:
- Memory Decay Predictor.
- Learning Style Detection.
- Focus Score Calculation.
- Adaptive Difficulty Engine.
- AI Study Twin simulation.

### 4.Recommendation Engine
- Suggests what to study next.
- Schedules revision sessions.
- Adjusts learning difficulty dynamically.

### 5.Storage Layer
- User learning history.
- Performance metrics.
- Progress logs.
- Security logs.

### 6.Security & Privacy Layer
- Suspicious login detection.
- Cross-device session continuity.
- Secure access handling.

## Data Flow Summary
User -> Frontend -> Data collection -> Intelligence Layer -> Recommendation Engine -> Frontend
