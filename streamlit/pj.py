import streamlit as st
import random

# รายการคำที่ใช้ในเกม
words = ["apple", "banana", "cherry", "date", "elderberry"]

# สุ่มคำจากรายการคำ
word = random.choice(words)

# สร้างเว็บแอปพลิเคชัน
st.title("เกมทายคำ")
st.write("คำที่ต้องการให้เดามีจำนวนตัวอักษร " + str(len(word)))

# สร้างช่องใส่คำ
guess = st.text_input("กรุณาใส่คำที่คุณเดา")

# เช็คว่าคำที่เดาถูกต้องหรือไม่
if guess.lower() == word.lower():
    st.write(f"ยินดีด้วย! คำที่คุณเดาถูกต้อง คำที่เราคิดคือ '{word}'")
else:
    st.write("คำที่คุณเดาไม่ถูกต้อง โปรดลองอีกครั้ง")

def set_background(image_url):
    image_url_str = f'url("{image_url}")'
    css = f"""
    <style>
    .stApp {{
        background-image: {image_url_str};
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


##ใช้งานตรงนี้
set_background("https://wallpapers.com/images/hd/anime-meme-background-w13zt6adj4t13chk.jpg")