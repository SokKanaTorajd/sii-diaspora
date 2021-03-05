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

    def inputDataInv(self, input_data):
        self.openDB()
        q = "INSERT INTO \
            barang (kd_obat, nm_obat, jenis_obat, asal, tahun, stok, harga, tempat) \
            values ('{}', '{}', '{}', '{}', {}, {}, {}, '{}')"%(input_data)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def inputDataNonInv(self, input_data):
        self.openDB()
        q = "INSERT INTO \
            barangnon (kd_barang, nm_barangnon, jenis_barangnon, asal, tgl_masuk, stok, harga, tempat) \
            values ({}, {}, {}, {}, {}, {}, {}, {})"%(input_data)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def updateDataInv(self, input_data):
        self.openDB()
        q = ""
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()