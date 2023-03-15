import random
from flask import Flask, render_template, session, request, redirect
from datetime import datetime
app = Flask(__name__)

app.secret_key = 'super secret'

@app.route('/')
def index():
    if "your_gold" not in session:
        session["your_gold"] = 0

    if "activities" not in session:
        session["activities"] = []

    activities = session["activities"]
    return render_template("index.html", activities=activities)

@app.route('/process_money', methods = ["POST"])
def process_money():
    location = request.form["location"]
    activities = session["activities"]
    if location == "Farm":
        earnedValue = random.randint(10, 20)
    elif location == "Cave":
        earnedValue = random.randint(5, 10)
    elif location == "House":
        earnedValue = random.randint(2, 5)
    elif location == "Casino":
        earnedValue = random.randint(-50, 50)

    activities.append({
        "activityName": location,
        "earnedGold": earnedValue,
        "date": datetime.now(),
    })
    session["your_gold"] += earnedValue
    session["activities"] = activities

    return redirect("/")

@app.route('/remove')
def remove():
    session.clear()
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)