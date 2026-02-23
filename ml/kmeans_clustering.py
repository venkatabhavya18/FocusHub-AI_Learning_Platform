import pandas as pd
from sklearn.cluster import KMeans

def perform_kmeans(data_path):
  df = pd.read_csv(data_path)

X = df[['watch_time','quiz_score','engagement_score']]
kmeans = KMeans(n_clusters=3, random_forest=42)
df['cluster'] = kmeans.fit_predict(X)

print("KMeans clustering completed.")
return df
