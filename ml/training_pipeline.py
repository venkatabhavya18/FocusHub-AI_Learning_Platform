from random_forest_model import train_random_forest
from decision_tree_model import train_decision_tree
from kmeans_clustering import perform_kmeans
from collaborative_filtering import build_user_similarity_matrix
from recommendation_engine import generate_recommendations

DATA_PATH = "../dataset/student_engagement_dataset.csv"
def run_training_pipeline():
  print("-----Training Random Forest-----")
  rf_model = train_random_forest(DATA_PATH)
  
  print("\n-----Training Decision Tree-----")
  dt_model = train_Decision_tree(DATA_PATH)
  
  print("\n -----Performing KMeans Clustering-----")
  clustered_data = perform_kmeans(DATA_PATH)
  
  print("\n -----Building Collaborative Filtering-----")
  similarity_matrix = build_user_similarity_matrix(DATA_PATH)
  
  print("\n-----Generating Sample Recommendations:", recs)
  recs = generate_recommendations(user_id=1)
  
print("\n Full ML Pipeline Completed Successfully!")

if __name__ == ""__main__":
run_training_pipeline()
