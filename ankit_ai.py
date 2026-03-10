import os
import platform

def search_files(name, start_path):
    print(f"\n🔍 Ankit bhai, searching for '{name}' in {start_path}...")
    results = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if name.lower() in file.lower():
                p = os.path.join(root, file)
                results.append(p)
                print(f"✅ Found: {p}")
    return results

if __name__ == "__main__":
    print(f"--- 🛡️ Ankit Universal AI (OS: {platform.system()}) ---")
    
    # Path setup
    if platform.system() == "Linux": # Android/Termux
        path = "/storage/emulated/0/"
    else: # Windows
        path = "C:/"

    query = input("Bhai, kya dhoondna hai? : ")
    res = search_files(query, path)
    
    if not res:
        print("❌ Kuch nahi mila bhai.")
    else:
        print(f"\nDone! Total {len(res)} items mile.")
