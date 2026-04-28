# csv_cleaner

터미널에서 CSV 파일 경로를 입력받고, 다음 기능을 수행한다.

## 필수 옵션

`--input`, `--output`, `--columns` 옵션은 반드시 입력해야 한다.

| 기능 | 설명 |
| --- | --- |
| CSV 읽기 | `--input`으로 파일 입력 |
| 결측치 제거 | `--drop-missing` 옵션이 있으면 빈 값 포함 행 제거 |
| 컬럼 선택 | `--columns name age city` 형태로 컬럼 선택 |
| 요약 출력 | `--summary` 옵션이 있으면 행 개수, 컬럼명 출력 |
| CSV 저장 | `--output`으로 결과 저장 |
