import streamlit as st

def run_home_app() :
    st.text('환영합니다.')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.' )
    st.text('데이터분석 및 고객 정보를 넣으면, 얼마정도의 차를 구매할지를 예측해 줍니다.')
    
    img_url = 'https://www.google.com/imgres?imgurl=http%3A%2F%2Fcarvatar.co.kr%2Fresources%2Fnew%2Fimg%2Fpage%2Fimg%2Fkona_big.png&imgrefurl=http%3A%2F%2Fcarvatar.co.kr%2F&tbnid=TFDKCFPey5ofHM&vet=12ahUKEwj7rNGwgfb7AhVE6ZQKHTq4CgMQMygNegUIARDdAg..i&docid=GF6hXbdLVohZwM&w=794&h=398&q=%EC%9E%90%EB%8F%99%EC%B0%A8&ved=2ahUKEwj7rNGwgfb7AhVE6ZQKHTq4CgMQMygNegUIARDdAg'
    st.image(img_url)
