# User Journey Flow - FocusHub

## Overview
This document describes the complete end-to-end journey of a student using FocusHub, demonstrating how verified learning content, user interaction data and machine learning models work together to create a personalized cognitive learning experience.

## Step 1 : User Entry & Authentication
- Student opens the FocusHub web platform
- User can log in for personalized learning or continue as a guest
- Logged-in users enable:
  - Progress tracking
  - Personalized recommendations
  - Learning history analysis

## Step 2 : Access to Verified Educational Content
- Students can access only learning videos uploaded by:
  - Verified faculty members
  - Approved subject experts
  - Trusted educators
- Students cannot upload learning content
- This ensures content accuracy and prevents confusion

## Step 3 : Content Discovery & Search
- Student searches for a topic or selects a subject
- System displays curriculum-aligned and verified videos only
- Video difficulty is matched to learner profile

## step 4 : Learning Session & Interaction Tracking
- Student watches the selected learning video
- System tracks engagement behaviour:
  - Watch duration
  - Pause and skip frequency
  - Idle time
  - Browser tab switching
- No camera or biometric tracking is used

## Step 5: Focus Score Computation
- Engagement signals are processed
- Focus Score is computed using ML-based logic
- Score reflects attention quality rather than total time spent

## Step 6 : Adaptive Quiz Interaction
- Quiz is triggered after the learning session
- Quiz difficulty adapts based on:
  - Focus score
  - Previous performance
- Quiz evaluates conceptual understanding

## Step 7 : Memory Decay Prediction
- Quiz results and time gaps are analyzed
- Memory decay model predicts forgetting probability
- Optimal revision timing is estimated

## Step 8 : Personalized Recommendations
- System generates learning recommendations based on :
  - Focus Score
  - Memory decay prediction
  - Quiz performance
- Recommendations include:
  - What to study next
  - When to revise
  - Appropriate difficulty level

## Step 9 : Analytics & Progress Dashboard
- Student views learning analytics including:
  - Focus trends
  - Strong and weak concepts
  - Revision schedule
- Progress visualization encourages consistent learning

## Summary
This user journey demonstrates that FocusHub is a complete AI-driven cognitive learning system that integrates verified educational content, behaviour-aware analytics and machine learning models to improve learning outcomes.
