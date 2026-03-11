# kmeans_clustering.py

import pandas as pd
from sklearn.cluster import KMeans

def perform_kmeans(data_path):

    # Load dataset
    df = pd.read_csv(data_path)

    # Remove label column if it exists
    if "label" in df.columns:
        X = df.drop("label", axis=1)
    else:
        X = df

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["cluster"] = kmeans.fit_predict(X)

    print("KMeans clustering completed.")
    return df
