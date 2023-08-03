import os
import sys
import requests
import json
import time

API_BASE = 'https://api.closeai-asia.com/v1/chat/completions'  # 修改了API的基础URL
API_KEY = 'sk-kn8rVHdC8NlpjrWT8gfsQawK2USx8JWMIex1Midz1GK57Ib2'  # 用你自己的API密钥替换这里


conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
]

def chat_with_gpt(input_text):
    global conversation_history
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    # 添加新的用户消息到对话历史
    conversation_history.append({"role": "user", "content": input_text})
    data = {
        "model": "gpt-3.5-turbo",  # 使用你想要的模型
        "messages": conversation_history
    }
    response = requests.post(API_BASE, headers=headers, data=json.dumps(data))  # 修改了请求的URL
    response.raise_for_status()
    response_data = response.json()
    # 添加模型的回复到对话历史
    assistant_response = response_data['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": assistant_response})

    # 输出AI回复开头的"AI: "，并返回剩余部分进行逐字输出
    return assistant_response[len("AI: "):]

if __name__ == "__main__":
    while True:
        input_text = input("You: ")
        if input_text.lower() == "quit":
            break
        response_text = chat_with_gpt(input_text)
        sys.stdout.write("unkonw: ")  # 输出开头的"AI: "
        sys.stdout.flush()
        for char in response_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # 模拟延迟
        print()  # 打印一个换行符，以便下一次输出在新的一行


if __name__ == "__main__":
    while True:
        input_text = input("You: ")
        if input_text.lower() == "quit":
            break
        response_text = chat_with_gpt(input_text)
        # 分割回复并逐字显示
        for char in response_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.001)  # 模拟延迟
        print()  # 打印一个换行符，以便下一次输出在新的一行
