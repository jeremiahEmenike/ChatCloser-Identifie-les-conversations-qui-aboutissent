import os
import json
import pandas as pd

def load_chats_from_directory(directory_path):
    data_rows = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            filepath = os.path.join(directory_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                chat_data = json.load(f)
                
                label = chat_data.get("label")
                messages = chat_data.get("messages", [])
                
                # Concaténer tout le contenu des messages
                all_content = " ".join(msg.get("content", "") for msg in messages)
                
                data_rows.append({
                    "label": label,
                    "text": all_content
                })
    return pd.DataFrame(data_rows)

if __name__ == "__main__":
    directory_path = "./data/chats"  # à adapter selon ton organisation
    df = load_chats_from_directory(directory_path)
    print(df.head())
