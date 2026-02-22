
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from misconceptions import MISCONCEPTIONS
from prompts import SYSTEM_PROMPT, get_misconception_prompt

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(
    page_title="Physics AI Tutor",
    page_icon="🔬",
    layout="wide"
)

# Title and description
st.title("🔬 Physics AI Tutor")
st.subheader("AP Physics 1 - Misconception Detection System")
st.markdown("Ask me any physics question and I'll help you understand!")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "misconception" in message:
            st.info(f"💡 Detected misconception: {message['misconception']}")

# Detect misconception function
def detect_misconception(user_question):
    user_question = user_question.lower()
    
    if any(word in user_question for word in ["heavier", "heavy", "weight", "fall faster"]):
        if "fall" in user_question or "drop" in user_question:
            return "heavy_falls_faster"
    
    if "force" in user_question and ("velocity" in user_question or "speed" in user_question):
        return "force_equals_velocity"
    
    if "action" in user_question and "reaction" in user_question:
        return "action_reaction_cancel"
    
    if "acceleration" in user_question and "velocity" in user_question:
        return "acceleration_velocity_same"
    
    if "rest" in user_question or "not moving" in user_question:
        if "force" in user_question:
            return "rest_means_no_forces"
    
    return None

# Get AI response function
def get_ai_response(user_question, detected_misconception=None):
    if detected_misconception:
        misc_prompt = get_misconception_prompt(detected_misconception)
        system_message = f"{SYSTEM_PROMPT}\n\n{misc_prompt}"
    else:
        system_message = SYSTEM_PROMPT
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_question}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I'm having trouble right now. Error: {str(e)}"

# Chat input
if prompt := st.chat_input("Ask a physics question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Detect misconception
    misconception = detect_misconception(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(prompt, misconception)
            st.markdown(response)
            
            if misconception:
                st.info(f"💡 Detected misconception: {misconception}")
    
    # Add assistant message to chat history
    assistant_message = {"role": "assistant", "content": response}
    if misconception:
        assistant_message["misconception"] = misconception
    st.session_state.messages.append(assistant_message)

# Sidebar with info
with st.sidebar:
    st.header("📚 About")
    st.markdown("""
    This AI tutor helps you understand physics by:
    - Detecting common misconceptions
    - Asking diagnostic questions
    - Providing targeted explanations
    - Using examples and analogies
    """)
    
    st.header("🎯 Target Misconceptions")
    st.markdown("""
    1. Heavier objects fall faster
    2. Force equals velocity
    3. Action-reaction forces cancel
    4. Acceleration and velocity are the same
    5. Objects at rest have no forces
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()