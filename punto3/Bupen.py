# States: q0 (Off), q1 (Waiting), q2 (Access Granted), q3 (Access Denied)

#Description: Show a welcome message
def welcome():
    print("---------WELCOME TO BUPEN---------")

#Descrition: initial state
def initial_state():
    return "q0"

# Description: Handles the state transitions for the AFD
def transition(current_state, input_id):
    if current_state == "q0":
        if input_id == "power_on":
            return "q1"

    elif current_state == "q1":
        if input_id.startswith("student_id:"):
            student_id = input_id.split(":")[1]
            if valid_student_id(student_id):
                return "q2"
            else:
                return "q3"

    elif current_state in ["q2", "q3"]:
        if input_id == "power_on":
            return "q1"
    return current_state

# Description: Check if the student ID has 9 digits and if it starts with the year from 2000 to 2025
# Example: valid_student_id("202459736") -> True
def valid_student_id(student_id):
    if student_id.isdigit() and len(student_id) == 9:
        first_digits = int(student_id[:4])
        return 2000 <= first_digits <= 2025
    else:
        return False

# Description: Simulates the execution of the AFD
def simulate_access(inputs):
    welcome()
    state = initial_state()
    print("Initial State:", state)
    for symbol in inputs:
        state = transition(state, symbol)
        print(f"Input: {symbol} --> New State: {state}")
    if state == "q0":
        print("Bupen is turned off")
    elif state == "q1":
        print("Waiting for Student ID")
    elif state == "q2":
        print("Access Granted")
    elif state == "q3":
        print("Access Denied")

# Run the program
if __name__ == '__main__':
    simulate_access(["power_on", "student_id:202312345"])
    simulate_access(["power_on", "student_id:2059736"])
    simulate_access(["power", "student_id:202459736"])
    simulate_access(["power_on", "student_id:150059736"])
    simulate_access(["power_on", ""])