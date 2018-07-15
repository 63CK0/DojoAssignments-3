from flask import Flask, session, redirect, request, render_template
import random

app = Flask(__name__)
app.secret_key = "thisissecret"
@app.route('/')

def index():
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guessit():
	if 'num' not in session:
		session['num'] = random.randrange(0,101)
	
	print session['num']
	guess = int(request.form['guess'])

	if guess < session['num']:
		session['guess'] = "too low"
	elif guess > session['num']:
		session['guess'] = "too high"
	else:
		session['guess'] = "correct"
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')





app.run(debug=True)
