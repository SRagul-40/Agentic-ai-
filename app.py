import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI Career Counselor", page_icon="🎯")

with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Ensure your key is from [Google AI Studio](https://aistudio.google.com/)")

st.title("🎓 AI Career Counselor")

# Inputs
current_status = st.text_input("Current Background")
target_role = st.text_input("Target Career")

if st.button("Generate Roadmap"):
    if not api_key:
        st.error("Please enter your API Key.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # --- MODEL DISCOVERY LOGIC ---
            # This part finds which model YOUR key is allowed to use
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            
            # Pick the best one available
            if '/models/gemini-1.5-flash-latest' in available_models:
                model_to_use = 'gemini-1.5-flash-latest'
            elif '/models/gemini-1.5-flash' in available_models:
                model_to_use = 'gemini-1.5-flash'
            elif '/models/gemini-pro' in available_models:
                model_to_use = 'gemini-pro'
            else:
                # If nothing else, pick the first one in the list
                model_to_use = available_models[0].split('/')[-1]
            
            st.info(f"Using model: {model_to_use}")
            
            # --- GENERATION ---
            model = genai.GenerativeModel(model_to_use)
            prompt = f"Act as a career counselor. Give a roadmap for {current_status} to become {target_role}."
            
            response = model.generate_content(prompt)
            st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Error: {e}")
            st.write("Current available models for your key:")
            # List all models so you can see what is available
            try:
                models = [m.name for m in genai.list_models()]
                st.write(models)
            except:
                st.write("Could not list models. Is your API Key correct?")
