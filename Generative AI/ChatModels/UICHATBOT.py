import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

st.set_page_config(
    page_title="Rohan's GPT",
    page_icon="🤖",
    layout="centered",
)

SYSTEM_PROMPT = "You are a funny AI Agent"

st.markdown(
    """
    <style>
    .stChatMessage { border-radius: 14px; }
    header[data-testid="stHeader"] { background: transparent; }
    .block-container { padding-top: 2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🤖 Rohan's GPT")
st.caption("Powered by Mistral · mistral-small-2506")

PERSONA_OPTIONS = {
    "😂 Funny AI Agent": "You are a funny AI Agent",
    "🧑‍💼 Professional Assistant": "You are a professional, concise, and helpful assistant.",
    "👨‍💻 Coding Expert": "You are an expert software engineer who gives precise, well-explained code answers.",
    "😏 Sarcastic Bot": "You are a witty, sarcastic AI that answers correctly but with dry humor.",
    "🧘 Friendly Mentor": "You are a warm, encouraging mentor who explains things simply and patiently.",
    "✍️ Custom": None,
}

if "persona" not in st.session_state:
    st.session_state.persona = "😂 Funny AI Agent"
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = PERSONA_OPTIONS[st.session_state.persona]

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=st.session_state.system_prompt)]

with st.sidebar:
    st.header("⚙️ Settings")

    selected_persona = st.selectbox(
        "AI Persona",
        list(PERSONA_OPTIONS.keys()),
        index=list(PERSONA_OPTIONS.keys()).index(st.session_state.persona),
        help="Pick a preset personality, or choose Custom to write your own.",
    )

    if selected_persona == "✍️ Custom":
        new_system_prompt = st.text_area(
            "Custom System Message",
            value=st.session_state.system_prompt if st.session_state.persona == "✍️ Custom" else "",
            height=120,
        )
    else:
        new_system_prompt = PERSONA_OPTIONS[selected_persona]
        st.text_area("System Message", value=new_system_prompt, height=100, disabled=True)

    if selected_persona != st.session_state.persona or new_system_prompt != st.session_state.system_prompt:
        st.session_state.persona = selected_persona
        st.session_state.system_prompt = new_system_prompt
        st.session_state.messages = [SystemMessage(content=new_system_prompt)]
        st.rerun()

    temperature = st.slider(
        "Temperature",
        0.0, 1.0, 0.9, 0.05,
        help="Controls randomness/creativity. Lower = more focused & predictable, Higher = more random & creative.",
    )
    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [SystemMessage(content=st.session_state.system_prompt)]
        st.rerun()
    st.divider()
    st.markdown("Made with ❤️ by **Rohan**")

if "model" not in st.session_state or st.session_state.get("temperature") != temperature:
    st.session_state.model = ChatMistralAI(model="mistral-small-2506", temperature=temperature)
    st.session_state.temperature = temperature

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="🧑"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg.content)

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            response = st.session_state.model.invoke(st.session_state.messages)
            st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))