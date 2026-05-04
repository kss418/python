# Diabetes Regression

Scikit-learn의 `load_diabetes` 내장 데이터셋을 사용해서 질병 진행 정도를 예측하는 회귀 예제입니다.

## 사용한 데이터

- `x`: 나이, 성별, BMI, 혈압, 혈청 수치 등 10개 feature
- `y`: 질병 진행 정도를 나타내는 숫자 target

## 사용한 모델

`RandomForestRegressor`를 사용합니다.

## 실행 방법

```bash
python diabetes_regression/diabetes_regression.py
```

## 코드 흐름

1. diabetes 데이터셋 로드
2. feature `x`와 target `y` 분리
3. train/test 데이터 분리
4. `RandomForestRegressor` 학습
5. test 데이터 예측
6. MSE와 R2 출력
