from app.models import config
import pymysql


class Database():
    def __init__(self, db=None, cursor=None):
        self.db = db
        self.cursor = cursor
        self.host = config.DB_HOST
        self.user = config.DB_USER
        self.pwd = config.DB_PASSWORD
        self.db_name = config.DB_NAME

    def openDB(self):
        self.db = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.pwd,
            db=self.db_name)
        self.cursor = self.db.cursor()
    
    def closeDB(self):
        self.db.close()

    def login(self, username, password):
        self.openDB()
        q = "SELECT nm_lengkap, username, password FROM admin \
            WHERE username='{}' and password='{}'".format(username, password)
        self.cursor.execute(q)
        login_data = self.cursor.fetchone()
        self.closeDB()
        return login_data

    def getDataInv(self):
        self.openDB()
        q = "SELECT * FROM barang"
        inv_data = []
        self.cursor.execute(q)
        for kode, jenis, asal, tahun, jumlah, harga, stok, tempat in self.cursor.fetchall():
            inv_data.append((kode, jenis, asal, tahun, jumlah, harga, stok, tempat))
        self.closeDB()
        return inv_data

    def inputDataInv(self, input_data):
        self.openDB()
        q = "INSERT INTO \
            barang (kd_obat, nm_obat, jenis_obat, asal, tahun, stok, harga, tempat) \
            values ('%s', '%s', '%s', '%s', %i, %i, %i, '%s')"%(input_data)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def getDataInvByKode(self, kode):
        self.openDB()
        q = "SELECT * FROM barang WHERE kd_obat='{}'".format(kode)
        self.cursor.execute(q)
        data = self.cursor.fetchone()
        self.closeDB()
        return data

    def updateDataInv(self, data):
        self.openDB()
        q = "UPDATE barang SET \
            nm_obat='%s', jenis_obat='%s', asal='%s', tahun=%i, stok=%i, harga=%i, tempat='%s' \
            WHERE kd_obat='%s'"%(data)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def deleteDataInv(self, kode):
        self.openDB()
        q = "DELETE FROM barang WHERE kd_obat='{}'".format(kode)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def getKondisi(self):
        self.openDB()
        q = "SELECT * FROM kondisi"
        self.cursor.execute(q)
        data = [(kode, kondisi) for kode, kondisi in self.cursor.fetchall()]
        self.closeDB()
        return data

    def inputPenggunaanInv(self, data):
        self.openDB()
        q = "INSERT INTO eoq (kd_obat, kd_kondisi, barang_rusak, keterangan) \
            values ('%s', '%s', %i, '%s')"%(data)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()
    
    def getKondisiBarang(self):
        self.openDB()
        q = "SELECT id, kd_obat, kondisi, barang_rusak, keterangan \
            FROM eoq, kondisi WHERE kondisi.kd_kondisi=eoq.kd_kondisi"
        self.cursor.execute(q)
        data = []
        for id, kd_barang, kondisi, jumlah, ket in self.cursor.fetchall():
            data.append((id, kd_barang, kondisi, jumlah, ket))
        self.closeDB()
        return data

    def cetakLaporanInv(self):
        self.openDB()
        q = "SELECT barang.kd_obat, nm_obat, jenis_obat, asal, tahun, stok, harga, \
                tempat, kondisi, barang_rusak, keterangan \
            FROM barang, eoq, kondisi \
            WHERE barang.kd_obat=eoq.kd_obat and kondisi.kd_kondisi=eoq.kd_kondisi"
        self.cursor.execute(q)
        data = []
        for kd, nm, jns, asal, thn, stok, hrg, tmpt, knd, rsk, ket in self.cursor.fetchall():
            data.append((kd, nm, jns, asal, thn, stok, hrg, tmpt, knd, rsk, ket)) 
        self.closeDB()
        return data
    
    def deletePenggunaanInv(self, id):
        self.openDB()
        q = "DELETE FROM eoq WHERE id={}".format(id)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def getDataNonInv(self):
        self.openDB()
        q = "SELECT * FROM barangnon"
        data = []
        self.cursor.execute(q)
        for kode, nama, jenis, asal, tgl_masuk, stok, harga, tempat in self.cursor.fetchall():
            data.append((kode, nama, jenis, asal, tgl_masuk, stok, harga, tempat))
        self.closeDB()
        return data

    def inputDataNonInv(self, input_data):
        self.openDB()
        q = "INSERT INTO \
            barangnon (kd_barang, nm_barangnon, jenis_barangnon, asal, tgl_masuk, stok, harga, tempat) \
            values ({}, {}, {}, {}, {}, {}, {}, {})"%(input_data)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def updateDataNonInv(self, input_data):
        self.openDB()
        q = ""
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()