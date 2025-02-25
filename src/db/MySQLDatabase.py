import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self):
        """
        初始化数据库连接

        :param host: 数据库主机地址
        :param user: 数据库用户名
        :param password: 数据库密码
        :param database: 数据库名称
        """
        self.host = "13.229.224.223"
        # self.host = "127.0.0.1"
        self.user = "root"
        self.password = "123456"
        self.database = "fortune"
        self.connection = None

    def connect(self):
        """建立数据库连接"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print(f"Error while connecting to the database: {e}")
            raise

    def execute_query(self, query, params=None):
        """
        执行写操作 (INSERT, UPDATE, DELETE)

        :param query: SQL 查询语句
        :param params: 参数化查询的参数
        """
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error while executing query: {e}")
            self.connection.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def fetch_all(self, query, params=None):
        """
        执行读取操作，返回所有结果

        :param query: SQL 查询语句
        :param params: 参数化查询的参数
        :return: 查询结果
        """
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error while fetching data: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def fetch_one(self, query, params=None):
        """
        执行读取操作，返回单个结果

        :param query: SQL 查询语句
        :param params: 参数化查询的参数
        :return: 单个查询结果
        """
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Error while fetching data: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def close_connection(self):
        """关闭数据库连接"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# 使用示例
if __name__ == "__main__":
    # 初始化数据库连接信息
    db = MySQLDatabase()

    try:
        # 连接数据库
        db.connect()

        # 创建表示例
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL
        )
        """
        db.execute_query(create_table_query)

        # 插入数据示例
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        db.execute_query(insert_query, ("John Doe", "john@example.com"))

        # 查询数据示例
        select_query = "SELECT * FROM users"
        results = db.fetch_all(select_query)
        print("Users:", results)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 关闭数据库连接
        db.close_connection()
