import os
import sys
import requests
import json
import time
import importlib
import subprocess

# 检查并安装缺失的库
def check_and_install_package(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# 检查并安装缺失的库
check_and_install_package("colorama")

from colorama import init, Fore, Back, Style

init()  # 初始化 colorama 库

API_BASE = 'https://api.closeai-asia.com/v1/chat/completions'
API_KEY = 'sk-kn8rVHdC8NlpjrWT8gfsQawK2USx8JWMIex1Midz1GK57Ib2'

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

    return assistant_response


if __name__ == "__main__":
    while True:
        input_text = input("/cd ")
        if input_text.lower() == "quit":
            break
        response_text = chat_with_gpt(input_text)
        # 在回复开头添加 "/cd t "
        response_text = "/cd t " + response_text
        # 分割回复并逐字显示
        for char in response_text:
            sys.stdout.write(Back.WHITE + Fore.BLUE + char + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.01)  # 模拟延迟
        print()  # 打印一个换行符，以便下一次输出在新的一行
