import streamlit as st
import openai

# 🔑 API 클라이언트 구성 (Project + Organization 지정)
client = openai.OpenAI(
    api_key="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",
    project="proj_oCt5LGaVEjXWxPyLLmUDL8yS",
    organization="org-5S9TCJj9up0nlCFz3G8ZlCP2"
)

# ✅ 앱 구성
st.set_page_config(page_title="밈 설명기", layout="centered")
st.title("🧠 오픈AI 밈 설명기")

# 📥 사용자 입력
meme_input = st.text_input("궁금한 밈의 이름을 입력하세요:")

# 🛠 프롬프트 구성 함수
def build_prompt(meme_name):
    return f"""
너는 인터넷 밈 전문가야. '{meme_name}'이라는 밈을 아래 세 가지 항목으로 한국어로 간단히 설명해줘:

1. 뜻
2. 유래
3. 사용 예시

친근하고 이해하기 쉽게 설명해줘.
"""

# 🤖 GPT 호출 함수
def query_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "너는 친근한 밈 설명가야."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ 오류 발생: {e}"

# ▶️ 실행 버튼
if st.button("밈 설명 요청") and meme_input:
    prompt = build_prompt(meme_input)
    result = query_gpt(prompt)
    st.markdown("### 📘 설명 결과")
    st.write(result)

# 🛠 버전 출력 (디버깅용)
st.write("🔧 openai 버전:", openai.__version__)
