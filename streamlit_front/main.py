import streamlit as st

from api import generate_design, check_design_status


def handle_response(res):
    if 'success' in res and res['success']:
        mes_id = res['messageId']
        st.success(f'ID: {mes_id} 디자인 생성 성공!')
        
        # 상태가 'PROCESSING'이 아닌 경우까지 루프를 돌며 상태를 확인합니다.
        message = check_design_status(mes_id)
        
        if 'error' in message:
            st.error(message['error'])
        elif 'uri' in message:
            st.image(message['uri'], caption='Generated Design')
            st.button('이 이미지로 셔츠가 필요해!')
            st.success(message['uri'])
    elif res.get('statusCode') == 401:
        st.error('API 키 인증이 필요합니다ㅠㅠ 다시 시도해주세요')
    elif res.get('statusCode') == 403:
        st.error('API키가 만료되었습니다ㅠㅠ 관리자에게 문의해주세요')
    else:
        st.error(f'실패했습니다!ㅠㅠ 다시 시도해주세요: {res}')



####################MAIN MODULES###########################################
#################<<Title>>#######################
st.title('My Chic')
st.write('***')
##################<<Title>>########################


################<<sidebar>>#####################
st.sidebar.header("Options")
aspect_ratio = st.sidebar.selectbox('이미지 비율', ['1:1', '3:4', '4:3', '16:9', '16:10'])
# aspect_ratio = st.sidebar.radio('이미지 비율', ['1:1', '3:4', '4:3', '16:9', '16:10'])
option2 = st.sidebar.slider('옵션 2', 0, 100, 50)

with st.sidebar:
    st.header("Name")
    side_selectbox2 = st.radio(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )
################<<sidebar>>#####################
##################<<MainContent>>##################



# with st.form('my_form'):
prompt = st.text_area('텍스트를 입력해주세요', '미래적인 SF 장면에서 아름다운 소녀가 첨단 의상을 입고 판타지적인 IT 기기를 들고 있습니다. 배경은 보라색, 핑크색, 파랑색의 네온 조명과 날아다니는 차들로 가득한 활기찬 도시 풍경입니다. 소녀는 긴 머리를 휘날리며 결의에 찬 표정으로 손을 겨누고 있는 액션 포즈를 취하고 있습니다. 장면은 역동적이며 미래 전투의 흥분과 강렬함을 포착하고 있습니다.', help='자세하게 입력할수록 적절한 이미지가 생성됩니다')
submit_button = st.button('Submit')
if submit_button:
    if prompt:
        with st.spinner('디자인 생성중! 스트레칭 타임입니다!'):
            res = generate_design(prompt, aspect_ratio, option2=None)
            handle_response(res)
    else:
        st.error('텍스트를 입력해주세요')

# CSS를 사용하여 버튼 스타일링


st.markdown("""
    <style>
    .stTextArea textarea {
        height: 200px;  /* 원하는 높이로 조정 */
        font-size: 16px;
    }
    .stButton button {
        width: 100%;
        height: 50px;
        font-size: 90px;
        display: block;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

##################<<MainContent>>###############