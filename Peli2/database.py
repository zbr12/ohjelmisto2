import os
import mysql.connector


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='mysql.metropolia.fi',
            port=3306,
            database='jussvih',
            user='jussvih',
            password='root123',
            autocommit=True
        )

    def get_conn(self):
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()