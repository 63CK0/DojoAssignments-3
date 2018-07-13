from flask import Flask, redirect, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user', methods=["POST"])
def show_user():
    print "Got post info"
    name = request.form['name']
    email = request.form['email']
    return render_template('user.html', name = name, email = email)
app.run(debug=True)
