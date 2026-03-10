import os
import requests
import json
import time

# --- 🔑 APNI API KEY YAHAN DALO ---
API_KEY = "AIzaSyCUEOisgg7wW9PtvOPyp9wIOOpLes-Yz2s"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

def brain(user_input):
    headers = {'Content-Type': 'application/json'}
    # AI ko instruction de rahe hain ki wo Ankit ka dost hai
    prompt = f"You are a smart, funny and helpful AI best friend of Ankit. Talk in friendly Hinglish. Always address him as Ankit bhai. User says: {user_input}"
    
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    try:
        response = requests.post(URL, headers=headers, data=json.dumps(data))
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception:
        return "Ankit bhai, lagta hai internet slow hai ya API key mein locha hai."

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

# --- STARTING THE ENGINE ---
clear_terminal()
print("\033[1;32m" + "="*40)
print("🛡️  ANKIT'S PERSONAL AI SYSTEM ONLINE  🛡️")
print("="*40 + "\033[0m")
print("\033[1;34mAI: Namaste Ankit bhai! Main taiyar hoon. Boliye, kya sewa karun?\033[0m")

while True:
    try:
        user_msg = input("\n\033[1;37mAnkit Bhai > \033[0m")
        
        if user_msg.lower() in ["exit", "bye", "band karo", "so jao"]:
            print("\033[1;31mAI: Thik hai Ankit bhai, apna khayal rakhna. Milte hain!\033[0m")
            break
            
        if user_msg.strip() == "":
            continue

        print("\033[1;33mThinking...\033[0m", end="\r")
        
        # AI se jawab mangna
        answer = brain(user_msg)
        
        # Typing effect
        print("\033[1;32mAI:\033[0m ", end="")
        for char in answer:
            print(char, end="", flush=True)
            time.sleep(0.01)
        print()
        
    except KeyboardInterrupt:
        print("\nAI: Bye Ankit bhai!")
        break
