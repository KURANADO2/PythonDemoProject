import mysql.connector
import configparser
from model.employee import Employee


class Database(object):
    # def create_connection(self):
    @classmethod
    def create_connection(cls):
        # connection = mysql.connector.connect(database='demo', user='root', password='', charset='utf8')
        config = configparser.ConfigParser()
        config.read('model/config.ini')
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
    def query_employee_by_id(cls, id):
        sql = 'SELECT * FROM employee WHERE id = %s'
        connection = Database.create_connection()
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        if len(result) == 0:
            return None
        return result[0]

    @classmethod
    def save_employee(cls, emp):
        sql = 'INSERT INTO employee(code, name) VALUES(%s, %s)'
        connection = Database.create_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (emp.code, emp.name))
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def update_employee(cls, emp):
        sql = 'UPDATE employee SET code = %s, name = %s WHERE id = %s'
        connection = Database.create_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (emp.code, emp.name, emp.id))
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def delete_employee(cls, id):
        sql = 'DELETE FROM employee WHERE id = %s'
        connection = Database.create_connection()
        cursor = connection.cursor()
        # 使用元组传入值，若元组内只有一个值，则后面要多加一个逗号
        # cursor.execute(sql, (id,))
        # 使用列表传入值
        cursor.execute(sql, [id])
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
    # Update
    # employee = Employee('001-update', 'Jing-update')
    # employee.id = 1
    # Database.update_employee(employee)
    # Delete
    Database.delete_employee(1)
    # Query
    print(Database.query_employee())
