# MLP Train

PyTorch로 간단한 MLP(Multi-Layer Perceptron) 분류 모델을 학습하는 예제입니다.

2차원 랜덤 데이터를 두 클래스로 나누고, 작은 신경망이 두 클래스를 구분하도록 학습합니다.

## 구성

- `MLP_train.py`: 데이터 생성, Dataset/DataLoader 구성, MLP 모델 정의, 학습 루프 실행

## 실행 방법

```bash
python MLP_train/MLP_train.py
```

## 학습 내용

- `Dataset`과 `DataLoader`로 데이터를 batch 단위로 불러오기
- `nn.Module`을 상속해 MLP 모델 만들기
- `CrossEntropyLoss`로 분류 loss 계산하기
- `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()`으로 모델 학습하기
- `argmax(dim=1)`로 모델 출력에서 예측 클래스 구하기
- epoch마다 loss와 accuracy 출력하기

## 모델 구조

```text
입력 2개
-> Linear(2, 16)
-> ReLU
-> Linear(16, 2)
-> 클래스 2개 중 하나로 분류
```

