import os
import sys
import requests
import json
import time

API_BASE = 'https://api.closeai-asia.com/v1/chat/completions'
API_KEY = 'sk-kn8rVHdC8NlpjrWT8gfsQawK2USx8JWMIex1Midz1GK57Ib22'

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
]

def chat_with_gpt(input_text):
    global conversation_history
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    conversation_history.append({"role": "user", "content": input_text})
    data = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history
    }
    response = requests.post(API_BASE, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    response_data = response.json()
    assistant_response = response_data['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": assistant_response})

    # 输出AI回复开头的"AI: "，并返回剩余部分进行逐字输出
    return assistant_response[len("/cd t "):]


if __name__ == "__main__":
    while True:
        input_text = input("/cd ")
        if input_text.lower() == "quit":
            break
        response_text = chat_with_gpt(input_text)
        # 分割回复并逐字显示
        for char in response_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)  # 模拟延迟
        print()  # 打印一个换行符，以便下一次输出在新的一行
