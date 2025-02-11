from openai import OpenAI

from src.rules.AstrologyAnalyzer import AstrologyAnalyzer
import datetime

class FortuneTellerAPI:
    def __init__(self,  base_url: str = "https://api.deepseek.com"):
        """
        Initialize the FortuneTellerAPI client with an API key and optional base URL.
        """
        # 从 txt 文件中读取 API 密钥
        # try:
        #     with open("api_key.txt", "r") as file:
        #         api_key = file.read().strip()
        # except FileNotFoundError:
        #     raise ValueError("API key file 'api_key.txt' not found. Please create the file and add your API key.")
        # except Exception as e:
        #     raise ValueError(f"Error reading API key from file: {str(e)}")

        # 初始化 OpenAI 客户端
        self.client = OpenAI(api_key="sk-7a4f554fde844054861941acbce554bf", base_url=base_url)

    def get_fortune(self,
                    birth_date: str,
                    birth_place: str,
                    gender:str,
                    bazi: str,
                    race:str) -> str:
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
                # f"请根据出生日期为{birth_date} {birth_time}出生的时间，八字排盘为{bazi},出生地为{birth_place}，请根据{bazi}八字排盘算一下。"
                # f"1.八字排盘。2.五行分析。3.日主性格分析，优点，缺点，做事风格等。4.十神分析。5.大运分析。6.性格特点。7.事业与财运。8.健康。9.婚姻与家庭。10.建议。其中3.日主分析。"
                # f"4.十神分析。5.大运分析。6.性格特点。7.事业与财运。8.健康。9.婚姻与家庭。10.建议。除了理论分析，还要将理论分析修改成通俗易懂的话，使得非"
                # f"专业人员能听懂，2000字左右，返回格式每个点都是单独一行重新开始"
                f"请根据出生日期为{birth_date} 出生的时间，八字排盘为{bazi},性别{gender},种族为:{race},出生地为{birth_place}，请根据{bazi}八字排盘算一下。"
                f"性格简述"
                # f"字数为2000字以上"
                # f"学业，财富，事业，婚姻"
            )

            # Send the request to the OpenAI API
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are an experienced fortune-teller"},
                    {"role": "user", "content": user_message},
                ],
                stream=False
            )
            print(response.choices[0].message.content)
            # Extract and return the result from the response
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual API key
    birth_date = (1994, 10, 14, 9)

    gender = 'male'
    fortune_teller = FortuneTellerAPI()
    analyzer = AstrologyAnalyzer(birth_date,gender)
    print(analyzer.bazi)
    # Call the get_fortune method
    result = fortune_teller.get_fortune(
        birth_date="1994-10-14 23:00:00",
        birth_place="安徽省",
        gender=gender,
        bazi=analyzer.bazi,
        race='汉族'
    )
    print(result)


