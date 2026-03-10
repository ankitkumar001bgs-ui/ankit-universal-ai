import os
import requests
import json

# --- SETUP ---
API_KEY = "AIzaSyCUEOisgg7wW9PtvOPyp9wIOOpLes-Yz2s"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

def get_ai_response(user_text):
    payload = {
        "contents": [{"parts": [{"text": f"You are a smart AI friend of Ankit. Reply in friendly Hinglish. Question: {user_text}"}]}]
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "Bhai, internet check karo ya API key sahi dalo."

def search_files(name):
    path = "/storage/emulated/0/"
    matches = []
    print(f"🔍 Searching for '{name}'...")
    for root, dirs, files in os.walk(path):
        for file in files:
            if name.lower() in file.lower():
                matches.append(os.path.join(root, file))
    return matches

# --- MAIN LOOP ---
print("\n--- 🛡️ Ankit Smart AI Online ---")
while True:
    puchna = input("\nAnkit: ")
    
    if puchna.lower() in ['exit', 'bye', 'band karo']:
        print("AI: Bye Ankit bhai!")
        break
        
    elif 'search' in puchna.lower() or 'dhoondo' in puchna.lower():
        item = input("AI: Kya dhoondna hai? : ")
        results = search_files(item)
        if results:
            print(f"AI: Ankit bhai, {len(results)} files mili hain. Pehli 5 ye rahi:")
            for r in results[:5]: print(f"-> {r}")
        else:
            print("AI: Maaf karna bhai, kuch nahi mila.")
            
    else:
        # Chatting feature
        jawab = get_ai_response(puchna)
        print(f"AI: {jawab}")
