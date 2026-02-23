from random_forest_model 
import train_random_forest
from decision_tree_model
import train_decision_tree

def compare_models(data_path):
  print("Training Random Forest...")
  rf_model = train_random_forest(data_path)
  
  print("Training Decision Tree...")
  dt_model = train_decision_tree(data_path)
  
  print("Model comparision completed.")
