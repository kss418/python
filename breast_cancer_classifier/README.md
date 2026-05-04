# Breast Cancer Classifier

Scikit-learn의 `load_breast_cancer` 예제 데이터를 사용해서 유방암 종양이 악성인지 양성인지 분류하는 간단한 Logistic Regression 프로젝트입니다.

## 사용한 데이터

`sklearn.datasets.load_breast_cancer`에서 제공하는 내장 데이터셋을 사용합니다.

- `x`: 종양의 여러 특징
- `y`: 정답 라벨
  - `0`: 악성
  - `1`: 양성

## 사용한 모델

1. `StandardScaler`: feature들의 scale을 평균 0, 표준편차 1 기준으로 표준화
2. `LogisticRegression`: 표준화된 feature를 사용해서 분류 모델 학습

Logistic Regression은 feature scale의 영향을 받는 선형 모델이므로, `area`처럼 값이 큰 feature와 `smoothness`처럼 값이 작은 feature를 비슷한 기준으로 맞추기 위해 `StandardScaler`를 사용합니다.

## 코드 흐름

1. breast cancer 데이터셋 로드
2. feature `x`와 target `y` 분리
3. train/test 데이터 분리
4. `StandardScaler`와 `LogisticRegression`을 Pipeline으로 구성
5. train 데이터로 모델 학습
6. test 데이터 예측
7. accuracy 출력
