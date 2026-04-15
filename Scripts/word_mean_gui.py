import requests
import tkinter as tk
from tkinter import ttk, messagebox

API_KEY = "YOUR_API_KEY_HERE"

def get_all_definitions(word):
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            if not data or not isinstance(data[0], dict):
                return "No definitions found."
            
            all_meanings = []
            
            for entry in data:
                part_of_speech = entry.get('fl', 'n/a')
                short_defs = entry.get('shortdef', [])
                
                if short_defs:
                    meaning_line = f"[{part_of_speech.upper()}] " + " | ".join(short_defs)
                    all_meanings.append(meaning_line)
            
            return "\n".join(all_meanings)
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Request failed: {e}"

def search_word():
    word = entry.get().strip()
    if not word:
        messagebox.showwarning("Input Required", "Please enter a word to search.")
        return
    
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", f"Searching for '{word}'...")
    result_text.config(state=tk.DISABLED)
    root.update()
    
    meanings = get_all_definitions(word)
    
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", meanings)
    result_text.config(state=tk.DISABLED)

def on_enter(event):
    search_word()

root = tk.Tk()
root.title("Dictionary Lookup")
root.geometry("500x400")
root.resizable(True, True)

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(main_frame, text="Enter a word:", font=("", 12)).pack(anchor=tk.W)

input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=(5, 10))

entry = ttk.Entry(input_frame, font=("", 14))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.bind("<Return>", on_enter)

search_btn = ttk.Button(input_frame, text="Search", command=search_word)
search_btn.pack(side=tk.LEFT, padx=(5, 0))

ttk.Label(main_frame, text="Definitions:", font=("", 12)).pack(anchor=tk.W)

result_text = tk.Text(main_frame, wrap=tk.WORD, font=("", 11), state=tk.DISABLED)
result_text.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_text, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

if __name__ == "__main__":
    root.mainloop()
