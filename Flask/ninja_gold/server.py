from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "thisisasecret"


@app.route('/')

def index():

	return render_template('index.html')
#Have form submit to process_money
@app.route('/process_money', methods=['POST'])
def processor():
	#have processor grab the submit forms and determine gold to put out
	

	if request.form['building'] == 'farm':
		gold = random.randrange(10,21)
		print gold
		session['gold'] = gold
		if 'earn' not in session:
			session['earn']= gold
		else: session['earn'] += gold
		print session['earn']
		
	if request.form['building'] == 'cave':
		gold = random.randrange(5,11)
		print gold
		session['gold'] = gold
		if 'earn' not in session:
			session['earn']= gold
		else: session['earn'] += gold
		print session['earn']
		
	if request.form['building'] == 'house':
		gold = random.randrange(2,6)
		print gold
		session['gold'] = gold
		if 'earn' not in session:
			session['earn']= gold
		else: session['earn'] += gold
		print session['earn']
		
	if request.form['building'] == 'casino':
		gold = random.randrange(-51,51)
		print gold
		session['gold'] = gold
		if 'earn' not in session:
			session['earn']= gold
		else: session['earn'] += gold
		print session['earn']

	


	
	# return render_template('index.html', earn = session['earn'])
	return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True)