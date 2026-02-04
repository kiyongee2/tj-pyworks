# 서버 프로그램 만들기
# 플라스크 (Flask) 프레임워크 사용

from flask import Flask

app = Flask(__name__) # Flask 애플리케이션 생성

# 라우트 설정
@app.route('/')  #http://127.0.0.1:5000/
def home():
    return "<h1>Hello, Flask!</h1>"

@app.route('/introduce')  #http://127.0.0.1:5000/introduce
def about():
    return "<h1>자기 소개 페이지입니다.</h1>"

@app.route('/board/view')  #http://127.0.0.1:5000/board/view
def board_view():
    return "<h1>게시판 글 보기 페이지입니다.</h1>"

if __name__ == '__main__':
    app.run(debug=True) # 디버그 모드로 서버 실행