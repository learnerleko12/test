import streamlit as st

# ✅ 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🧑‍🔬")

# ✅ 앱 제목
st.title("🧑‍🔬 MBTI로 과학자 친구를 만나고 이공계 진로를 추천받아보자!")
st.markdown("**너의 성격 유형에 맞는 과학자 친구와 진로를 찾아보아요 😊**")

# ✅ MBTI 데이터 (16유형 전체 포함)
# 아래 코드는 너무 길어져 생략했지만, 앞서 제공한 `scientist_data = {...}` 전체를 붙여넣으세요.
# ⬇️ 여기에서 시작
scientist_data = {
    "INTJ": {
        "name": "스티븐 호킹",
        "desc": "나는 우주의 비밀을 풀기 위해 매일 생각했어!",
        "emoji": "🧠🌌",
        "keywords": ["계획적", "분석적", "미래지향적"],
        "jobs": ["이론물리학자", "AI 연구원", "빅데이터 분석가"],
        "job_details": {
            "이론물리학자": "우주나 자연의 근본 원리를 수학적으로 탐구해요.",
            "AI 연구원": "기계가 스스로 판단하도록 인공지능 알고리즘을 만들어요.",
            "빅데이터 분석가": "대량의 데이터를 분석해 숨겨진 패턴을 찾아내요."
        }
    },
    # ... 15개 MBTI 유형 생략 (앞서 받은 전체 딕셔너리 내용을 그대로 복붙하세요)
    "ESFP": {
        "name": "빌 나이",
        "desc": "나는 과학을 재밌게 알리는 일을 했어!",
        "emoji": "🎤🧪",
        "keywords": ["사교적", "재미 추구", "감각적"],
        "jobs": ["과학 콘텐츠 제작자", "기술 홍보 전문가", "STEM 교육자"],
        "job_details": {
            "과학 콘텐츠 제작자": "과학을 쉽게 알려주는 영상이나 책을 만들어요.",
            "기술 홍보 전문가": "기술을 소개하고 홍보하는 일을 해요.",
            "STEM 교육자": "어린이·청소년에게 과학을 쉽게 가르쳐요."
        }
    }
}

# ✅ 선택 모드: 직접 선택 vs 설문
st.markdown("### 💡 먼저, 아래 중 하나를 선택하세요:")
mode = st.radio("MBTI를 직접 고르거나 설문을 통해 알아볼 수 있어요.", ["🔤 MBTI 직접 선택", "📝 간단 MBTI 설문"])

# MBTI 결정 변수
selected_mbti = None

if mode == "🔤 MBTI 직접 선택":
    selected_mbti = st.selectbox("👉 너의 MBTI 유형을 선택하세요:", list(scientist_data.keys()))
else:
    st.markdown("#### 🧠 아래 문항에 답해주세요!")

    ei1 = st.radio("1. 사람들과 있을 때 에너지가 생긴다", ["예", "아니오"], key="ei1")
    sn1 = st.radio("2. 상상보다 실제가 더 중요하다", ["예", "아니오"], key="sn1")
    tf1 = st.radio("3. 결정을 내릴 때 감정보다 논리를 따른다", ["예", "아니오"], key="tf1")
    jp1 = st.radio("4. 미리 계획하는 걸 좋아한다", ["예", "아니오"], key="jp1")
    ei2 = st.radio("5. 나는 혼자 있는 시간보다 친구들과의 시간이 더 좋다", ["예", "아니오"], key="ei2")
    sn2 = st.radio("6. 설명할 때 실제 예시를 자주 든다", ["예", "아니오"], key="sn2")
    tf2 = st.radio("7. 친구가 속상하면 일단 공감부터 한다", ["예", "아니오"], key="tf2")
    jp2 = st.radio("8. 해야 할 일은 미리 계획해서 처리하는 편이다", ["예", "아니오"], key="jp2")

    if st.button("👉 MBTI 테스트 결과 확인하기"):
        # 점수 계산
        e = [ei1, ei2].count("예")
        s = [sn1, sn2].count("예")
        t = [tf1, tf2].count("아니오")
        j = [jp1, jp2].count("예")

        mbti = ""
        mbti += "E" if e >= 1 else "I"
        mbti += "S" if s >= 1 else "N"
        mbti += "T" if t >= 1 else "F"
        mbti += "J" if j >= 1 else "P"

        selected_mbti = mbti
        st.success(f"🎯 당신의 MBTI 유형은 **{selected_mbti}** 입니다!")

# ✅ 결과 출력
if selected_mbti and selected_mbti in scientist_data:
    data = scientist_data[selected_mbti]

    st.markdown("---")
    st.markdown(f"### 👩‍🔬 과학자 친구: {data['name']} {data['emoji']}")
    st.write(f"**설명:** {data['desc']}")
    st.markdown("**성격 키워드:** " + ", ".join(data["keywords"]))

    st.markdown("### 🎯 어울리는 이공계 진로 추천:")
    for job in data["jobs"]:
        with st.expander(f"🔍 {job} 자세히 보기"):
            st.write(data["job_details"].get(job, "상세 정보가 준비 중이에요."))

    st.success("🎉 너와 잘 어울리는 과학자 친구와 진로를 찾았어요!")
