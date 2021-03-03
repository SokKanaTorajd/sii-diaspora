from flask import Flask, render_template, request,  \
	redirect, url_for

app = Flask(__name__)


@app.errorhandler(404)
def page_note_found(e):
	return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid username or password! Please try again.'
		else:
			return redirect(url_for('dashboard'))

	return render_template('index.html', error=error)

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/about')
def about():
	return render_template('about.html')