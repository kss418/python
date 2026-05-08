import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

users_df = pd.read_csv(BASE_DIR / "users.csv")
items_df = pd.read_csv(BASE_DIR / "items.csv")
interactions_df = pd.read_csv(BASE_DIR / "interactions.csv")

def min_max_normalize(series):
    if series.min() == series.max():
        return pd.Series([0.0] * len(series), index=series.index)
    return (series - series.min()) / (series.max() - series.min())

def recommend(user_id, users_df, items_df, interactions_df, top_k):
    user_df = users_df[users_df["user_id"] == user_id].iloc[0]
    interested_categories = user_df["interested_categories"].split("|")
    
    viewed_items = interactions_df[
        (interactions_df["user_id"] == user_id) &
        (interactions_df["event_type"] == "view")
    ]["item_id"].tolist()

    purchased_items = interactions_df[
        (interactions_df["user_id"] == user_id) &
        (interactions_df["event_type"] == "purchase")
    ]["item_id"].tolist()

    candidates = items_df.copy()
    candidates = candidates[candidates["is_available"] == True]
    candidates = candidates[~candidates["item_id"].isin(viewed_items)]
    candidates = candidates[~candidates["item_id"].isin(purchased_items)]
    candidates = candidates[candidates["category"].isin(interested_categories)]

    if candidates.empty:
        return []
    
    candidates["views_norm"] = min_max_normalize(candidates["views"])
    candidates["purchases_norm"] = min_max_normalize(candidates["purchases"])
    candidates["rating_norm"] = min_max_normalize(candidates["rating"])
    candidates["review_count_norm"] = min_max_normalize(candidates["review_count"])

    candidates["score"] = (
        candidates["views_norm"] * 0.2 +
        candidates["purchases_norm"] * 0.4 +
        candidates["rating_norm"] * 0.3 +
        candidates["review_count_norm"] * 0.1
    )

    result = candidates.sort_values("score", ascending=False).head(top_k)
    return result[
        ["item_id", "title", "category", "score"]
    ].to_json(orient="records", force_ascii=False)

for user_id in range(1, 4):
    recommend_json = recommend(user_id, users_df, items_df, interactions_df, 1)
    print("user_id :", user_id, "/", recommend_json)
