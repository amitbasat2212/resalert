import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="res_alert",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
