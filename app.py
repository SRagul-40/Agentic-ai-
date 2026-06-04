import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Career Counselor", page_icon="🎓", layout="wide")

# --- DATABASE (The "Brain" of our Counselor) ---
# This replaces the API by storing expert knowledge locally
CAREER_DATABASE = {
    "Technology": {
        "roles": ["Software Engineer", "Data Analyst", "Cybersecurity Specialist"],
        "skills": ["Programming (Python/Java)", "Problem Solving", "Cloud Computing"],
        "courses": ["Computer Science Degree", "AWS Certification", "Coding Bootcamps"],
        "roadmap": ["Step 1: Learn a language (Python)", "Step 2: Build a Portfolio", "Step 3: Internships"]
    },
    "Healthcare": {
        "roles": ["Nurse", "Healthcare Administrator", "Medical Lab Technician"],
        "skills": ["Empathy", "Attention to Detail", "Medical Knowledge"],
        "courses": ["Nursing Degree (BSN)", "Health Admin Certification"],
        "roadmap": ["Step 1: Get Science Prerequisites", "Step 2: Clinical Training", "Step 3: State Licensing"]
    },
    "Business & Finance": {
        "roles": ["Financial Analyst", "Marketing Manager", "Project Manager"],
        "skills": ["Strategic Thinking", "Data Analysis", "Leadership"],
        "courses": ["MBA or BBA", "PMP Certification", "CFA Level 1"],
        "roadmap": ["Step 1: Learn Excel/SQL", "Step 2: Junior Analyst Role", "Step 3: Management Training"]
    },
    "Creative Arts": {
        "roles": ["Graphic Designer", "UX/UI Designer", "Content Creator"],
        "skills": ["Design Software (Adobe/Figma)", "Creativity", "Visual Branding"],
        "courses": ["Design Foundations Course", "Google UX Design Cert"],
        "roadmap": ["Step 1: Master Design Tools", "Step 2: Build Freelance Portfolio", "Step 3: Agency Experience"]
    }
}

# --- SIDEBAR (Information Section) ---
with st.sidebar:
    st.title("📖 About AI Counselor")
    st.info("An AI career counselor is a system that uses logic to help people make education and career decisions.")
    st.markdown("### 🎯 Purpose")
    st.write("Increase access to advice and save time by analyzing information quickly.")
    st.markdown("### ✅ Advantages")
    st.write("- 24/7 Availability\n- No API Keys needed\n- Instant responses")
    st.markdown("### ⚠️ Limitations")
    st.write("- No emotional context\n- Based on pre-set logic")

# --- MAIN UI ---
st.title("🎓 Smart AI Career Counselor")
st.write("Professional guidance for education and career decisions — *Offline Version*")

# Tabs for Organization
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Assessment", "🔍 Career Exploration", "📝 Prep Support", "📋 Planning"])

with tab1:
    st.header("Career Assessment")
    name = st.text_input("Full Name")
    interest = st.selectbox("What is your primary area of interest?", list(CAREER_DATABASE.keys()))
    strength = st.multiselect("Select your top strengths:", ["Math/Logic", "Communication", "Creativity", "Leadership", "Hands-on work"])
    
    if st.button("Analyze My Profile"):
        data = CAREER_DATABASE[interest]
        st.success(f"Hello {name}! Based on your interest in {interest}, here is your assessment:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Suggested Roles")
            for role in data["roles"]:
                st.write(f"- {role}")
        with col2:
            st.subheader("Required Skills")
            for skill in data["skills"]:
                st.write(f"- {skill}")

with tab2:
    st.header("Career Exploration")
    st.write("Compare roles and understand the industry.")
    selected_area = st.selectbox("Explore a Field:", list(CAREER_DATABASE.keys()), key="explore")
    
    info = CAREER_DATABASE[selected_area]
    st.info(f"**Industries in {selected_area}:** Typical salaries range from $50k to $120k depending on experience.")
    st.write(f"**Education Recommendations:** {', '.join(info['courses'])}")

with tab3:
    st.header("Resume & Interview Prep")
    prep_mode = st.radio("Choose Service:", ["Resume Optimization", "Mock Interview Tips"])
    
    if prep_mode == "Resume Optimization":
        st.write("### AI Resume Tips")
        st.write("1. Use action verbs like 'Managed', 'Developed', or 'Led'.")
        st.write("2. Quantify achievements (e.g., 'Increased sales by 20%').")
        st.write("3. Include keywords specific to your industry.")
    else:
        st.write("### Interview Preparation")
        st.write("**Q:** Tell me about yourself.")
        st.caption("**AI Tip:** Use the Present-Past-Future model. Current role, past success, and why you want this job.")
        st.write("**Q:** What is your greatest strength?")
        st.caption("**AI Tip:** Share a strength that solves a problem for this specific company.")

with tab4:
    st.header("Step-by-Step Roadmap")
    target = st.selectbox("Select Target Path:", list(CAREER_DATABASE.keys()), key="roadmap")
    
    steps = CAREER_DATABASE[target]["roadmap"]
    
    for i, step in enumerate(steps):
        st.checkbox(step, key=f"step_{i}")
    
    st.progress((1/3) * len(steps)) # Simple progress bar visualization

# --- FOOTER ---
st.divider()
st.caption("This tool provides automated guidance based on professional counseling frameworks.")
