import streamlit as st
import pandas as pd

# สร้างข้อมูลเริ่มต้น
movies_data = {
    'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight'],
    'Director': ['Frank Darabont', 'Francis Ford Coppola', 'Christopher Nolan'],
    'Year': [1994, 1972, 2008],
    'Rating': [9.3, 9.2, 9.0]
}

# สร้าง DataFrame จากข้อมูลเริ่มต้น
movies = pd.DataFrame(movies_data)

# สร้างหน้าเว็บ
st.title('Movie Review Community')
st.write('Welcome to our movie review community!')
st.write('Here are the top movies:')
st.write(movies)

# เก็บข้อมูลใน Session State
if 'movies_list' not in st.session_state:
    st.session_state.movies_list = movies_data

# เพิ่มรีวิวใหม่
st.subheader('Add a New Review')
title = st.text_input('Movie Title')
director = st.text_input('Director')
year = st.number_input('Year', min_value=1900, max_value=2025)
rating = st.slider('Rating', min_value=0.0, max_value=10.0, step=0.1)
submit = st.button('Submit Review')

if submit:
    new_review = {
        'Title': title,
        'Director': director,
        'Year': year,
        'Rating': rating
    }
    # เพิ่มข้อมูลใหม่เข้ารายการข้อมูลใน Session State
    st.session_state.movies_list['Title'].append(new_review['Title'])
    st.session_state.movies_list['Director'].append(new_review['Director'])
    st.session_state.movies_list['Year'].append(new_review['Year'])
    st.session_state.movies_list['Rating'].append(new_review['Rating'])
    st.write('New review added successfully!')
    st.write(pd.DataFrame(st.session_state.movies_list))
