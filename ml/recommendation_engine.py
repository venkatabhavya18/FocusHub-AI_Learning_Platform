# FocusHub - Study Recommendation Engine

def recommend_topics(focus_score , topics , k=3):
  """ Recommends top-k topics based on focus score and topic priority. """

  # Adjust priority based on focus score
  for topic in topics:
    if focus_score < 40:
      topic["adjusted_priority"] = topic["difficulty"] * 0.5
    elif focus_score < 70:
      topic["adjusted_priority"] = topic["difficulty"] * 1.0
    else:
      topic["adjusted_priority"] = topic["difficulty"] * 1.5

   # Sort topics by adjusted priority(descending)
    sorted_topics = sorted( topics , key=lambda x: x["adjusted_priority"] , reverse=True)
    return sorted_topics[:k]

# Example
if __name__ == "__main__":
  focus_score = 65

topics = [ {"name": "Arrays" , "difficulty" : 3}, {"name": "Linked Lists" , "difficulty" : 4},
          {"name": "Recursion" , "difficulty" : 5}, {"name": Sorting" , "difficulty" : 2},  
            {"name": "Searching" , "difficulty" : 2}
         ]
recommendations = recommend_topics(focus_score , topic , k=3)
print("Recommended Topics:")
for topic in recommendations:
  print("-", topic["name"])
