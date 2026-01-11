# FocusHub - Focus Score Calculation

def calculate_focus_score(study_time_minutes , distractions , tasks_completed):
  """ Calculates focus score based on user behaviour.
  Score range: 0-100"""
score = 100

# Penalize distrations
score -= distractions * 5

# Reward study time (max reward : 40 points)
score += min(study_time_minutes / 5,40)

# Reward task completion
score += tasks_completed * 10

# Clamp score between 0 and 100
score = max(0, min (score, 100))

return score

# Example
if __name__ == "__main__":
  focus_score = calculate_focus_score(
    study_time_minutes=90, distractions=3,tasks_completed=4
  )
  print("Focus Score:", focus_score)
