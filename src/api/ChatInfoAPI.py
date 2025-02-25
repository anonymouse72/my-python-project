from openai import OpenAI

from src.rules.AstrologyAnalyzer import AstrologyAnalyzer
import datetime

class ChatInfoAPI:
    def __init__(self,  base_url: str = "https://api.deepseek.com"):
        """
        Initialize the FortuneTellerAPI client with an API key and optional base URL.
        """
        # 从 txt 文件中读取 API 密钥
        try:
            with open("api_key.txt", "r") as file:
                api_key = file.read().strip()  # 读取并去除可能的空白字符
        except FileNotFoundError:
            raise ValueError("API key file 'api_key.txt' not found. Please create the file and add your API key.")
        except Exception as e:
            raise ValueError(f"Error reading API key from file: {str(e)}")

        # 初始化 OpenAI 客户端
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def get_chatContent(self, data: str) -> str:
        print(data, '接口里')
        try:


            # Send the request to the OpenAI API
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are an experienced fortune-teller"},
                    {"role": "user", "content": data},
                ],
                stream=False
            )
            print(data,'接口里')
            # Extract and return the result from the response
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"



