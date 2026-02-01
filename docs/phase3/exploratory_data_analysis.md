#Phase 3 : Exploratory Data Analysis
## 1.Introduction
Exploratory Dta Analysis (EDA) is conducted in the FocusHub system to understand leaner interaction patterns, engagement behaviour, focus trends and memory retention characteristics before building machine learning models.
This phase helps in validating feature relevance, identifying behaviour trends and preparing the system for predictive modeling.

EDA ensures the FocusHub is designed based on **data-driven insights** rather than assumptions.

## 2.Dataset Overview
Since FocusHub is a research-oriented academic project, a **synthetic learner interaction dataset** was created to simulate real-world learning behavior.
The dataset represents anonymized and randomly generated user interaction logs collected during learning sessions.
Ecah record corresponds to a learner session on the FocusHub platform.
**Key attibutes analyzed**:
- User ID
- Session duration
- Video watch precentage
- Pause and rewind frequency
- Quiz attempt score
- Time gap between learning and revision
- Session timestamps
- Device continuity indicator
This dataset enables controlled analysis of focus patterns, engagement signals and memory decay trends.
## 2.1 Tools Used for EDA
- Python
- Pandas and NumPy for data manipulation
- Matplotlib / Seaborn for visualization of trends
- Jupyter Notebook for exploratory analysis

## 3. User Interaction Distribution Analysis
User interactio data was analyzed to understand how learner consume educational content on platform.
**Analysis Findings** :
 - Most learners prefer short to medium-length study sessions.
 - High pause and rewind frequency is observed for conceptually difficult content.
 - Drop-off patterns are visible in longer videos without engagement triggers.
These findings justify the need for **adaptive content delivery and engagement monitoring** in FocusHub.

## 4. Focus Score Trend Analysis
Focus Score are derived using engagement-related features such as:
- continuous watch duration
- Interaction frequency
- Distraction indicators
**Analysis Findings**:
- Higher focus scores are strongly associated with better quiz performance.
- Focus tends to decrease after prolonged sessions without breaks.
- Learners with consistent study schedules maintain stable focus levels.
This analysis supports the design of the **Focus Score Computation Model.**

## 5. Quiz Performance Analysis
Quiz interaction data was analyzed to evaluate learning effectiveness and concept understanding.
**Analysis Findings**:
- Quiz accuracy improves when attempted immediately after focused learning sessions.
- Repeated incorrect attempts highlight concept-level knowledge gaps.
- Adaptive quiz difficulty can improve engagement and learning confidence.
These insights guide the **Adaptive Quiz and Difficulty Engine**.

## 6. Memory Decay Pattern Observation
Memory decay analysis focuses on understanding how knowledge retention changes over time.
**Analysis Findings**:
- Retention decreases as the time gap between revisions increases.
- Scheduled and periodic revisions improve long-term recall.
- Different learners exhibit different forgetting rates.
This analysis forms the basis for the **Memory Decay Prediction and Smart Revision System**.

## 7.Correlation Analysis
Correlation analysis was conceptually performed between:
- Focus Score and quiz accuracy
- Session regularity and retention rate
- Engagement behviour and learning outcomes

**Key Insight** :
Learners with higher focus stability and structured learning behaviour show improved performance and retention.

## 8. EDA Summary
The Exploratory Data Analysis phase provided critical insights into learner behviour, engagement patterns and cognitive trends.
These findings directly influenced:
- Feature selection
- Model design decisions
- System architecture refinement
EDA validates the necessity of FocusHub's AI-driven personalized learning approach. 
