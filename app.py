import streamlit as st
import io
import requests

st.title("Customer Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")
if st.button("Send") and user_input:
    st.session_state.messages.append(("You", user_input))
    # Replace with your Rasa server URL if different
    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": user_input}
    )
    # Rasa can return multiple messages (text, image, buttons, etc.)
    for msg in response.json():
        st.session_state.messages.append(("Bot", msg))

# Display chat history with rich content
for idx, (sender, msg) in enumerate(st.session_state.messages):
    if sender == "Bot" and isinstance(msg, dict):
        # Show text (with markdown)
        if "text" in msg:
            st.markdown(f"**Bot:** {msg['text']}")
        # Show image
        if "image" in msg:
            st.image(msg["image"], caption="Bot sent an image")
        # Show buttons
        if "buttons" in msg:
            for bidx, button in enumerate(msg["buttons"]):
                # Use both message index and button index for uniqueness
                if st.button(button["title"], key=f"{button['title']}_{idx}_{bidx}"):
                    st.session_state.messages.append(("You", button["title"]))
                    response = requests.post(
                        "http://localhost:5005/webhooks/rest/webhook",
                        json={"sender": "user", "message": button["payload"]}
                    )
                    for reply in response.json():
                        st.session_state.messages.append(("Bot", reply))
    else:
        st.markdown(f"**{sender}:** {msg}")

# Prepare chat history as text
chat_text = ""
for sender, message in st.session_state.messages:
    if isinstance(message, dict):
        chat_text += f"{sender}: {message.get('text', '')}\n"
    else:
        chat_text += f"{sender}: {message}\n"

# Download button
st.download_button(
    label="Download Chat History",
    data=chat_text,
    file_name="chat_history.txt",
    mime="text/plain"
)