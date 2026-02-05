# Phase 3 - Data Collection & Preprocessing

## Data Overview
The Student Engagement Dataset is a structured behavioural dataset designed to simulate how students interact with learning content on the **FocusHub** platfrom.
Since real-world cognitive engagement datasets are not publicly available due to privacy and ethical constraints, a **synthetic yet realistic dataset** was created based on cognitive psychology principles and real learning behaviour patterns.
This dataset captures **focus behaviour, engagement intensity, memory decay indicators, quiz performance and stress levels** during learning sessions.

## Dataset Size
- **Number of records** : 200 learning sessions
- **Number of students** : 200 (each presesnting individual engagement instances ; students may appear in multiple sessions if extended data is added later)
- **Number of features** : 9
- **Data format** : CSV (comma-seperated values)

## Features Description
**Column Name          **   |              **   Description**
student_id                  |     Unique identifier for each student (1-200)
session_id                  |     Unique learning session identifier (S1, S2, S3,..)
video_id                    |     Identifier for the learning content/video watched (1-20)
watch_time_minutes          |     Total time spent watching the video (10-60 minutes)
pause_count                 |     Number of times the student paused the video (0-6)
rewind_count                |     Number of times the student rewounded the video (0-4)
quiz_score                  |     Post-session quiz score indicating understanding (50-100)
stress_level                |     Self-estimated cognitive stress level during the session (1-5)
days_since_last_revision    |     Days since the topic was last revised (1-30)

## Data Collection Strategy
The dataset was **manually generated using controlled randomization** in Excel to reflect realistic student learning behaviour:
- Watch time varies with engagement level
- Higher pause/rewind counts reflect confusion or cognitive overload
- Quiz scores correlate with watch time and revision frequency
- Stress level increases with longer sessions and poor quiz performance
 Each formulas such as RANDBETWEEN() were used, followed by **Paste Special -> Values** to fix the data permanently.

## Data Preprocessing
Basic preprocessing steps applied:
- Ensured to missing or null values
- Maintained valid ranges for all features
- Standardized numeric columns for ML compatibility
- Verified logical consistency between engagement features and quiz scores
The dataset is clean, structured and ready for **Exploratory Data Analysis(EDA) and **Machine Learning model training**.

## Usage in FocusHub
This dataset is used for :
- Focus score prediction
- Memory decay modeling
- Engagement pattern analyis
- Adaptive quiz difficulty logic
- Recommendation engine inputs
It forms the **foundation of all cognitive intelligence components** in the FocusHub system.

## Ethical Considerations
- No real student data was used
- No personl identifiers included
- Dataset complies with privacy and academic ethics.
- Designed strictly for eduactional and research purposes.

## Conclusion
The Student Engagement Dataset enables FocusHub to simulate and analyze real-world learning behaviour in a controlled and ethical manner.
It supports explainable, lightweight ML models while aligning with the project's vision of **AI-driven personalized cognitive learning**.
