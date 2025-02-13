from flask import Flask, request, jsonify, send_from_directory, session
from flask_cors import CORS
import os

# ✅ 导入 API 蓝图
from src.api.getinformation import getinformation_api
from src.api.Register import register_api
from src.bean.Constant import Constant

app = Flask(__name__, static_folder="frontend/dist", template_folder="frontend/dist")

# ✅ 设置 SECRET_KEY 以支持 session
app.secret_key = os.getenv("FLASK_SECRET_KEY", Constant.AES_KEY)  # 确保 session 可用

# ✅ 允许前端携带 session 并指定跨域源
# CORS(app, supports_credentials=True, origins=["http://localhost:8000"])  # 确保与前端一致
CORS(app, supports_credentials=True, origins=["http://13.229.224.223:5000"])  # 确保与前端一致

# ✅ 注册 API 蓝图
app.register_blueprint(getinformation_api, url_prefix="/getinformation")

app.register_blueprint(register_api, url_prefix="/api")

@app.after_request
def after_request(response):
    """ 确保所有请求都返回 CORS 头 """
    # response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"  # 必须匹配前端域名
    response.headers["Access-Control-Allow-Origin"] = "http://13.229.224.223:5000"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

# ✅ 处理 OPTIONS 预检请求，避免 CORS 405 错误
@app.route('/api/<path:dummy>', methods=['OPTIONS'])
def options_handler(dummy):
    return '', 204

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    """ 让 Flask 返回前端静态页面 """
    frontend_path = os.path.join(app.template_folder, path)

    if path and os.path.exists(frontend_path):
        return send_from_directory(app.template_folder, path)

    return send_from_directory(app.template_folder, "index.html")

if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000, debug=False)
