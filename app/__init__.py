from flask import Flask, render_template, request,  \
	redirect, url_for, session
from app.models.db import Database

app = Flask(__name__)
app.secret_key='f57037d4e48dfd249bc41ef33e15b66a'
database = Database()

@app.errorhandler(404)
def page_note_found(e):
	return render_template('404.html'), 404

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
def index():
	error = None

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		try:
			login_data = database.login(username, password)

			if username==login_data[1] and password==login_data[2]:
				session['name'] = login_data[0]
				session['username'] = login_data[1]
				return render_template('dashboard.html', user=login_data[0])

		except TypeError:
			error = 'Invalid username or password! Please try again.'
			return render_template('index.html', error=error)

	return render_template('index.html', error=error)

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/data-barang-inventaris')
def data_inv():
	return render_template('data-barang-inventaris.html')

@app.route('/input-data-inventaris')
def input_inv():
	return render_template('input-data-inventaris.html')

@app.route('/cetak-data-inventaris')
def cetak_inv():
	return render_template('cetak-data-inventaris.html')

@app.route('/data-barang-non-inventaris')
def data_non_inv():
	return render_template('data-barang-non-inventaris.html')

@app.route('/input-data-non-inventaris')
def input_non_inv():
	return render_template('input-data-non-inventaris.html')

@app.route('/cetak-data-non-inventaris')
def cetak_non_inv():
	return render_template('cetak-data-non-inventaris.html')
