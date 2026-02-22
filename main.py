
# Physics AI Tutor - Main Program
# This is the core program that runs the AI tutor

import os
from dotenv import load_dotenv
from groq import Groq
from misconceptions import MISCONCEPTIONS
from prompts import SYSTEM_PROMPT, get_misconception_prompt
from test_questions import get_all_questions
import time

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(user_question, detected_misconception=None):
    """
    Gets a real AI response from Groq
    """
    
    # Build the prompt
    if detected_misconception:
        misc_prompt = get_misconception_prompt(detected_misconception)
        system_message = f"{SYSTEM_PROMPT}\n\n{misc_prompt}"
    else:
        system_message = SYSTEM_PROMPT
    
    try:
        # Call Groq API
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
        return f"Sorry, I'm having trouble connecting to my AI brain right now. Error: {str(e)}"


def detect_misconception(user_question):
    """
    Checks if the user's question contains keywords related to common misconceptions
    Returns the misconception key if found, None otherwise
    """
    
    user_question = user_question.lower()
    
    # Check for "heavy falls faster" misconception
    if any(word in user_question for word in ["heavier", "heavy", "weight", "fall faster"]):
        if "fall" in user_question or "drop" in user_question:
            return "heavy_falls_faster"
    
    # Check for "force equals velocity" misconception
    if "force" in user_question and ("velocity" in user_question or "speed" in user_question):
        return "force_equals_velocity"
    
    # Check for "action-reaction cancel" misconception
    if "action" in user_question and "reaction" in user_question:
        return "action_reaction_cancel"
    
    # Check for "acceleration and velocity same" misconception
    if "acceleration" in user_question and "velocity" in user_question:
        return "acceleration_velocity_same"
    
    # Check for "rest means no forces" misconception
    if "rest" in user_question or "not moving" in user_question:
        if "force" in user_question:
            return "rest_means_no_forces"
    
    return None


def main():
    """
    Main function - runs the tutor program
    """
    
    print("=" * 50)
    print("PHYSICS AI TUTOR - AP Physics 1")
    print("Misconception Detection System")
    print("=" * 50)
    print()
    
    print("Hello! I'm your physics tutor.")
    print("Ask me any physics question, and I'll help you understand!")
    print()
    print("Type 'quit' to exit")
    print("-" * 50)
    print()
    
    while True:
        # Get user input
        user_question = input("You: ")
        
        if user_question.lower() == 'quit':
            print("\nThanks for learning with me! Goodbye!")
            break
        
        # Detect if there's a misconception
        misconception = detect_misconception(user_question)
        
        if misconception:
            print(f"\n[Detected misconception: {misconception}]")
        
        # Get AI response
        print("\nTutor: ", end="")
        response = get_ai_response(user_question, misconception)
        
        # Print response with a typing effect (just for fun!)
        for char in response:
            print(char, end="", flush=True)
            time.sleep(0.01)
        
        print("\n")


if __name__ == "__main__":
    main()