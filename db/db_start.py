import pymysql

db = pymysql.connect(host="localhost", user="root", password="qwerty123F!", database="users")

cur = db.cursor()
