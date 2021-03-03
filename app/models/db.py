import pymysql
import config


class Database():
    def __init__(self, db=None, cursor=None):
        self.db = db
        self.cursor = cursor
    
    def openDB(self):
        self.db = pymysql.connect(
            config.DB_HOST,
            config.DB_USER,
            config.DB_PASSWORD,
            config.DB_NAME
        )
        self.cursor = self.db.cursor()
    
    def closeDB(self):
        self.db.close()

    def inputDataInv(self, input_data):
        self.openDB()
        q = "INSERT INTO \
            barang (kd_obat, nm_obat, jenis_obat, asal, tahun, stok, harga, tempat) \
            values (%s, %s, %s, %s, %s, %s, %s, %s)"%(input_data)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def inputDataNonInv(self, input_data):
        self.openDB()
        q = "INSERT INTO \
            barangnon (kd_barang, nm_barangnon, jenis_barangnon, asal, tgl_masuk, stok, harga, tempat) \
            values (%s, %s, %s, %s, %s, %s, %s, %s)"%(input_data)
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()

    def updateDataInv(self, input_data):
        self.openDB()
        q = ""
        self.cursor.execute(q)
        self.db.commit()
        self.closeDB()