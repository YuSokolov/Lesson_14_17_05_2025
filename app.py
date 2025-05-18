from flask import Flask, render_template, request

from processing import get_prediction

app = Flask(__name__)

@app.route('/', methods=["get", "post"]) # 127.0.0.1:5000/
def index():
    message = "Здесь будут отражены результаты прогноза: 0 - до 18лет, 1 - от 18 до 25, 2 - 26-35, 3 - 36-45, 4 - 46-55, 5 - 56-65, 6 - >65"
    if request.method == "POST":
        user_num = request.form.get("user_num")
        # проверка кода
        age_code = get_prediction(float(user_num))
        message = f"Пользователь с кодом {user_num} возраст в группе {age_code}"

    return render_template("index.html", message = message)

if __name__ == '__main__':
    app.run()
