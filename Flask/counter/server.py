from flask import Flask, session, redirect, request, render_template
app = Flask(__name__)
app.secret_key = "isismysecretkey"

@app.route('/')
def index():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 1
    return render_template('index.html', count = session["count"])
app.run(debug=True)
