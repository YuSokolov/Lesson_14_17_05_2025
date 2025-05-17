from flask import Flask, render_template, request

from processing import get_prediction

app = Flask(__name__)

@app.route('/', methods=["get", "post"]) # 127.0.0.1:5000/
def index():
    # message = "Стартовое сообщение"
    if request.method == "POST":
        area = request.form.get("area")
        # проверка кода
        cost = get_prediction(float(area))
        print(cost)

    return render_template("index.html")

if __name__ == '__main__':
    app.run()
