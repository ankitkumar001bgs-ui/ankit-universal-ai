import os
import google.generativeai as genai

# Yahan apni API Key daal dena Ankit bhai
genai.configure(api_key="AIzaSyDtc65QYocAgE_xblwkm_EYVPAXOp7Tdug")
model = genai.GenerativeModel('gemini-1.5-flash')

def find_files_logic(filename):
    # System scanning logic
    path = "/storage/emulated/0/" if os.name != 'nt' else "C:/"
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if filename.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

def start_chat():
    print("--- 🛡️ Ankit's Smart AI (Termux Edition) ---")
    print("AI: Hello Ankit bhai! Kaise ho? Main online hoon.")
    
    while True:
        user_input = input("Ankit: ").lower()

        if 'exit' in user_input or 'bye' in user_input:
            print("AI: Bye Ankit bhai! Phir milenge.")
            break
        
        elif 'search' in user_input or 'dhoondo' in user_input:
            file_to_find = input("AI: Kaunsi file dhoondni hai? : ")
            results = find_files_logic(file_to_find)
            if results:
                print(f"AI: Ankit bhai, mujhe {len(results)} files mili hain.")
                for r in results[:5]: print(f"-> {r}")
            else:
                print("AI: Maaf karna bhai, kuch nahi mila.")
        
        else:
            # Normal Baatein (Gemini AI se)
            response = model.generate_content(f"User is Ankit. Respond in Hinglish like a smart friend. User says: {user_input}")
            print(f"AI: {response.text}")

if __name__ == "__main__":
    start_chat()
