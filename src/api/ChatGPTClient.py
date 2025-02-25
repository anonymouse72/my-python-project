import openai

from src.bean.Constant import Constant

# ✅ 直接定义 API Key 常量（请替换为你的真实 API Key）
API_KEY = Constant.CONV_KEY

class ChatGPTClient:
    def __init__(self):
        openai.api_key = API_KEY  # 直接使用常量 API_KEY

    # 定义与 ChatGPT 交互的函数
    def query(self, user_message):
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 确保使用正确的模型 ID
            messages=[{"role": "user", "content": user_message}]
        )

        # 提取并返回 AI 的回复内容
        message = response['choices'][0]['message']['content']
        return message

# 使用封装的类进行查询
if __name__ == "__main__":
    chat_client = ChatGPTClient()

    query_content = "乙亥乙酉乙丑壬午，女性，请对这个进行一个八字排盘，性格简述"
    result = chat_client.query(query_content)

    print(f"用户查询: {query_content}")
    print(f"ChatGPT 回复: {result}")
