import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(page_title="나의 소개", page_icon=":wave:", layout="centered")

# 제목
st.title("👋 안녕하세요! 반갑습니다.")
st.markdown("나의 소개 페이지에 오신 것을 환영합니다!")

# 사이드바 - 프로필 이미지 업로드
st.sidebar.header("📸 프로필 사진")
uploaded_image = st.sidebar.file_uploader("사진을 업로드하세요", type=["jpg", "jpeg", "png"])
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="나의 프로필 사진", use_column_width=True)
else:
    st.sidebar.info("사진을 업로드해 주세요.")

# 기본 정보 입력
st.subheader("📄 기본 정보")
name = st.text_input("이름")
school = st.text_input("학교")
email = st.text_input("이메일")
hobby = st.text_area("취미 (여러 줄 가능)")

# 출력
if name or school or email or hobby:
    st.markdown("---")
    st.subheader("🧾 나에 대해")
    if name:
        st.markdown(f"**이름**: {name}")
    if school:
        st.markdown(f"**학교**: {school}")
    if email:
        st.markdown(f"**이메일**: {email}")
    if hobby:
        st.markdown(f"**취미**:\n{hobby}")

# 추가 기능: 간단한 연락 버튼
st.markdown("---")
if email:
    st.markdown(f"📬 [이메일로 연락하기](mailto:{email})")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ by Streamlit")
