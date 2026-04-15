import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_all_definitions(word):
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            if not data or not isinstance(data[0], dict):
                return ["No definitions found."]

            all_meanings = []
            
            # Loop through every dictionary entry (e.g., 'break' as verb, 'break' as noun)
            for entry in data:
                part_of_speech = entry.get('fl', 'n/a') # fl = functional label
                short_defs = entry.get('shortdef', [])
                
                if short_defs:
                    # Format: "verb: to separate into parts; to fracture"
                    meaning_line = f"[{part_of_speech.upper()}] " + " | ".join(short_defs)
                    all_meanings.append(meaning_line)
            
            return all_meanings
        else:
            return [f"Error: {response.status_code}"]
    except Exception as e:
        return [f"Request failed: {e}"]

def save_detailed_dictionary(word_list, filename="detailed_definitions.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for word in word_list:
            print(f"Deep searching: {word}...")
            meanings = get_all_definitions(word)
            
            f.write(f"WORD: {word.upper()}\n")
            for m in meanings:
                f.write(f"  - {m}\n")
            f.write("-" * 40 + "\n")
    
    print(f"\nFinished! Open '{filename}' to see the full list.")

if __name__ == "__main__":
    my_words = ["break", "set", "run"] # These words have the most meanings in English!
    save_detailed_dictionary(my_words)