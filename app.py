import streamlit as st
from revChatGPT.V1 import Chatbot

def main():
    # Set page title and description
    st.set_page_config(page_title="AI Assistant: revChatGPT", page_icon=":speak_no_evil:")
    st.subheader("AI Assistant: revChatGPT")
    st.markdown("This app allows you to chat with ChatGPT using a reverse-engineered API library called [revChatGPT](https://github.com/acheong08/ChatGPT). Replies from ChatGPT are streamed back to the user in real-time, which gives the user an experience similar to how ChatGPT streams back its answers.")

    # Add image to the sidebar
    st.sidebar.image("https://i.ibb.co/z84mCfY/image-8.png", use_column_width=True)
    # Create Streamlit sidebar
    st.sidebar.subheader("Configuration")
    st.sidebar.write("Create an account on [OpenAI's ChatGPT](https://chat.openai.com/) and save your credentials.")
    auth_method = st.sidebar.selectbox("Authentication method:", ["Email/Password", "Session token", "Access token"])

    # Show text input widgets based on selected authentication method
    if auth_method == "Email/Password":
        email = st.sidebar.text_input("Email:")
        password = st.sidebar.text_input("Password:", type="password")
        st.sidebar.markdown("## Authentication Methods")
        st.sidebar.markdown("")
        st.sidebar.markdown("#### Email/Password")
        st.sidebar.write("Not supported for Google/Microsoft accounts")
        st.sidebar.markdown("----")
        st.sidebar.markdown("#### Session token")
        st.sidebar.write("Comes from cookies on chat.openai.com as *\"__Secure-next-auth.session-token\"*")
        st.sidebar.markdown("----")
        st.sidebar.markdown("#### Access token")
        st.sidebar.write("[https://chat.openai.com/api/auth/session](https://chat.openai.com/api/auth/session)")
        if email != "" and password != "":
            config = {"email": email, "password": password}
            
        else:
            st.write("**Please enter your email and password.**")
            return
    elif auth_method == "Session token":
        session_token = st.sidebar.text_input("Session token:")
        st.sidebar.markdown("## Authentication Methods")
        st.sidebar.markdown("")
        st.sidebar.markdown("#### Email/Password")
        st.sidebar.write("Not supported for Google/Microsoft accounts")
        st.sidebar.markdown("----")
        st.sidebar.markdown("#### Session token")
        st.sidebar.write("Comes from cookies on chat.openai.com as *\"__Secure-next-auth.session-token\"*")
        st.sidebar.markdown("----")
        st.sidebar.markdown("#### Access token")
        st.sidebar.write("[https://chat.openai.com/api/auth/session](https://chat.openai.com/api/auth/session)")        
        if session_token != "":
            config = {"session_token": session_token}
        else:
            st.write("**Please enter your session token.**")
            return
    else:
        access_token = st.sidebar.text_input("Access token:")
        st.sidebar.markdown("## Authentication Methods")
        st.sidebar.markdown("")
        st.sidebar.markdown("#### Email/Password")
        st.sidebar.write("Not supported for Google/Microsoft accounts")
        st.sidebar.markdown("----")
        st.sidebar.markdown("#### Session token")
        st.sidebar.write("Comes from cookies on chat.openai.com as *\"__Secure-next-auth.session-token\"*")
        st.sidebar.markdown("----")
        st.sidebar.markdown("#### Access token")
        st.sidebar.write("[https://chat.openai.com/api/auth/session](https://chat.openai.com/api/auth/session)")        
        if access_token != "":
            config = {"access_token": access_token}
        else:
            st.write("**Please enter your access token.**")
            return

    # Instantiate chatbot
    chatbot = Chatbot(config=config)

    # Get user input using text input widget
    user_input = st.text_input("You: ", placeholder="Ask me anything ...", key="input")

    if st.button("Submit", type="primary"):
        st.markdown("----")
        res_box = st.empty()

        for data in chatbot.ask(user_input):
            message = data["message"]
            res_box.write("ChatGPT: " + message)

        st.markdown("")
        st.markdown("---")
        st.markdown("")
        st.markdown("<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
