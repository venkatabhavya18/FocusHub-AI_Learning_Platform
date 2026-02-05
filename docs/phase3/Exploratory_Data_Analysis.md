# Phase 3 : Exploratory Data Analysis

## 1.Introduction 
Exploratory Dta Analysis (EDA) was conducted in the FocusHub system to understand leaner interaction patterns, engagement behaviour, focus trends and memory retention characteristics before building machine learning models. 
This phase ensures that FocusHub is designed based on  **data-driven insights** rather than assumptions. EDA helps validate feature relevance, identifying behaviour patterns and refine cognitive modeling strategies.

## 2.Dataset Overview 
For Phase 3 implementation, a **structured synthetic dataset** containing **200 learner session records** was created. The dataset simulates anonymized student interaction logs collected during learning sessions on the FocusHub platform.
Each row represents a unique learner engagement session.

### **Key attibutes analyzed:**
- Student ID
- Session ID
- Video ID
- Watch time(minutes)
- Pause frequency
- rewind frequency
- Quiz Score
- Stress level
- Days since last revision
This dataset enables controlled analysis of focus patterns, engagement signals and memory decay behaviour.

## **3. Tools Used for EDA**
- Python
- Pandas and NumPy for data manipulation
- Matplotlib / Seaborn for visualization
- Jupyter Notebook for exploratory analysis

## 4. User Interaction Distribution Analysis 
The dataset was analyzed to understand how learners consume educational content. 
**Observations:**
- Watch time ranges between 10-60 minutes.
- Most sessions fall within moderate engagement duration.
- High pause and rewind frequency is observed in sessions with lower quiz scores.

### **Insights :**
Increased interaction events(pause/rewind) may indicate cognitive difficulty or confusion.
This jsutifies the need for adaptive content deliveru and engagement monitoring.

## 5. Focus Behaviour Analysis 
Focus-related features are derived using:
- Watch time duration
- Pause and rewind frequency
- Stress level indicators
  
### **Observations:**
- Higher watch time generally corresponds to higher quiz performance.
- Sessions with higher stress levels often show lower focus consistency.
- Balanced session durations yield better learning outcomes.

### **Insight:**
Focus stability plays a significant role in quiz accuracy and knowledge retention.This supports the design of the Focus Score Computation Model.

## 6. Quiz Performance Analysis 
Quiz interaction data was analyzed to evaluate learning effectiveness.
### **Analysis Findings:**
- Quiz scores range between 50-100
- Higher quiz scores are observed in sessions with:
  - Lower stress levels
  - Moderate watch duration
  - Lower revision gaps

### **Insight** :
Quiz performance is a strong indicator for retention modeling and adaptive difficulty implementation.

## 7. Memory Decay Pattern Analysis 
Memory decay was examined using the feature:
- Data since last revision
  
### **Observations:**
- As revision gap increases, quiz performance tends to decline.
- Regular revision correlates with better retention.
- Retention behaviour varies across learners.

### **Insight** :
 This validates the need for a Memory Decay Prediction Model within FocusHub.

## 8.Correlation Analysis 
Conceptual correlation observations include:
- Watch time (increases) -> Quiz score (increases)
- Stress level (increases) -> Quiz score (decreases)
- Revision gap (increases) -> Quiz score (decreases)
- Pause/Rewind frequency (increases) -> Stress level (increases)

### Key insight:
Learners with stable focus behaviour and structured revision patterns demonstrate improved performance and retention

## 9. EDA Summary 
The Exploratory Data Analysis phase provided critical insights into:
- Engagement behaviour
- Cognitive load indicators
- Retention patterns
- Stress-performance relationships
These insights directly influenced:
- Feature selection
- Model design decisions
- Focus score logic
- Memory decay modeling
- Adaptive quiz system
EDA validates the necessity of FocusHub's AI-driven personalized cognitive learning architecture.
