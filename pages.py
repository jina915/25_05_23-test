
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🧭", layout="centered")

# 제목
st.title("🧭 MBTI 기반 진로 추천")
st.markdown("당신의 MBTI를 선택하면, 어울리는 직업을 추천해 드릴게요! 😊")

# MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 추천 직업 데이터 (예시)
mbti_jobs = {
    "ISTJ": ["📊 회계사", "🧑‍⚖️ 법률 전문가", "📐 엔지니어"],
    "ISFJ": ["🧑‍🏫 교사", "🏥 간호사", "📚 사서"],
    "INFJ": ["🎨 예술가", "🧠 심리학자", "📖 작가"],
    "INTJ": ["🧪 과학자", "📈 전략 컨설턴트", "💻 개발자"],
    "ISTP": ["🔧 기계공", "🛠️ 기술자", "🚓 경찰관"],
    "ISFP": ["🎨 디자이너", "🎼 음악가", "🌿 플로리스트"],
    "INFP": ["📖 소설가", "🧘 상담사", "🎬 시나리오 작가"],
    "INTP": ["💡 발명가", "🖥️ 데이터 과학자", "🔬 연구원"],
    "ESTP": ["💼 세일즈 전문가", "🎙️ 방송인", "🚀 창업가"],
    "ESFP": ["🎤 연예인", "👗 스타일리스트", "🧳 여행 가이드"],
    "ENFP": ["💡 크리에이터", "📢 마케팅 전문가", "🎭 배우"],
    "ENTP": ["📊 기업가", "🎯 기획자", "🧠 전략가"],
    "ESTJ": ["📋 관리자", "🏗️ 건축가", "👮 공무원"],
    "ESFJ": ["🏥 의료보조", "🏫 교육행정가", "💼 HR 매니저"],
    "ENFJ": ["🧑‍🏫 교육자", "🌍 NGO 활동가", "🎤 연설가"],
    "ENTJ": ["📈 CEO", "🏦 금융분석가", "💼 프로젝트 매니저"]
}

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 💡", mbti_types)

# 결과 출력
if selected_mbti:
    st.markdown("---")
    st.subheader(f"🔍 {selected_mbti}에게 추천하는 직업은:")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
    st.markdown("🎉 멋진 진로를 향해 나아가보세요!")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ for 진로 탐색하는 여러분 by Streamlit")
