import pymysql
# import server.main as server
# import key_de as key
from . import key_de as key

class Database:
    def __init__(self):
        self.db = pymysql.connect(host=key.d['host'],
                                  user=key.d['user'],
                                  password=key.d['password'],
                                  db=key.d['db'],
                                  charset='utf8',
                                  port=key.d['port'])
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        # server.server.logger.info('DB connect')

    def execute(self, query):
        print(query)
        # if args is None:
        args = {}
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        if query.find('SELECT') == 0:
            if len(row) == 0:
                raise ValueError('Index not found')
            else:
                self.db.commit()
        return row

Database = Database()