import pandas as pd

def recommend_content(metadata_path, performance_level):

    print("Loading learning content metadata...")

    df = pd.read_csv(metadata_path)

    if performance_level == "low":
        recommended = df[df["difficulty"] == "Easy"]

    elif performance_level == "medium":
        recommended = df[df["difficulty"] == "Medium"]

    elif performance_level == "high":
        recommended = df[df["difficulty"] == "Hard"]

    else:
        print("Invalid performance level")
        return

    print("\nRecommended Learning Content:\n")

    for index, row in recommended.iterrows():
        print(f"Topic: {row['topic']}")
        print(f"Difficulty: {row['difficulty']}")
        print(f"Type: {row['content_type']}")
        print(f"Estimated Time: {row['estimated_time']} minutes")
        print("--------------")
