import random
import smtplib
import string
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import timedelta
from venv import logger

import mysql.connector  # ✅ 建议使用 mysql.connector
import requests
from flask import jsonify, Blueprint, request, session
from flask_cors import CORS

from src.api.AskInfo import AskInfo
from src.bean.Constant import Constant
from src.db.ConnectedDB import get_db_connection, app
from src.rules.AstrologyAnalyzer import AstrologyAnalyzer
from src.tools.BaziCalculator import BaziCalculator
from src.utils.CryptoUtils import CryptoUtils

# ✅ 创建 Blueprint
getinformation_api = Blueprint("getinformation", __name__)

@getinformation_api.route('/testInfo', methods=['GET'])
def test_info():
    """
    示例接口：仅演示 getInformation.py 里自定义的接口
    这里可以实现你所需的获取用户信息等逻辑
    """
    # 下面只是返回一个示例 JSON
    return jsonify({"message": "Hello from getInformation module!"}), 200

# 可以根据需要补充更多非重复的接口 ...
@getinformation_api.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    email = data.get("Email")
    gender = data.get("Gender", "")
    birth = data.get("Birth")
    birth_location = data.get("Birthlocation", "")
    race = data.get("Race")
    name = data.get("Name")
    userid = data.get('user')
    if not email or not birth or not race:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        birth_datetime = datetime.strptime(birth, "%Y-%m-%d %H:%M:%S")
        birth_year = birth_datetime.year
        birth_month = birth_datetime.month
        birth_day = birth_datetime.day
        birth_hour = birth_datetime.hour
        birth_minute = birth_datetime.minute
        birth_second = birth_datetime.second

        conn = get_db_connection()
        if conn is None:
            return jsonify({'message': 'Database connection failed'}), 500

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name,email, gender, year, month, day, hour, minute, seconds, location, race, createtime) VALUES "
            "(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name,email, gender, birth_year, birth_month, birth_day, birth_hour, birth_minute, birth_second,
             birth_location, race, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )

        cursor.execute(
            "INSERT INTO recordbirth (birth, gender, fromuser,createtime) VALUES (%s, %s, %s,%s)",
            (birth, gender, userid,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # `user_id` 未定义，改用 `email`
        )

        conn.commit()
        cursor.close()
        conn.close()
        birth_date = (birth_year, birth_month, birth_day, birth_hour)

        analyzer = AstrologyAnalyzer(birth_date, gender)

        str = CryptoUtils.simple_encrypt_decrypt(analyzer.bazi+','+gender, Constant.AES_KEY)
        response = jsonify({"message": "Form submitted successfully",'data':str,'code':200})
        return response, 200
    except mysql.connector.Error as err:
        return jsonify({"error": "Database error", "details": str(err)}), 500


from flask import Flask, request, jsonify
from datetime import datetime
import json
import mysql.connector

@getinformation_api.route('/getPersonInfo', methods=['POST'])
def getPersonInfo():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    gender = data.get("Gender", "")
    birth = data.get("Birth")

    if not birth:
        return jsonify({"error": "Birth date is required"}), 400

    try:
        # 解析生日
        birth_datetime = datetime.strptime(birth, "%Y-%m-%d %H:%M:%S")
        birth_date = (birth_datetime.year, birth_datetime.month, birth_datetime.day, birth_datetime.hour)

        # 生成八字信息
        analyzer  = AstrologyAnalyzer(birth_date, gender)
        # 构造 AI 查询请求
        query = f"""
        请根据中国传统命理学分析以下命主的八字，并返回完整的八字排盘数据。
        {analyzer.bazi},性别{gender},
        请严格按照 JSON 格式返回数据，并计算五行平衡、阴阳属性、空亡信息、纳音等。
        """

        # 发送请求给 AI
        result = AskInfo().ask(query)

        # 确保返回的是 JSON 格式
        if isinstance(result, str):
            result = json.loads(result)  # 转换为字典格式，防止二次 JSON 化

        return jsonify(result), 200

    except ValueError:
        return jsonify({"error": "Invalid birth date format, expected 'YYYY-MM-DD HH:MM:SS'"}), 400
    except mysql.connector.Error as err:
        return jsonify({"error": "Database error", "details": str(err)}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500


# 获取八字阴阳的数据
@getinformation_api.route('/getData1', methods=['POST'])
def getYinAndYang():
    try:
        data = request.json
        logger.info(f" /api/getData1 Received request data: {data}")  # 记录收到的数据

        if not data:
            return jsonify({"error": "No data provided"}), 400

        gender = data.get("gender", "")
        birth = data.get("bazi")

        if not birth:
            return jsonify({"error": "Birth date is required"}), 400
        conn = get_db_connection()
        if conn is None:
            return jsonify({'message': 'Database connection failed'}), 500
        cursor = conn.cursor()
        query = "SELECT content FROM bazi_analysis WHERE bazi = %s AND gender = %s"
        cursor.execute(query, (birth, gender))

        # 获取第一条数据
        row = cursor.fetchone()

        # 如果有数据，则打印
        if row:
            # 关闭连接
            cursor.close()
            conn.close()
            return jsonify(row[0])
        else:
            query = (f"请根据中国传统命理学分析八字：{birth}，性别：{gender}。每个分析特点要200字以上\n"
                     "请详细分析该八字的：\n"
                     "- 性格特点\n"
                     "- 性格优点\n"
                     "- 性格缺点\n"
                     "- 做事风格（工作表现）\n"
                     "- 金钱观\n"
                     "- 爱情观\n"
                     "- 给外人的感受\n"
                     "- 常见 MBTI 性格类型\n\n"
                     "请以 JSON 格式返回结果，确保：\n"
                     "1. `title` 字段使用英文\n"
                     "2. `内容` 使用中文，且**不要**进行字符编码（例如 `\\u4e00\\u4e8c` 等）。\n"
                     "3. 格式示例如下：\n\n"
                     "{\n"
                     '  "CharacterTraits": "具体的性格特点",\n'
                     '  "Strengths": "具体的性格优点",\n'
                     '  "Weaknesses": "具体的性格缺点",\n'
                     '  "WorkStyle": "具体的做事风格",\n'
                     '  "MoneyConcept": "具体的金钱观",\n'
                     '  "LoveView": "具体的爱情观",\n'
                     '  "ImpressionToOthers": "给外人的感受",\n'
                     '  "CommonMBTIType": "常见的 MBTI 类型"\n'
                     "}"
                     "4. 用英文返回\n\n"
                     )

            askInfo = AskInfo()

            try:
                response_data = askInfo.ask(query)
                if('Error' in response_data):
                    logger.error("API results contain error information and are not stored in the database.")
                else:
                    cursor.execute(
                        "INSERT INTO bazi_analysis (bazi, content,gender, createtime) VALUES (%s, %s, %s, %s)",
                        (birth, response_data, gender, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    )

                conn.commit()
                cursor.close()
                conn.close()
                logger.debug(f"API response: {response_data}")  # 记录 API 返回数据
            except Exception as e:
                logger.error(f"Error calling askInfo.ask(): {e}", exc_info=True)
                return jsonify({"error": "Failed to fetch analysis"}), 500
            return jsonify(response_data)
    except Exception as e:
        logger.error(f"Unexpected error in getYinAndYang: {e}", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500



# 获取八字阴阳的数据
@getinformation_api.route('/getData2', methods=['POST'])
def getAllOfInfo():
    try:
        data = request.json
        logger.info(" /api/getData2 Received request data:%s", data)

        if not data:
            return jsonify({"error": "No data provided"}), 400

        gender = data.get("gender", "").strip()
        birth = data.get("bazi", "").strip()

        if not birth:
            return jsonify({"error": "Birth date is required"}), 400

        conn = get_db_connection()
        if conn is None:
            return jsonify({'message': 'Database connection failed'}), 500
        cursor = conn.cursor()
        query = "SELECT content FROM lifeOverview WHERE bazi = %s AND gender = %s"
        cursor.execute(query, (birth, gender))
        # 获取第一条数据
        row = cursor.fetchone()
        # 如果有数据，则打印
        if row:
            # 关闭连接
            cursor.close()
            conn.close()
            return jsonify(row[0])
        else:
            query = (f"请根据中国传统命理学分析八字：{birth}，性别：{gender}。\n"
                     f"请详细分析该八字的：\n"
                     f"1. **学业运势**：学习能力、适合的学科、考试运、未来学业发展方向（200 字以上）。\n"
                     f"2. **财富运势**：财运走势、适合的赚钱方式、投资风险、大运对财富的影响（200 字以上）。\n"
                     f"3. **未来运势**：30 岁后大运对事业和财运的影响（200 字以上）。\n"
                     f"请严格按照 **JSON 格式** 返回,用英文返回：\n"
                     f"{{\n"
                     f"  \"BaziAnalysis\": {{\n"
                     f"    \"Academics\": {{\n"
                     f"      \"title\": \"Academics\",\n"
                     f"      \"content\": \"...\"\n"
                     f"    }},\n"
                     f"    \"Wealth\": {{\n"
                     f"      \"title\": \"Wealth\",\n"
                     f"      \"content\": \"...\"\n"
                     f"    }},\n"
                     f"    \"FutureTrends\": {{\n"
                     f"      \"title\": \"Future Trends\",\n"
                     f"      \"content\": \"...\"\n"
                     f"    }}\n"
                     f"  }}\n"
                     f"}}"
                     )

            askInfo = AskInfo()


            try:
                response_data = askInfo.ask(query)
                if ('Error' in response_data):
                    logger.error("API results contain error information and are not stored in the database.")
                else:
                    cursor.execute(
                        "INSERT INTO lifeOverview (bazi, content,gender, createtime) VALUES (%s, %s, %s, %s)",
                        (birth, response_data, gender, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    )

                conn.commit()
                cursor.close()
                conn.close()
                logger.info("AI Response: %s", response_data)

            except Exception as e:
                logger.error(f"Error calling askInfo.ask(): {e}", exc_info=True)
                return jsonify({"error": "Failed to fetch analysis"}), 500
            return jsonify(response_data)


    except ValueError as ve:
        return jsonify({"error": "Invalid request data", "details": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500





@getinformation_api.route('/getData3', methods=['POST'])
def get_bazi_info():
    try:
        # 解析请求 JSON 数据
        bazi_data = request.get_json()
        if not bazi_data or 'bazi' not in bazi_data:
            logger.warning("请求缺少 'bazi' 字段")
            return jsonify({"错误": "请求缺少 'bazi' 字段"}), 400

        logger.info(f" /api/getData3 收到请求数据: {bazi_data}")  # 记录请求数据

        # 计算八字
        bazi_calculator = BaziCalculator(bazi_data['bazi'], Constant)
        result_json = bazi_calculator.pillars_analysis_json()


        # 以中文格式返回 JSON
        return app.response_class(
            response=json.dumps(result_json, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    except json.JSONDecodeError:
        logger.error("无效的 JSON 格式")
        return jsonify({"错误": "无效的 JSON 格式"}), 400
    except Exception as e:
        logger.exception(f"处理八字数据时发生错误: {e}")  # 使用 logger.exception 记录异常堆栈
        return jsonify({"错误": "服务器内部错误", "详细信息": str(e)}), 500


@getinformation_api.route('/getData4', methods=['POST'])
def get_bazipaipan():
    try:
        data = request.json
        logger.info(" /api/getData4 Received request data:%s", data)

        if not data:
            return jsonify({"error": "No data provided"}), 400

        gender = data.get("gender", "").strip()
        birth = data.get("bazi", "").strip()

        if not birth:
            return jsonify({"error": "Birth date is required"}), 400

        conn = get_db_connection()
        if conn is None:
            return jsonify({'message': 'Database connection failed'}), 500
        cursor = conn.cursor()
        query = "SELECT content FROM bazipaipan WHERE bazi = %s AND gender = %s"
        cursor.execute(query, (birth, gender))
        # 获取第一条数据
        row = cursor.fetchone()
        print(row)
        # 如果有数据，则打印
        if row:
            # 关闭连接
            cursor.close()
            conn.close()
            return jsonify(row[0])
        else:
            query = (f"请根据中国传统命理学分析八字：{birth}，性别：{gender}。\n"
                     f"请回答以下内容：\n"
                     f"1. **年柱**：\n"
                     f"   - 藏干（Hidden Stems）\n"
                     f"   - 自坐（Self-Sitting）\n"
                     f"   - 空亡（Void）\n"
                     f"2. **月柱**：\n"
                     f"   - 藏干（Hidden Stems）\n"
                     f"   - 自坐（Self-Sitting）\n"
                     f"   - 空亡（Void）\n"
                     f"3. **日柱**：\n"
                     f"   - 藏干（Hidden Stems）\n"
                     f"   - 自坐（Self-Sitting）\n"
                     f"   - 空亡（Void）\n"
                     f"4. **时柱**：\n"
                     f"   - 藏干（Hidden Stems）\n"
                     f"   - 自坐（Self-Sitting）\n"
                     f"   - 空亡（Void）\n\n"
                     f"自坐的类型是沐浴，，胎，养，。。。。藏干的类型是：壬正印，甲劫财。。。,丁十神"
                     f"请严格按照 **JSON 格式** 返回：\n"
                     f"{{\n"
                     f"  \"BaziAnalysis\": {{\n"
                     f"    \"YearPillar\": {{ \"HiddenStems\": \"xxx\", \"SelfSitting\": \"xxx\", \"Void\": \"xxx\" }},\n"
                     f"    \"MonthPillar\": {{ \"HiddenStems\": \"xxx\", \"SelfSitting\": \"xxx\", \"Void\": \"xxx\" }},\n"
                     f"    \"DayPillar\": {{ \"HiddenStems\": \"xxx\", \"SelfSitting\": \"xxx\", \"Void\": \"xxx\" }},\n"
                     f"    \"HourPillar\": {{ \"HiddenStems\": \"xxx\", \"SelfSitting\": \"xxx\", \"Void\": \"xxx\" }}\n"
                     f"  }}\n"
                     f"}}")

            askInfo = AskInfo()

            try:
                response_data = askInfo.ask(query)
                if ('Error' in response_data):
                    logger.error("API results contain error information and are not stored in the database.")
                else:
                    cursor.execute(
                        "INSERT INTO bazipaipan (bazi, content,gender, createtime) VALUES (%s, %s, %s, %s)",
                        (birth, response_data, gender, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    )

                conn.commit()
                cursor.close()
                conn.close()
                logger.info("AI Response: %s", response_data)

            except Exception as e:
                logger.error(f"Error calling askInfo.ask(): {e}", exc_info=True)
                return jsonify({"error": "Failed to fetch analysis"}), 500
            return jsonify(response_data)


    except ValueError as ve:
        return jsonify({"error": "Invalid request data", "details": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@getinformation_api.route('/get_location', methods=['GET'])
def get_location():
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)  # 获取 IP 地址
        response = requests.get(f"https://ipapi.co/{ip}/json/")  # 查询 IP 位置
        data = response.json()

        location_info = {
            "ip": ip,
            "city": data.get("city", "未知"),
            "region": data.get("region", "未知"),
            "country": data.get("country_name", "未知"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude")
        }
        return jsonify(location_info)
    except Exception as e:
        return jsonify({"error": "无法获取地理位置", "details": str(e)}), 500

from flask import request, jsonify
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

@getinformation_api.route('/calculateInfo', methods=['POST'])
def get_calculate_info():
    try:
        data = request.json
        logger.info("/calculateInfo Received request data: %s", data)

        if not data:
            return jsonify({"error": "No data provided"}), 400

        user = data.get("user", "").strip()
        if not user:
            return jsonify({"error": "User ID is required"}), 400

        # 连接数据库
        conn = get_db_connection()
        if conn is None:
            return jsonify({'message': 'Database connection failed'}), 500

        cursor = conn.cursor()
        query = "SELECT birth, gender FROM `recordbirth` WHERE fromuser = %s ORDER BY createtime DESC LIMIT 1"
        cursor.execute(query, (user,))  # 确保传入的是元组 `(user,)`

        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            birth_str, gender = row  # 获取生日和性别
            if not birth_str:
                return jsonify({"error": "Birth date not found"}), 404

            # 解析出生日期
            try:
                dt = datetime.strptime(birth_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return jsonify({"error": "Invalid birth date format"}), 400

            # 提取 年、月、日、时
            birth_date = (dt.year, dt.month, dt.day, dt.hour)

            # 确保 gender 只有 "male" 或 "female"
            gender = gender.lower()
            if gender not in ["male", "female"]:
                gender = "unknown"

            # 计算八字排盘
            analyzer = AstrologyAnalyzer(birth_date, gender)
            logger.info("八字排盘结果: %s", analyzer.bazi)

            return jsonify(analyzer.bazi+","+gender), 200

        return jsonify({"message": "No birth record found for this user"}), 404

    except Exception as e:
        logger.error("Error in /calculateInfo: %s", str(e))
        return jsonify({"error": "serve error", "details": str(e)}), 500
