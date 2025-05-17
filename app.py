from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["get", "post"])
def index():
    message = "Стартовое сообщение"
    if request.method == "POST":
        area = request.form.get(area)
        # проверка кода
        area = float(area)
    return render_tamplate("index.html", message = message)

if __name__ == '__main__':
    app.run()
