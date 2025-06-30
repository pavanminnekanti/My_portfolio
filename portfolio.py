import streamlit as st

# --- Page config (must be first) ---
st.set_page_config(page_title="Pavan Kumar  | Portfolio", layout="wide")


# resume_path = r"C:\Users\91944\Downloads\resume\Guru2025.pdf"
# resume_text = extract_text_from_pdf(resume_path)

# --- Simulated Structured Resume Data ---
personal_info = {
    "name": "Pavan Kumar Minnekanti",
    "title": "AI/ML Enthusiast & Data Science | Python Developer",  # "AI/ML & Data Science | Python Developer"
    "summary": (
        "Summary:-\n\n"
        "👉 Data Collection & Processing Assist in collecting,cleaning and structuring datasets for ML Training and Analysis\n\n"
        "👉 Designing,Training, and evaluting machine learning models\n\n"
        "👉 Maintain clear and concise documentation of ML experiments,model performance and project progress.\n\n"
        "👉 Skilled in NLP, Neural Networks, and solving real-world problems with data.\n\n"
        "👉 Automating tasks and integrating AI into DevOps pipelines and improve efficiency, reliability, and scalability"
    ),
    "email": "minnekanti129@gmail.com",
    "linkedin": "https://www.linkedin.com/in/pavan-kumar-minnekanti-899b93366/",
    "github": "https://github.com/pavanminnekanti",
}

education = [
    {
        "degree": "Civil Engineering",
        "institution": "College: Chalapathi Institute of Engineering and Technology",
        "year": "2017 - 2021",
        "details": "Gained foundational knowledge in the design, construction, and maintenance of infrastructure such as buildings, roads, and bridges..",
    },
    {
        "degree": "Certification in Auto CAD",
        "institution": "Certification: CANTER CADD",
        "year": "2020",
        "details": "Completed a certified course in AutoCAD, gaining proficiency in 2D drafting and 3D modeling."
        "Trained in AutoCAD for creating detailed engineering drawings and construction plans.",
    },
]


skills = {
    "Python": 90,
    "Machine Learning": 85,
    "Deep Learning": 70,
    "HTML/CSS": 70,
    "SQL": 65,
    "Streamlit": 80,
    "Pandas/Numpy": 85,
}


experience = [
    {
        "year": "Feb 2025 - Present",
        "role": "Software Engineer",
        "company": "Lyros Technologies",
        "description":  "I’m an enthusiastic and detail-oriented *AI/ML Intern at Lyros*, passionate about transforming data into actionable insights.\n\n"
        "- 🤖 Hands-on experience in *Machine Learning, **Deep Learning, and **Large Language Models (LLMs)*\n"
        "- 🐍 Proficient in *Python, **SQL*, and modern AI/ML tools\n"
        "- 📊 Passionate about exploring datasets and uncovering hidden patterns\n"
        "- 🧠 Experienced in *Natural Language Processing (NLP)* and *Neural Networks*\n"
        "- ⚙️ Skilled at automating tasks and integrating AI into *DevOps pipelines* for efficiency and scalability\n"
        "- 🚀 Driven by curiosity and a commitment to continuous learning\n"
        "- 📝 Strong at documenting progress and sharing actionable insights",
    },
]

