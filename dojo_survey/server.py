from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app.secret_key = 'super secret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/input', methods=['POST'])
def input():
    session['name'] = request.form['name']
    session['dojos'] = request.form['dojos']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('results.html')

if __name__ =="__main__":
    app.run(debug=True)