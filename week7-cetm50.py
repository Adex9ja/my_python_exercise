from pony.orm import Database
from pony.orm import db_session
import pymysql as mysql_module

db = Database()
db.bind(provider='mysql', host='europa.ashley.work', user='student_bi12oy', passwd='iE93F2@8EhM@1zhD&u9M@K', db='student_bi12oy')

with db_session:
    customers = db.execute('SELECT * FROM CUSTOMER')
    for row in customers:
        print(row)
    orders = db.execute('SELECT amount FROM ORDERS')
    for row in orders:
        print(row)

