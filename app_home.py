import streamlit as st

def run_home_app() :
    st.subheader('!!!Welcome!!!.')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.' )
    st.text('데이터분석 및 고객 정보를 넣으면, 얼마정도의 차를 구매할지를 예측해 줍니다.')
    
    img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20221125_150%2F1669362759043l3Dmh_JPEG%2F70498538767715080_1128182524.jpg&type=sc960_832'
    
    st.image(img_url)
