
from flask import Flask, render_template
import os

app = Flask(__name__)  # Flask 애플리케이션 생성

# 라우트 설정
@app.route('/')  # http://127.0.0.1:5000/
def home():
    return render_template('index.html')  # 템플릿 렌더링

# 갤러리 페이지
@app.route('/gallery')  # http://127.0.0.1:5000/gallery
def gallery():
    photos = os.listdir("static/photos")  # 갤러리 폴더의 사진 목록 가져오기
    return render_template('gallery.html', photos=photos)  # 갤러리 템플릿 렌더링

if __name__ == '__main__':
    app.run(debug=True)  # 디버그 모드로 서버 실행