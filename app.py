import streamlit as st
from streamlit_chat import message
import random
from src.chatbot import gita_chatbot

# Configure the sacred interface in homage to the Bhagavad Gita
st.set_page_config(
    page_title='🕉️ Bhagavad Gita Bot: Divine Wisdom',
    layout='centered',
    page_icon='📖'
)

# Display the sacred title in reverence to the Bhagavad Gita
st.title("🕉️ Bhagavad Gita Bot: Eternal Teachings of the Gita")

# Assign a unique session ID for each soul seeking the Gita’s wisdom
session_id = random.randint(0, 100000)
if "session_id" not in st.session_state:
    st.session_state.session_id = session_id

# Initial divine message inspired by the Bhagavad Gita
INIT_MESSAGE = {
    "role": "assistant",
    "content": "Om Namo Bhagavate Vasudevaya! I am the Bhagavad Gita Bot, a humble messenger of the divine dialogue between Lord Krishna and Arjuna. Seek the eternal wisdom of the Bhagavad Gita, and I shall guide you with its sacred teachings."
}

# Initialize the sacred dialogue with the Gita’s blessings
if "messages" not in st.session_state:
    st.session_state.messages = [INIT_MESSAGE]

def invoke_gita_wisdom(input_text):
    """Invoke the divine counsel of the Bhagavad Gita through the Bot."""
    divine_guidance = gita_chatbot(user_query=input_text)
    return divine_guidance

# Render the sacred dialogue inspired by the Gita’s verses
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Receive the seeker’s query
user_input = st.chat_input(
    placeholder="Seek the wisdom of the Bhagavad Gita...",
    key="divine_input"
)

# Display the seeker’s offering of words
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

# Bestow the Bhagavad Gita’s divine response
if st.session_state.messages[-1]["role"] != "assistant":
    divine_response = invoke_gita_wisdom(user_input)
    st.session_state.messages.append({"role": "assistant", "content": divine_response})
    with st.chat_message("assistant"):
        st.markdown(divine_response)