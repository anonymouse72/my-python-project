# from openai import OpenAI
import openai

from src.bean.Constant import Constant


class AskInfo:
    def __init__(self, base_url: str = Constant.BASE_URL):
        """
        Initialize the AskInfo client without requiring API key input.
        """
        self.client = OpenAI(api_key=Constant.API_KEY, base_url=base_url)

    def ask(self, query: str) -> str:
        """
        Send a query to the API and return the response.
        """
        try:
            response = self.client.chat.completions.create(
                model=Constant.MODEL,
                messages=[
                    {"role": "system", "content": Constant.SYSTEM_ROLE},
                    {"role": "user", "content": query},
                ],
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"{Constant.ERROR_MESSAGE}: {str(e)}"


# Example usage
if __name__ == "__main__":
    ask_info = AskInfo()

    query = "请根据中国传统命理学分析八字：乙亥乙酉乙丑壬午，性别：female。请提供详细的排盘信息，包括天干、地支、藏干、副星、星运、自坐、空亡、纳音、神煞等，并以 JSON 格式返回。"
    result = ask_info.ask(query)
    print(result)
