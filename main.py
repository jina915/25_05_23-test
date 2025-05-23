import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(page_title="나의 소개", page_icon=":wave:", layout="centered")

# --- ✏️ 여기를 수정하세요 ---
NAME = "정지나"
SCHOOL = "영동일 고등학교"
EMAIL = "23s079@ydi.hs.kr"
HOBBIES = ["영화 감상", "독서", "포토샵"]
PROFILE_IMG_PATH = "profile.jpg"  # 같은 폴더에 있는 이미지 파일 경로
# ---------------------------

# 제목
st.title(f"👋 안녕하세요! {NAME}입니다.")
st.markdown("나의 소개 페이지에 오신 것을 환영합니다!")

# 프로필 이미지
try:
    image = Image.open(PROFILE_IMG_PATH)
    st.image(image, caption=f"{NAME}의 프로필 사진", use_column_width=True)
except:
    st.warning("⚠️ 프로필 이미지를 불러올 수 없습니다. 경로를 확인해주세요.")

# 기본 정보
st.subheader("📄 기본 정보")
st.markdown(f"**이름**: {NAME}")
st.markdown(f"**학교**: {SCHOOL}")
st.markdown(f"**이메일**: [{EMAIL}](mailto:{EMAIL})")

# 취미
st.subheader("🎯 취미")
for hobby in HOBBIES:
    st.markdown(f"- {hobby}")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ by Streamlit")
