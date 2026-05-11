import pandas as pd
from pathlib import Path
import numpy as np
BASE_DIR = Path(__file__).resolve().parent

items_df = pd.read_csv(BASE_DIR / "items.csv")
interactions_df = pd.read_csv(BASE_DIR / "interactions.csv")

tag_set = set()
for tags in items_df["tags"]:
    for tag in tags.split("|"):
        tag_set.add(tag)

tag_list = sorted(tag_set)

tag_index = {}
for index, tag in enumerate(tag_list):
    tag_index[tag] = index

tag_vectors = {}
for index, row in items_df.iterrows():
    item_id = row["item_id"]
    vector = np.zeros(len(tag_list))
    for tag in row["tags"].split("|"):
        index = tag_index[tag]
        vector[index] = 1
    
    tag_vectors[item_id] = vector

EVENT_WEIGHTS = {
    "view": 1.0,
    "like": 3.0,
    "purchase": 5.0
}

def build_user_vector(user_id):
    user_interactions = interactions_df[interactions_df["user_id"] == user_id]
    user_vector = np.zeros(len(tag_list))
    for _, _, item_id, event_type in user_interactions.itertuples():
        user_vector += EVENT_WEIGHTS[event_type] * tag_vectors[item_id]
    return user_vector

def cosine_similarity(a, b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    if a_norm == 0 or b_norm == 0:
        return 0

    return np.dot(a, b) / (a_norm * b_norm)

def recommend(user_id, top_k):
    user_vector = build_user_vector(user_id)
    interacted_items = interactions_df[
        interactions_df["user_id"] == user_id
    ]

    interacted_item_ids = interacted_items["item_id"]
    candidate_items = items_df[
        (~items_df["item_id"].isin(interacted_item_ids)) &
        (items_df["is_available"] == True)
    ].copy()

    similarities = []
    for _, row in candidate_items.iterrows():
        item_id = row["item_id"]
        similarity = cosine_similarity(user_vector, tag_vectors[item_id])
        similarities.append(similarity)

    candidate_items["similarity"] = similarities
    candidate_items = candidate_items.sort_values("similarity", ascending=False)
    return candidate_items.head(top_k)

for user_id in range(1, 4):
    print("user_id", user_id)
    print(recommend(user_id, 2))
