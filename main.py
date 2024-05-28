import os
from openai import AzureOpenAI
import streamlit as st
from st_pages import add_page_title, show_pages_from_config

client = AzureOpenAI(
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
)

add_page_title()
show_pages_from_config()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_message := st.chat_input(
    "Hi, how can I help you?",
):
    with st.chat_message("user"):
        st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

    completion = client.chat.completions.create(
        model=os.environ.get("AZURE_OPENAI_DEPLOYMENT_MODEL"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )

    with st.chat_message("assistant"):
        st.markdown(completion.choices[0].message.content)
        st.session_state.messages.append(
            {"role": "assistant", "content": completion.choices[0].message.content}
        )
