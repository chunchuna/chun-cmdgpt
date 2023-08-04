import os
from datetime import datetime

def save_chat_record(conversation_history):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"save/{conversation_history[1]['content'][:5]}_{current_time}.txt"
    os.makedirs("save", exist_ok=True)
    with open(filename, "w") as file:
        for message in conversation_history:
            role = message["role"]
            content = message["content"]
            file.write(f"{role}: {content}\n")

def read_chat_record():
    save_folder = "save"
    chat_files = sorted(os.listdir(save_folder))
    if not chat_files:
        print("No chat records found.")
        return
    print("=== Chat Records ===")
    for i, file in enumerate(chat_files):
        print(f"{i+1}. {file}")
    file_index = input("Enter the index of the chat record to read: ")
    try:
        file_index = int(file_index)
        if 1 <= file_index <= len(chat_files):
            selected_file = chat_files[file_index - 1]
            filepath = os.path.join(save_folder, selected_file)
            with open(filepath, "r") as file:
                content = file.read()
                print(content)
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

