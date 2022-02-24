from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import io

app = Flask(__name__)

@app.route('/')
def hello():
    #기본 인덱스를 돌려줘라
    return render_template('index.html')

#현재 모델 저장 및 불러오는게 뭔가 오류가 나서 진행이 안됨
@app.route('/result', methods=['POST'])
def result():
    #모델을 불러와라 - 현재 바이블
    #bible_model = load_model('C:/Users/zekca/Section6/Project_1/data_out/bible_model/tf_model.h5')
    #예측에 입력값을 가져와라
    input_text = str(request.form["input_text"])
    #pred = bible_model.predict(input_text)
    #예측값을 페이지에 둬라
    return render_template('index.html', pred=input_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)