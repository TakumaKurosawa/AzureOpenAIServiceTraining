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
    "どんな画像が生成したいですか？",
):
    with st.chat_message("user"):
        st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

    result = client.images.generate(
        model=os.environ.get("AZURE_OPENAI_DEPLOYMENT_MODEL_IMAGE_GENERATOR"),
        prompt=user_message,
        n=1,
        size="512x512",
    )

    st.image(result.data[0].url)
    st.session_state.messages.append(
        {"role": "assistant", "content": result.data[0].url}
    )
