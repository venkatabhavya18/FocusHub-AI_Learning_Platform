import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def run_collaborative_filtering(data):

  user_item_matrix = data.pivot_table(index="student_id", 
                                      columns="video_id", 
                                      values="quiz_score", 
                                      fill_value=0
                                     )
  
  similarity_matrix = cosine_similarity(user_item_matrix)
  
  print("Collaborative Filtering Similarity Matrix Generated")
  return similarity_matrix
