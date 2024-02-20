import streamlit as st

st.header('My OOP comp')
st.subheader('private web')
st.write('สร้างยากโพด')
st.image('https://www.chromethemer.com/wallpapers/chromebook-wallpapers/images/960/cyberpunk-chromebook-wallpaper.jpg')

st.button('click me')
text = st.text_input('prompt: ')
if text:
    st.write(f'กำลังสร้างมองข้ามไปก่อน...{text}')
    st.button('ไปต่อหรือพอส่ำนี้')