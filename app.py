import streamlit as st

def main():
    st.title("Personal Website")
    
    # Add some styling
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #333;
            margin-bottom: 30px;
        }
        .section-header {
            font-size: 24px;
            font-weight: bold;
            color: #555;
            margin-bottom: 20px;
        }
        .project-item {
            margin-bottom: 15px;
        }
        .logo {
            width: 32px;
            height: 32px;
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # About Me section
    st.header("About Me")
    st.write("""
    I'm a student deeply passionate about Natural Language Processing (NLP) and Artificial Intelligence (AI). Currently pursuing Bachelor of Engineering (B.E.) in Information Technology at Gujarat Technological University (GTU) with a current CGPA of 8.9/10. My goal is to become a proficient Machine Learning Engineer.
    
    Outside of academics, you can find me lost in the pages of a good book or working on AI projects. I believe in continuous learning and collaboration, and I'm excited about the opportunities ahead in my journey.
    """)
    
    st.write("---")  # Add a horizontal line for separation

    # Education section
    st.header("Education")
    st.write("""
    - Bachelor of Engineering (B.E.) in Information Technology  
      Gujarat Technological University (GTU)  
      Current CGPA: 8.9/10
    
    - Higher Secondary (12th Grade)  
      Adani Vidya Mandir  
      Score: 88%
    
    - Secondary School (10th Grade)  
      Adani Vidya Mandir  
      Score: 83%
    
    **Certifications**
    
    - Full Stack Web Development - Udemy
    - Prompt Engineering - Coursera
    - Machine Learning - Coursera
    """)

    st.write("---")  # Add a horizontal line for separation

    # Projects section
    st.header("Projects")
    st.write("""
    1. **Chatbot**
       - Developed a chatbot using Streamlit and Groq to provide conversational interactions for users. Implemented natural language processing techniques to understand user queries and provide relevant responses.
    
    2. **Weather API**
       - Created a website that displays weather information for searched cities. Integrated with a weather API to fetch real-time weather data and presented it in a user-friendly interface.
    
    3. **Family Travel Tracker**
       - Utilized JavaScript and SQL to develop a Family Travel Tracker application. Designed to help families plan and track their travel experiences, including itinerary management and expense tracking.
    """)
    
    st.write("---")  # Add a horizontal line for separation

    # Skills section
    st.header("Skills")
    st.write("""
    **Technical Skills:**
    - Machine Learning
    - SQL
    - JavaScript
    - UI/UX
    
    **Soft Skills:**
    - Communication
    - Teamwork
    - Problem-solving
    - Adaptability
    - Time management
    - Leadership
    - Emotional intelligence
    """)

    st.write("---")  # Add a horizontal line for separation

    # Contact section
    st.header("Contact Me")
    st.write("""
    If you'd like to get in touch with me, feel free to reach out via email at [prince13142004@gmail.com](mailto:prince13142004@gmail.com).
    
    You can also check out my projects and contributions on [GitHub](https://github.com/Prince1314-patel) and connect with me on [LinkedIn](https://www.linkedin.com/in/prince-patel-527a25289/).
    """)


if __name__ == "__main__":
    main()
