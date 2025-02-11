import json
import random
import smtplib
import string
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector
from datetime import datetime, timedelta
from flask import jsonify, request, session, Blueprint
from flask_cors import CORS
import uuid
from src.bean.Constant import Constant
from src.db.ConnectedDB import get_db_connection
from src.utils.CryptoUtils import CryptoUtils

# ✅ 创建 Blueprint 以便于 Flask 绑定
register_api = Blueprint("register", __name__)

def generate_verification_code(length=6):
    """生成6位随机验证码"""
    return ''.join(random.choices(string.digits, k=length))

def send_verification_email(email, code):
    """发送邮箱验证码"""
    sender_email = "qinjing_org@student.usm.my"
    sender_password = "Reiki13243546."
    subject = "验证码通知"
    body = f"您的验证码是: {code}，请在5分钟内输入完成验证。"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        print("Verification email sent")
    except Exception as e:
        print(f"Email sending failed: {e}")

# ✅ 发送验证码接口
@register_api.route('/send_verification_code', methods=['POST', 'OPTIONS'])
def send_verification_code():
    """发送验证码"""
    if request.method == 'OPTIONS':
        return jsonify({'message': 'Options request approved'}), 200

    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Email is required'}), 400

    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({'message': 'Database connection failed'}), 500

        cursor = conn.cursor()
        verification_code = generate_verification_code()

        # ✅ 存入数据库（支持更新验证码）
        cursor.execute(
            "INSERT INTO email_verification (email, code, created_at) VALUES (%s, %s, NOW()) "
            "ON DUPLICATE KEY UPDATE code=%s, created_at=NOW()",
            (email, verification_code, verification_code)
        )
        conn.commit()
        send_verification_email(email, verification_code)

        cursor.close()
        conn.close()
        return jsonify({'message': 'Verification code sent successfully'}), 200

    except Exception as e:
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

# ✅ 用户注册接口
@register_api.route('/register', methods=['POST', 'OPTIONS'])
def register():
    """注册新用户"""
    if request.method == 'OPTIONS':
        return jsonify({'message': 'Options request approved'}), 200

    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    code = data.get('verificationCode')

    if not name or not email or not password or not code:
        return jsonify({'message': 'All fields are required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # ✅ 验证验证码是否正确且未过期
        cursor.execute(
            "SELECT * FROM email_verification WHERE email=%s AND code=%s AND TIMESTAMPDIFF(MINUTE, created_at, NOW()) <= 2",
            (email, code)
        )
        if not cursor.fetchone():
            return jsonify({'message': 'Invalid or expired verification code'}), 400

        # ✅ 加密密码
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # ✅ 插入用户数据
        cursor.execute("INSERT INTO userinfo (name, email, password) VALUES (%s, %s, %s)",
                       (name, email, hashed_password))
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({'message': 'User registered successfully'}), 200

    except mysql.connector.IntegrityError:
        return jsonify({'message': 'Email already exists'}), 409
    except Exception as e:
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

# ✅ 检查邮箱是否存在
@register_api.route('/checkEmail', methods=['GET'])
def checkEmail():
    """检查邮箱是否已经被注册"""
    email = request.args.get('email')
    if not email:
        return jsonify({'message': 'Missing email parameter'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userinfo WHERE email = %s", (email,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            return jsonify({'message': 'Email already exists'}), 201
        else:
            return jsonify({'message': 'Email available for registration'}), 200

    except Exception as e:
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500


@register_api.route("/check_login", methods=["GET"])
def check_login():
    """ 检查当前用户是否已登录 """
    print(session)
    if "user_id" in session:
        # session["user_id"]  去查询这个表recordbirth 通过fromuser字段和 然后根据birth排序，选取时间最近的一条，
        return jsonify({"logged_in": True, "user_id": session["user_id"], "username": session["username"]})

    return jsonify({"logged_in": False}), 401



@register_api.route("/logout", methods=["POST"])
def logout():
    """ 用户登出 """
    session.clear()  # 清除 session
    return jsonify({"message": "已退出登录"})

# ✅ 登录接口
@register_api.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("SELECT * FROM userinfo WHERE email=%s AND password=%s", (email, hashed_password))
        user = cursor.fetchone()

        cursor.close()
        conn.close()


        if user:
            session["user_id"] = email # 存储用户 ID
            session['username'] = str(uuid.uuid4()).replace("-","")
            session.permanent = True
            return jsonify({
                'message': 'Login successful',
                # 'user': CryptoUtils.simple_encrypt_decrypt(json.dumps(user),Constant.AES_KEY),
                'user':user["id"],
                'code': 200,
                'session': session['username']
            }), 200
        else:
            return jsonify({'message': 'Invalid email or password', 'code': 401}), 401

    except Exception as e:
        return jsonify({'message': 'Internal server error', 'code': 500, 'error': str(e)}), 500
