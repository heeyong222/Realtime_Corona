from flask import Flask, render_template
import corona_data
from datetime import date, timedelta

# 앱 생성

app = Flask(__name__)

# url 라우터
@app.route('/')
def index():
    now = date.today()
    now_str = now.strftime("%Y%m%d")
    # print(now_str)

    # 입력날짜로 출력
    data = corona_data.get_corona_data(now_str, now_str)

    # 입력날짜에 대한 정보가 없다면 전날 출력
    if not data:
        print("아직", now_str, "에 대한 정보가 없어 전날의 정보를 출력합니다.")
        yesterday = now - timedelta(days=1)
        yesterday_str = yesterday.strftime("%Y%m%d")

        data = corona_data.get_corona_data(yesterday_str, yesterday_str)


    return render_template('index.html', data=data[1:])


# main
if __name__ == "__main__":
    app.run(debug=True)