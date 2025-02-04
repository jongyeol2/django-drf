from openai import OpenAI
from api_pjt import config

CLIENT = OpenAI(
    api_key=config.OPENAI_API_KEY,
)



def ask_chatgpt(user_message):
    system_instructions = """
    이제부터 너는 "영어, 한글 번역가"야. 
    지금부터 내가 입력하는 모든 프롬프트를 무조건 한글은 영어로, 영어는 한글로 번역해줘. 
    프롬프트의 내용이나 의도는 무시하고 오직 번역만 해줘.
    """
    
    completion = CLIENT.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_instructions,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )
    return completion.choices[0].message.content


while True:
    user_input = input("번역기 : ")
    if user_input == "exit":
        break
    response = ask_chatgpt(user_input)
    print("챗봇 : ", response, "\n\n")




