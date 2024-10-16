import streamlit as st

def show_about():
    st.title("About")
    st.write("This is a blog site created using Streamlit.")
    
    st.subheader("About Me")
    st.write("""
    Hi, I'm Udaysinh, a Developer and Student.
    - **Age and Gender**: 20, Male
    - **Occupation**: Developer and Student
    - **Education**: Currently pursuing Computer Science at DYPIU, Akurdi Pune.
    - **Projects**: Visit my Discord Bot Myra Bot :)
    - **More About Me**: Hi! I am an undergraduate student developer. I enjoy working on various projects and learning new technologies.
    """)
    
    st.subheader("Contact Me")
    st.write("""
    - **Discord**: @udaysinh
    - **Email**: contact@udaysinh.me
    """)
    
    st.markdown(
        """
        <iframe src="https://udaysinh.me" width="100%" height="600px" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

show_about()