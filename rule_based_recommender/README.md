# Rule Based Recommender

pandas로 만든 간단한 규칙 기반 추천 시스템입니다.

사용자의 관심 카테고리와 기존 행동 데이터를 보고, 아직 보거나 구매하지 않은 상품 중 추천 후보를 골라 JSON 형태로 출력합니다.

## 파일 구성

- `rule_based_recommender.py`: 추천 로직 실행 코드
- `users.csv`: 사용자 정보와 관심 카테고리
- `items.csv`: 상품 정보, 조회수, 구매수, 평점, 리뷰 수
- `interactions.csv`: 사용자의 view/purchase 행동 기록

## 실행 방법

```bash
python3 rule_based_recommender/rule_based_recommender.py
```

## 추천 방식

1. 사용자 관심 카테고리를 가져옵니다.
2. 이미 조회하거나 구매한 상품을 제외합니다.
3. 판매 가능한 상품만 남깁니다.
4. 조회수, 구매수, 평점, 리뷰 수를 min-max normalization 합니다.
5. 가중합으로 score를 계산합니다.
6. score가 높은 순서대로 추천 결과를 JSON으로 출력합니다.

