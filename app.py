import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI Career Counselor", page_icon="🎯")

# Sidebar for Gemini API Key
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key at [Google AI Studio](https://aistudio.google.com/)")

st.title("🎓 AI Career Counselor")
st.write("Get a professional roadmap to your dream career.")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    current_status = st.text_input("Current Role/Background", placeholder="e.g. Student")
    target_role = st.text_input("Target Career Goal", placeholder="e.g. Data Scientist")

with col2:
    experience = st.selectbox("Experience Level", ["Entry-Level", "Mid-Level", "Senior"])
    skills = st.text_area("Your Skills", placeholder="e.g. Python, Excel")

if st.button("Generate Roadmap"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar.")
    else:
        try:
            # Setup the SDK
            genai.configure(api_key=api_key)
            
            # Using the stable model name
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner("Generating your plan..."):
                prompt = f"""
                Act as a Career Counselor. Provide a detailed career roadmap for:
                Current Role: {current_status}
                Target Role: {target_role}
                Level: {experience}
                Skills: {skills}
                
                Include: 
                1. Skill gaps
                2. Learning path
                3. A 3-month action plan.
                """
                
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.markdown(response.text)
                
        except Exception as e:
            # This will help us see the exact error if it fails again
            st.error(f"An error occurred: {e}")
