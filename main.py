import streamlit as st
import openai

# ✅ 최신 방식으로 클라이언트 객체 생성
client = openai.OpenAI(
    api_key="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",  # 너의 키
    project="proj_oCt5LGaVEjXWxPyLLmUDL8yS",
    organization="org-5S9TCJj9up0nlCFz3G8ZlCP2"
)

st.set_page_config(page_title="밈 설명기", layout="centered")
st.title("🧠 오픈AI 밈 설명기")

meme_input = st.text_input("궁금한 밈 이름을 입력하세요:")

def build_prompt(meme_name):
    return f"""
너는 인터넷 밈 전문가야. '{meme_name}'이라는 밈을 아래 세 가지 항목으로 한국어로 간단히 설명해줘:

1. 뜻
2. 유래
3. 사용 예시

친근하고 이해하기 쉽게 설명해줘.
"""

def query_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "너는 친근한 밈 설명가야."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[❌ 에러 발생] {e}"

if st.button("밈 설명 요청") and meme_input:
    prompt = build_prompt(meme_input)
    result = query_gpt(prompt)
    st.markdown("### 📘 설명 결과")
    st.write(result)
    st.write("🧪 OpenAI 라이브러리 버전:", openai.__version__)
