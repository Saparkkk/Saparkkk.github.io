import streamlit as st
import pandas as pd

# กำหนดขนาดตารางข้อมูล
st.set_page_config(
    layout="wide",  # กำหนดเป็น wide เพื่อให้ตารางข้อมูลขยายตัวเต็มหน้าจอ
    initial_sidebar_state="expanded"  # กำหนดให้ sidebar เปิดอยู่เสมอ
)

# สร้างข้อมูลตัวอย่าง
data = {
    'หัวข้อ': ['เรื่องน่าสนใจ', 'ความรู้สึก', 'คะแนน'],
    'รีวิว': ['เรื่องนี้น่าสนใจมาก แนวซอมบี้ที่ไม่ซ้ำใคร', 'รู้สึกตื่นเต้นและรอคอยตอนต่อไป', 9.5],
    'Movie': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight'],
    'Category': ['Drama', 'Crime', 'Action'],
    'Poster' : ['https://markpeak.net/wp-content/uploads/2022/03/shawshank-700x394.jpg', 
                'https://img.monomax.me/-XnASaiSaflF2FV3NDZwMvnRo4k=/monomax-obj.obs.ap-southeast-2.myhuaweicloud.com/assets/fileupload/picture/the-godfather-508d945641aed.jpg', 
                'https://static.tvtropes.org/pmwiki/pub/images/rsz_tdkrposter29_2001.jpg']
    
}

# แปลงข้อมูลเป็น DataFrame
df = pd.DataFrame(data)

# สร้างเว็บแอป
st.title('เว็บรีวิวหนัง')
st.write('แสดงรีวิวหนัง')

movie_title = st.text_input('ชื่อหนัง')
movie_review = st.text_area('รีวิว')
movie_rating = st.slider('คะแนน', min_value=0.0, max_value=10.0, step=0.5)

# สร้าง DataFrame ของรีวิว
review_data = {
    'หัวข้อ': ['ชื่อหนัง', 'รีวิว', 'คะแนน'],
    'ข้อมูล': [movie_title, movie_review, movie_rating]
}

review_df = pd.DataFrame(review_data)

# แสดงรีวิวที่ผู้ใช้กรอก
st.write(review_df)

# แสดงข้อมูลในตาราง
st.write(df)

# สร้าง dropdown สำหรับเลือกหมวดหนัง
category = st.selectbox('Select a category', df['Category'].unique())

for index, row in df[df['Category'] == category].iterrows():
    st.image(row['Poster'], caption=row['Movie'], use_column_width=True)
    st.caption(f"Movie: {row['Movie']} - Category: {row['Category']}")
