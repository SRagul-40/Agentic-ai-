import streamlit as st
from google import genai
from google.genai import types

# Page Configuration
st.set_page_config(page_title="AI Career Counselor", page_icon="🎯", layout="centered")

# Sidebar for Gemini API Key
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your API key at [Google AI Studio](https://aistudio.google.com/)")
    st.markdown("---")
    st.markdown("### How it works")
    st.caption("1. Enter your API Key")
    st.caption("2. Fill in your profile")
    st.caption("3. Get a data-driven career path")

st.title("🎓 AI Career Counselor")
st.write("Unlock your potential with personalized, AI-driven career guidance.")

# User Input Form
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        current_status = st.text_input("Current Role / Background", placeholder="e.g. Mechanical Engineer")
        target_role = st.text_input("Target Dream Career", placeholder="e.g. AI Product Manager")
    
    with col2:
        experience = st.selectbox("Years of Experience", ["Student/Fresh Grad", "1-3 Years", "3-7 Years", "7+ Years"])
        location = st.text_input("Preferred Location", placeholder="e.g. Remote / London")

    skills = st.text_area("List your top skills (Comma separated)", placeholder="e.g. Python, Project Management, SQL")

# Action Button
if st.button("Generate My Career Roadmap", type="primary"):
    if not api_key:
        st.error("Please provide a Gemini API Key in the sidebar to proceed.")
    elif not target_role:
        st.warning("Please enter a Target Career Goal.")
    else:
        try:
            # Initialize Gemini Client
            client = genai.Client(api_key=api_key)
            
            with st.spinner("Analyzing market trends and crafting your path..."):
                prompt = f"""
                Act as an expert Career Counselor. Create a professional career roadmap for a user with the following profile:
                - Current Role: {current_status}
                - Target Career: {target_role}
                - Experience: {experience}
                - Current Skills: {skills}
                - Location Preference: {location}

                Provide the roadmap in these specific sections:
                1. **Skills Gap Analysis**: Contrast what they have vs. what the target role requires.
                2. **Learning Roadmap**: Suggest specific certifications, tools, or courses.
                3. **Resume & LinkedIn Optimization**: Give 3 specific bullet points to add.
                4. **Interview Prep**: Top 3 technical or behavioral questions for this specific transition.
                5. **3-Phase Action Plan**: Steps for the next 30, 60, and 90 days.
                """

                # Call Gemini Model (using 1.5-flash for speed and cost-efficiency)
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=prompt
                )

                # Display Result
                st.markdown("---")
                st.success(f"### 🚀 Roadmap to {target_role}")
                st.markdown(response.text)
                
                # Option to download
                st.download_button("Download Roadmap as Text", response.text, file_name="career_roadmap.txt")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.caption("Privacy Note: Your data is processed via the API and not stored on this server.")