projects = [
    {
        "name": "🎓 Income Tax Calculation",
        "desc": (
            "- Developed a user-friendly web application with Streamlit to automate and simplify income tax calculations based on user input.\n"
            "- Implemented dynamic forms and interactive UI components for real-time tax computation and result display. \n"
            "- Integrated Python logic to handle various income types, tax slabs, and deductions, ensuring accurate calculations for different scenarios"
        ),
    },
    {
        "name": "🎓 Student Grading System",
        "desc": (
            "- Developed a Tkinter-based GUI to manage student marks\n"
            "- Implemented role-based access for admins and teachers\n"
            "- Used Pandas for data handling and predictive grade analysis"
        ),
    },
    {
        "name": "🏠 Airbnb Price Prediction",
        "desc": (
            "- Built regression models to predict listing prices\n"
            "- Analyzed key features affecting price fluctuations\n"
            "- Enabled data-driven pricing recommendations"
        ),
    },
    {
        "name": "Iris Project using regression model",
        "desc": (
            "- Built a regression model to predict Iris flower characteristics using Python and relevant machine learning libraries\n"
            "- Designed and implemented an interactive web interface with Streamlit for seamless user input and real-time prediction results.\n"
            "- Preprocessed and analyzed the Iris dataset, applying feature engineering and model evaluation techniques to optimize performance."
        ),
    }
]

# ------------side bar navigation 1, check up for the new one----
st.sidebar.title("📌 Navigation")

if "page" not in st.session_state:
    st.session_state.page = "About Me"

if st.sidebar.button("About Me"):
    st.session_state.page = "About Me"
if st.sidebar.button("Education"):
    st.session_state.page = "Education"
if st.sidebar.button("Skills   "):
    st.session_state.page = "Skills"
if st.sidebar.button("Experience"):
    st.session_state.page = "Experience"
if st.sidebar.button("Projects"):
    st.session_state.page = "Projects"
if st.sidebar.button("Contact"):
    st.session_state.page = "Contact"

page = st.session_state.page
# ------ side bar------------


# --- About Me ---
if page == "About Me":
    st.title(f"👋 Hi, I'm {personal_info['name']}")
    st.markdown(f"### {personal_info['title']}")
    # st.markdown(f"###### {personal_info['summary']}")
    st.info(personal_info["summary"])

    st.markdown(
        f"""
    *📧 Email:* [{personal_info['email']}](mailto:{personal_info['email']})  
    *🔗 LinkedIn:* [{personal_info['linkedin']}]({personal_info['linkedin']})  
    *💻 GitHub:* [{personal_info['github']}]({personal_info['github']})
    """
    )

# --- Education ---
elif page == "Education":
    st.header("🎓 Education")
    for edu in education:
        st.subheader(f"{edu['institution']}")
        st.markdown(f"{edu['degree']}")
        st.markdown(f"*📅 {edu['year']}*")

        st.info(edu["details"])
        st.markdown("---")

# --- Skills ---
elif page == "Skills":
    st.header("🧠 Skills Overview")
    for skill, value in skills.items():
        st.markdown(f"*{skill}*")
        st.progress(value)

# --- Experience ---
elif page == "Experience":
    st.header("💼 Experience Timeline")

    for exp in experience:
        with st.container():
            st.subheader(f"{exp['role']} • {exp['company']}")
            st.markdown(f"*📅 {exp['year']}*")
            st.markdown(exp["description"])
            st.markdown("---")


# --- Projects ---
elif page == "Projects":
    st.header("🛠 Projects Showcase")
    for proj in projects:
        st.markdown(f"#### {proj['name']}")
        st.success(proj["desc"])



# --- Contact ---
elif page == "Contact":
    st.header("📬 Contact Me")
    contact_form = """
    <form action="https://formsubmit.co/minnekanti129@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px;"><br><br>
         <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px;"><br><br>
         <textarea name="message" placeholder="Your message" required style="width: 100%; padding: 10px;"></textarea><br><br>
         <button type="submit" style="padding: 10px 20px; background-color: teal; color: white;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown(
        "\n\n 💡Tip: Replace your email with the one you want to receive messages on."
    )

# --- Footer ---
st.markdown("---")
# st.write("Crafted with precision and passion for 💖Python and Data Science. © 2025 Gurunath Tokala")
# st.write("Data speaks, Python listens, and 💖 I build. © 2025 Gurunath Tokala")
st.markdown(
    """
<div style="text-align:center; font-size:16px;">
   
</div>
""",
    unsafe_allow_html=True,
)
