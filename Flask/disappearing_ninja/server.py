from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")
@app.route('/blue')
def leonardo():
    return render_template("blue.html")
@app.route('/orange')
def michelangelo():
    return render_template("orange.html")
@app.route('/red')
def raphael():
    return render_template("red.html")
@app.route('/purple')
def donatello():
    return render_template("purple.html")
@app.route('/<string>')
def notapril(string):
    string != ['blue','ninjas', 'red', 'orange','purple']
    return render_template('notapril.html')

app.run(debug=True)
