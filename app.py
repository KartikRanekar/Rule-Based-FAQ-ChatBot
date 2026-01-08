import streamlit as st
from faq_data import get_answer

# Page config
st.set_page_config(page_title="Institute FAQ Chatbot", page_icon="🏫")

# Title
st.title("🏫 Institute FAQ Chatbot")
st.markdown("Ask me anything about the institute! (e.g., Timings, Fees, Courses)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add an initial greeting
    st.session_state.messages.append({"role": "assistant", "content": "Hello! I can help you with questions about the institute. What would you like to know?"})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Type your question here..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response
    response = get_answer(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.header("Help")
    # Clear Chat Button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": "Chat history cleared. How can I help you regarding the institute?"})
        st.rerun()

    st.write("Try asking about:")
    topics = [
        "Timings & Holidays",
        "Fees & Admissions",
        "Courses & Placements",
        "Hostel & Transport",
        "Library & Sports",
        "Contact & Address"
    ]
    for topic in topics:
        st.markdown(f"- {topic}")
