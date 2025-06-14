# Pablo Nicolas Marin Gonzalez 2459440
# Daniel Antonio Hoyos Ruiz 202459736

# Teacher: Luis Germán Toro Pareja
# Group number: 52
# Laboratory 5

# States: q0 (Off), q1 (Waiting), q2 (Access Granted), q3 (Access Denied)

def welcome():
    """Display welcome message for Bupen system"""
    print("---------WELCOME TO BUPEN---------")

def initial_state():
    """Return the initial state of the system"""
    return "q0"

def transition(current_state, input_id):
    """
        str: New state after processing the input
    """
    if current_state == "q0":
        # Transition from Off state
        if input_id == "power_on":
            return "q1"  # Turn system on
        else:
            return "q0"  # Remain off

    elif current_state == "q1":
        # Waiting state for student ID
        if input_id.startswith("student_id:"):
            student_id = input_id.split(":")[1]
            if valid_student_id(student_id):
                return "q2"  # Valid ID - grant access
            else:
                return "q3"  # Invalid ID - deny access
        else:
            return "q1"  # Remain in waiting state

    elif current_state in ["q2", "q3"]:
        # After access granted/denied
        if input_id == "power_on":
            return "q1"  # Reset to waiting state
        else:
            return current_state  # Remain in current state
    
    return current_state  # Default: stay in current state

def valid_student_id(student_id):
    """"
    Validation rules:
    - Must be 9 digits
    - First 4 digits must represent a year between 2000-2025
    """
    if student_id.isdigit() and len(student_id) == 9:
        first_digits = int(student_id[:4])
        return 2000 <= first_digits <= 2025
    else:
        return False

def get_user_input():

    print("\nAvailable commands:")
    print("1. power_on - Turn on the system")
    print("2. student_id:XXXXXXX - Enter student ID (9 digits)")
    print("3. exit - Exit the system")
    
    return input("\nEnter a command: ").strip()

def main():
    """Main function to run the system simulation"""
    state = initial_state()
    welcome()
    
    print("\nInitial state:", state)
    print("Bupen is powered off. Enter 'power_on' to turn it on.")
    
    while True:
        user_input = get_user_input()
        
        if user_input.lower() == "exit":
            print("\nSystem powered off. Goodbye!")
            break
            
        # Update state based on user input
        new_state = transition(state, user_input)
        print(f"Input: {user_input} --> New state: {new_state}")
        
        # Display state messages
        if new_state == "q0":
            print("Bupen is powered off")
        elif new_state == "q1":
            print("Waiting for student ID")
        elif new_state == "q2":
            print("ACCESS GRANTED! Welcome to the library.")
        elif new_state == "q3":
            print("ACCESS DENIED: Invalid student ID")
        
        state = new_state

if __name__ == '__main__':
    main()
