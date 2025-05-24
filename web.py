import streamlit as st

# Title and subtitle
st.title("🌟 Welcome to My First Streamlit Website!")
st.subheader("This is a  website built with Streamlit.")

# Display an image (optional)
st.image("https://via.placeholder.com/600x300.png?text=Welcome+to+Streamlit", caption="My Simple Web App")

# Paragraph
st.write("""
Hello! My name is Shumaila Usmani. This is a basic website created using Python and Streamlit.
Streamlit makes it super easy to build web apps with just a few lines of code!
""")

# Form: Ask for user name
st.write("### 👤 Enter Your Name")
name = st.text_input("What's your name?")

if st.button("Say Hello"):
    st.success(f"Hello, {name}! 👋 Welcome to my website.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
