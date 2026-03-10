import streamlit as st
import os
import platform

st.set_page_config(page_title="Aman AI - System Finder", page_icon="🔍")

st.title("🛡️ Aman's Universal System Data Finder")
st.markdown("---")

# Device Information
st.sidebar.header("Connected Device")
st.sidebar.write(f"**OS:** {platform.system()}")
st.sidebar.write(f"**Node:** {platform.node()}")

# Search UI
query = st.text_input("Bhai, kya dhoondna hai? (File ka naam)", placeholder="e.g. results, bill, secret")
path_to_search = st.text_input("Search Path (Laptop: C:/ or D:/ | Phone: /storage/emulated/0/)", value="C:/")

if st.button("Deep Scan Start"):
    if query:
        st.write(f"🔎 Searching for '{query}' in {path_to_search}...")
        found_files = []
        try:
            for root, dirs, files in os.walk(path_to_search):
                for file in files:
                    if query.lower() in file.lower():
                        found_files.append(os.path.join(root, file))
            
            if found_files:
                st.success(f"Bhai, {len(found_files)} files mili hain!")
                for f in found_files:
                    st.code(f)
            else:
                st.error("Nahi mila bhai! Shayad naam galat hai ya permission nahi hai.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch type toh karo!")
