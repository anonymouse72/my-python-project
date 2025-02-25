
from flask import Flask, request, jsonify
import mysql.connector
import hashlib

app = Flask(__name__)
# 数据库连接配置
DB_CONFIG = {
    'host': '13.229.224.223',
    # 'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'fortune'
}

def get_db_connection():
    """获取数据库连接"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"数据库连接错误: {err}")
        return None