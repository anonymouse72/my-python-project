from openai import OpenAI

from src.rules.AstrologyAnalyzer import AstrologyAnalyzer
import datetime

class Method:
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

    def get_fortune(self) -> str:
        """
        Get the fortune-telling response based on the provided birth information.

        Parameters:
            birth_date (str): The birth date in the format 'YYYY-MM-DD'.
            birth_time (str): The birth time in the format 'HH:MM'.
            birth_place (str): The birth place as a string.

        Returns:
            str: The response from the fortune-telling API.
        """
        try:
            # Construct the query content for the fortune-telling API
            user_message = (
                f"""

                """
            )

            # Send the request to the OpenAI API
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are an experienced SCI reviewer"},
                    {"role": "user", "content": user_message},
                ],
                stream=False
            )

            # Extract and return the result from the response
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual API key
    birth_date = (1995, 10, 1, 12)

    gender = 'female'
    fortune_teller = Method()

    # Call the get_fortune method
    result = fortune_teller.get_fortune()
    print(result)


