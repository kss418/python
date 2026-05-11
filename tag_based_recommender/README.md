# Tag Based Recommender

태그 정보를 이용해 사용자별 아이템을 추천하는 간단한 예제입니다.

## 파일 구성

- `items.csv`: 추천 대상 아이템 정보
- `interactions.csv`: 사용자와 아이템의 상호작용 기록
- `tag_based_recommender.py`: 태그 벡터 생성, 유저 벡터 생성, 추천 실행 코드

## 실행 방법

```bash
python3 tag_based_recommender/tag_based_recommender.py
```

## 추천 방식

1. 아이템의 `tags` 값을 기준으로 태그 목록을 만듭니다.
2. 각 아이템을 태그 벡터로 변환합니다.
3. 사용자의 상호작용 기록을 바탕으로 유저 벡터를 만듭니다.
   - `view`: 1.0
   - `like`: 3.0
   - `purchase`: 5.0
4. 유저 벡터와 아이템 벡터의 코사인 유사도를 계산합니다.
5. 이미 상호작용한 아이템은 제외하고, 유사도가 높은 아이템을 추천합니다.
