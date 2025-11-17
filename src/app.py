from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def zeroing():
    cnt.reset()
    return redirect("/")

@app.route("/set", methods=["POST"])
def setter():
    amount = int(request.form.get("value", "0"))
    cnt.setto(amount)
    return redirect("/")

