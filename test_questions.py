
# Pre/Post Test Questions for Physics Misconceptions
# These questions test student understanding before and after using the tutor

TEST_QUESTIONS = [
    {
        "id": 1,
        "misconception": "heavy_falls_faster",
        "question": "A bowling ball and a marble are dropped from the same height at the same time in a vacuum. Which hits the ground first?",
        "options": ["A) Bowling ball", "B) Marble", "C) Both at the same time", "D) Depends on their weight"],
        "correct_answer": "C",
        "explanation": "In a vacuum (no air resistance), all objects fall at the same rate regardless of mass."
    },
    
    {
        "id": 2,
        "misconception": "force_equals_velocity",
        "question": "A hockey puck slides across frictionless ice at constant velocity. What is the net force on the puck?",
        "options": ["A) In the direction of motion", "B) Opposite to motion", "C) Zero", "D) Equal to its velocity"],
        "correct_answer": "C",
        "explanation": "Constant velocity means zero acceleration, so net force = 0 (Newton's first law)."
    },
    
    {
        "id": 3,
        "misconception": "action_reaction_cancel",
        "question": "You push on a wall with 50N of force. The wall pushes back on you with 50N. Why don't these forces cancel out?",
        "options": ["A) They do cancel", "B) They act on different objects", "C) One is bigger", "D) They're in the same direction"],
        "correct_answer": "B",
        "explanation": "Action-reaction pairs act on different objects (you and the wall), so they don't cancel."
    },
    
    {
        "id": 4,
        "misconception": "acceleration_velocity_same",
        "question": "A car is traveling at 60 mph with the cruise control on (constant speed). What is its acceleration?",
        "options": ["A) 60 mph", "B) Zero", "C) Increasing", "D) 60 m/s²"],
        "correct_answer": "B",
        "explanation": "Constant velocity means zero acceleration. Acceleration is the rate of change of velocity."
    },
    
    {
        "id": 5,
        "misconception": "rest_means_no_forces",
        "question": "A book sits at rest on a table. What can you say about the forces on the book?",
        "options": ["A) No forces act on it", "B) Only gravity acts on it", "C) Forces are balanced (net force = 0)", "D) Upward force is greater"],
        "correct_answer": "C",
        "explanation": "Gravity pulls down, normal force pushes up. They balance (net force = 0), so the book doesn't accelerate."
    },
    
    {
        "id": 6,
        "misconception": "heavy_falls_faster",
        "question": "On Earth (with air), a feather falls slower than a rock. Why?",
        "options": ["A) The feather is lighter", "B) Air resistance affects them differently", "C) Gravity pulls less on the feather", "D) The rock has more force"],
        "correct_answer": "B",
        "explanation": "Both experience the same gravitational acceleration, but air resistance affects the feather more due to its shape and low mass."
    },
    
    {
        "id": 7,
        "misconception": "force_equals_velocity",
        "question": "A car accelerates from rest. As its speed increases, what happens to the net force (assuming constant acceleration)?",
        "options": ["A) Increases with speed", "B) Decreases", "C) Stays constant", "D) Becomes zero"],
        "correct_answer": "C",
        "explanation": "Constant acceleration requires constant net force (F=ma). Force doesn't depend on velocity."
    },
    
    {
        "id": 8,
        "misconception": "acceleration_velocity_same",
        "question": "At the highest point of a ball's trajectory (thrown upward), what is its acceleration?",
        "options": ["A) Zero", "B) 9.8 m/s² downward", "C) 9.8 m/s² upward", "D) Equal to its velocity"],
        "correct_answer": "B",
        "explanation": "Even though velocity is momentarily zero at the top, acceleration is always 9.8 m/s² downward (gravity)."
    },
    
    {
        "id": 9,
        "misconception": "action_reaction_cancel",
        "question": "A horse pulls a cart. The cart pulls back on the horse with equal force. Why does the cart move?",
        "options": ["A) The forces cancel", "B) Horse pulls harder", "C) Forces act on different objects", "D) Cart has less friction"],
        "correct_answer": "C",
        "explanation": "The action-reaction pair acts on different objects. The cart moves because the net force ON THE CART is forward."
    },
    
    {
        "id": 10,
        "misconception": "rest_means_no_forces",
        "question": "You stand still on the ground. How many forces act on you?",
        "options": ["A) Zero", "B) One (gravity)", "C) Two (gravity and normal force)", "D) Three"],
        "correct_answer": "C",
        "explanation": "Gravity pulls you down, the ground pushes you up (normal force). They balance, so you remain at rest."
    }
]

def get_questions_by_misconception(misconception_key):
    """Get all test questions related to a specific misconception"""
    return [q for q in TEST_QUESTIONS if q["misconception"] == misconception_key]

def get_all_questions():
    """Get all test questions"""
    return TEST_QUESTIONS