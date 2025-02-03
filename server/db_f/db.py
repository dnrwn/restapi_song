import pymysql
from server.main import server as server
import key as key

class Database:
    def __init__(self):
        self.db = pymysql.connect(host=key.d['host'],
                                  user=key.d['user'],
                                  password=key.d['password'],
                                  db=key.d['db'],
                                  charset='utf8',
                                  port=key.d['port'])
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        server.logger.info('DB connect')

    def execute(self, query, args=None):
        server.logger.info('DB EXECUTE')
        if args is None:
            args = {}
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        if query.find('SELECT') == 0:
            if len(row) == 0:
                raise ValueError('Index not found')
            else:
                self.db.commit()
        return row