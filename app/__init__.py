from flask import Flask, render_template, request,  \
	redirect, url_for, session
from flask_weasyprint import HTML, render_pdf
from app.models.db import Database
from datetime import date

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
				return redirect(url_for('dashboard'))

		except TypeError:
			error = 'Invalid username or password! Please try again.'
			return render_template('index.html', error=error)

	return render_template('index.html', error=error)

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/data-barang-inventaris')
def data_inv():
	inv_data = database.getDataInv()
	return render_template('data-barang-inventaris.html', data=inv_data)

@app.route('/input-data-inventaris', methods=['GET', 'POST'])
def input_inv():
	if request.method == 'POST':
		kode = request.form['kode_barang']
		nama = request.form['nama_barang']
		jenis = request.form['jenis_barang']
		asal = request.form['asal_barang']
		tahun = int(request.form['tahun'])
		jumlah = int(request.form['jumlah'])
		harga = int(request.form['harga'])
		tempat = request.form['tempat']
		data = (kode, nama, jenis, asal, tahun, jumlah, harga, tempat)
		database.inputDataInv(data)
		return redirect(url_for('data_inv'))
	else:
		return render_template('input-data-inventaris.html')

@app.route('/update-barang-inventaris/<kode_barang>', methods=['GET', 'POST'])
def update_inv(kode_barang):
	if request.method == 'GET':
		data = database.getDataInvByKode(kode_barang)
		return render_template('update-data-inventaris.html', data=data)

	else:
		kode = request.form['kode_barang']
		nama = request.form['nama_barang']
		jenis = request.form['jenis_barang']
		asal = request.form['asal_barang']
		tahun = int(request.form['tahun'])
		jumlah = int(request.form['jumlah'])
		harga = int(request.form['harga'])
		tempat = request.form['tempat']
		data = (nama, jenis, asal, tahun, jumlah , harga, tempat, kode)
		database.updateDataInv(data)
		return redirect(url_for('data_inv'))

@app.route('/delete-barang-inventaris/<kode_barang>')
def delete_inv(kode_barang):
	database.deleteDataInv(kode_barang)
	return redirect(url_for('data_inv'))

@app.route('/penggunaan-barang-inventaris', methods=['GET', 'POST'])
def penggunaan_inv():
	if request.method == 'GET':
		kondisi = database.getKondisi()
		data = database.getDataInv()
		return render_template('penggunaan-barang-inventaris.html', kondisi=kondisi, data=data)
	else:
		kode = request.form['kode_barang']
		kondisi = request.form['kondisi']
		jumlah = int(request.form['jumlah'])
		keterangan = request.form['keterangan']
		data = (kode, kondisi, jumlah, keterangan)
		database.inputPenggunaanInv(data)
		return redirect(url_for('laporan_inv'))

@app.route('/laporan-inventaris', methods=['GET'])
def laporan_inv():
	if request.method=='GET':
		data = database.getKondisiBarang()
		return render_template('laporan-barang-inventaris.html', data=data)
	
@app.route('/delete-penggunaan-inventaris/<id>')
def delete_penggunaan_inv(id):
	database.deletePenggunaanInv(id)
	return redirect(url_for('laporan_inv'))

@app.route('/cetak-laporan-inventaris', methods=['GET'])
def cetak_inventaris():
	if request.method=='GET':
		data = database.cetakLaporanInv()
		tanggal = date.today()
		tanggal = tanggal.strftime("%d %b %Y")
		# laporan = render_template('cetak-data-inventaris.html', data=data, tanggal=tanggal)
		# return render_pdf(HTML(string=laporan, base_url=request.build_absolute_uri()))
		return render_template('cetak-data-inventaris.html', data=data, tanggal=tanggal)

# @app.route('/laporan-inventaris.pdf')
# def cetak_pdf():
# 	return render_pdf(url_for('cetak_inventaris'))

@app.route('/data-barang-non-inventaris')
def data_non_inv():
	data = database.getDataNonInv()
	return render_template('data-barang-non-inventaris.html', data=data)

@app.route('/input-data-non-inventaris')
def input_non_inv():
	return render_template('input-data-non-inventaris.html')

@app.route('/penggunaan-barang-non-inventaris')
def penggunaan_non_inv():
	return render_template('penggunaan-barang-non-inventaris.html')

@app.route('/laporan-non-inventaris')
def laporan_non_inv():
	return render_template('laporan-barang-non-inventaris.html')

@app.route('/cetak-data-non-inventaris')
def cetak_non_inv():
	return render_template('cetak-data-non-inventaris.html')
