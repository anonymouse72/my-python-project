from flask import Flask, request, jsonify
from flask_cors import CORS
from src.API.ChatInfoAPI import ChatInfoAPI
from src.rules.AstrologyAnalyzer import AstrologyAnalyzer
from src.API.FortuneTellerAPI import FortuneTellerAPI

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

def parse_int(value, default=0):
    """尝试将值转换为整数，失败则返回默认值"""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

@app.route('/', methods=['GET'])
def index():
    year = parse_int(request.args.get('year'))
    month = parse_int(request.args.get('month'))
    day = parse_int(request.args.get('day'))
    hour = parse_int(request.args.get('hour'))
    minutes = request.args.get('minutes', None)
    location = request.args.get('location', "")

    if not all([year, month, day, hour]):
        return jsonify({"error": "Invalid or missing parameters"}), 400

    birth_date = (year, month, day, hour)
    gender = 'male'
    fortune_teller = FortuneTellerAPI()
    analyzer = AstrologyAnalyzer(birth_date, gender)

    result = fortune_teller.get_fortune(
        birth_date=f"{year}-{month}-{day}",
        birth_time=f"{hour}:00",
        birth_place=location,
        bazi=analyzer.bazi
    )
    return jsonify(result)

@app.route('/api/getChatInfo', methods=['POST'])
def get_chat_info():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    print("Received data:", data)
    result = ChatInfoAPI().get_chatContent(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
