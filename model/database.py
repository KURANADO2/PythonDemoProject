import mysql.connector
import configparser
from model.employee import Employee


class Database(object):
    # def create_connection(self):
    @classmethod
    def create_connection(cls):
        # connection = mysql.connector.connect(database='demo', user='root', password='', charset='utf8')
        config = configparser.ConfigParser()
        config.read('config.ini')
        DATABASE = config.get('DB_SECTION', 'database')
        USER = config.get('DB_SECTION', 'user')
        PASSWORD = config.get('DB_SECTION', 'password')
        CHARSET = config.get('DB_SECTION', 'charset')
        connection = mysql.connector.connect(database=DATABASE, user=USER, password=PASSWORD, charset=CHARSET)
        return connection

    @classmethod
    def query_employee(cls):
        sql = 'SELECT * FROM employee'
        connection = Database.create_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    @classmethod
    def save_employee(cls, emp):
        sql = 'INSERT INTO employee(code, name) VALUES(%s, %s)'
        connection = Database.create_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (emp.code, emp.name))
        connection.commit()
        cursor.close()
        connection.close()


if __name__ == '__main__':
    # db = Database()
    # db.create_connection()
    # Database.create_connection()
    # Save
    # employee = Employee('001', 'Jing')
    # Database.save_employee(employee)
    # Query
    print(Database.query_employee())
