from flask import Flask, render_template, request
from model import predict_growth

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        values = [
            int(request.form["population"]),
            int(request.form["waste"]),
            int(request.form["recycling"]),
            int(request.form["rainfall"]),
            int(request.form["urban"])
        ]

        prediction = predict_growth(values)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)