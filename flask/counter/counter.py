from flask import Flask, render_template, request, redirect,flash,make_response, session
app=Flask(__name__)
app.secret_key= 'secret'
@app.route('/',methods=['POST','GET'])
def count():
	if 'counter' in session:
		session['counter']=session.get('counter')+1
	else:
		session['counter']=1
	c=str(session.get('counter'))
	#if request.form['clear']:
		#print('clear')
	return render_template('counter.html',c=c)
@app.route('/delete',methods=['POST','GET'])
def delete():
	session.clear()
	session['counter']=0
	c=str(session.get('counter'))
	return render_template('counter.html',c=c)
@app.route('/plus',methods=['POST','GET'])
def plus():
	count
	if 'counter' in session:
		session['counter']=session.get('counter')+2
	c=str(session.get('counter'))
	return render_template('counter.html',c=c)
@app.route('/acc', methods=['POST','GET'])
def acc():
	y=request.form['var']
	z = int(y)
	if 'counter' in session:
		session['counter']=session.get('counter')+z
	c=str(session.get('counter'))
	return render_template('counter.html',c=c ,z=z)
app.run(debug=True)