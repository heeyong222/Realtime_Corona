# Realtime_Corona
공공데이터포털 data.go.kr의 코로나19 시·도발생 현황 OpenAPI와 Flask를 사용하여 실시간 코로나 확진자 및 사망자 차트 기능 웹 구현

## Installation
```
pip install pylint
pip install xmltodict
pip install Flask
```

## Detail
* gubun : 지역 목록
* localOccCnt : 날짜별 확진자 수
* deathCnt : 지역별 사망 누적자 수
* incDec : 전일대비 증감
* isolClearCnt : 격리해제 수
* qurRate : 10만명 당 발생 수

* 가시성을 위해 chart js 사용
  ```
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
  ```

## Screenshots
![cc1](https://user-images.githubusercontent.com/71097404/98326443-a09d8c80-2034-11eb-8132-8e94ecd904d7.JPG)
![cc2](https://user-images.githubusercontent.com/71097404/98326461-aabf8b00-2034-11eb-80dc-520b298dac79.JPG)

