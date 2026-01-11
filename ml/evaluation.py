# FocusHub - Recommendation Evaluation

def precision_at_k(recommended , relevant , k):
  """ 
  recommended : list of recommended item names 
  relevant : list of actually relevant item names
  k : number of top recommendations
  """
  recommended_k = recommended[:k]
  relevant_set = set(relevant)

  relevant_count = sum( 1 for item in recommended_k if item in relevant_set)
  return relevant_count / k

# Example
if __name__ == "__main__":
  recommended_topics = ["Arrays" , "Recursion" , "Sorting" , "Linked Lists"]
  relevant_topics = ["Arrays" , "Searching" , "Recursion"]

k = 3
precision = precision_at_k(recommended_topics , relevant_topics , k)
print(f"Precision@{k}:", precision)
