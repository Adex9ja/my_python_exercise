from pony.orm import Database
from pony.orm import db_session
import pymysql as mysql_module

db = Database()
db.bind(provider='mysql', host='europa.ashley.work', user='cetm50_user', passwd='iE93F2@8EhM@1zhD&u9M@K', db='cetm50')

# with db_session:
#     my_query_result = db.select('SELECT * FROM gameUser')
#     for row in my_query_result:
#         print(row)

# with db_session:
#     some_limit = 10
#     my_query_result = db.select(f'SELECT * from gameUser LIMIT {some_limit}')
#     for row in my_query_result:
#         print({
#             'id': row.id,
#             'name': row.name,
#             'phone': row.phone,
#             'email': row.email,
#         })
