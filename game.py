import streamlit as st
import random
st.sidebar.header("Select to play game")
page=st.sidebar.radio("games",["User guessing","Machine guessing"])
if page=="User guessing":
# Function to initialize or reset the game
    start=st.number_input("Enter start value",min_value=1)
    end=st.number_input("Enter end value",min_value=1,max_value=100)
    if start>=end:
        st.write("start value is less than end value")
    else:
        if "number_to_guess" not in st.session_state:
            # Generate a random number between 1 and 100
            st.session_state.number_to_guess = random.randint(start,end)
            # Store the number in the session state so that it persists across reruns
            st.session_state.attempts = 0
            st.session_state.game_over = False
    
# Check if the game has been initialized, if not, initialize it


    # Title of the game
    st.title("Guess the Number Game")

    # Show instructions
    st.write("I have selected a random number between 1 and 100.")
    st.write("Try to guess it in as few attempts as possible.")

    # Input box for the user to make a guess
    guess = st.number_input("Your Guess:", min_value=1, max_value=100, step=1)

    # Button to submit the guess
    if st.button("Submit Guess"):
        if guess < st.session_state.number_to_guess:
            st.write("Too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulation,you won the game {st.session_state.number_to_guess}.")
            st.session_state.game_over = True
    # Increment the number of guesse
        st.session_state.attempts+= 1
        if not st.session_state.game_over:
            st.write(f"Number of guesses: {st.session_state.attempts}")

elif page=="Machine guessing":

    
    if "min_value" not in st.session_state:
        st.session_state.min_value = 1
        st.session_state.max_value = 100
        st.session_state.attempts = 0
        st.session_state.machine_guess = (st.session_state.min_value + st.session_state.max_value) // 2
        st.session_state.game_active = False

    # Title
    st.title("Simple Machine Guessing Game")
    st.write("Think of a number within the range you set, and the machine will try to guess it!")

        # Step 1: Get the range from the player
    min_value = st.number_input("Enter the minimum value for the range:", value=1)
    max_value = st.number_input("Enter the maximum value for the range:", value=100)

        # Start the game
    if st.button("Start Game"):
            if min_value >= max_value:
                st.write("Minimum value must be less than the maximum value.")
            else:
                
                st.session_state.min_value = min_value
                st.session_state.max_value = max_value
                st.session_state.attempts = 1
                st.session_state.machine_guess = (min_value + max_value) // 2
                st.session_state.game_active = True
                st.write(f"The machine's guess is {st.session_state.machine_guess}")
    if st.session_state.game_active:
            feedback = st.radio("How is the machine's guess?", ("Correct", "Too Low", "Too High"))

            if st.button("Submit Feedback"):
                if feedback == "Correct":
                    st.write(f"The machine guessed it! The number was {st.session_state.machine_guess}.")
                    st.write(f"Attempts: {st.session_state.attempts}")
                    st.session_state.game_active = False  # End the game
                else:
                    # Update the range based on feedback
                    if feedback == "Too Low":
                        st.session_state.min_value = st.session_state.machine_guess + 1
                    elif feedback == "Too High":
                        st.session_state.max_value = st.session_state.machine_guess - 1

                    # Make a new guess
                    st.session_state.machine_guess = (st.session_state.min_value + st.session_state.max_value) // 2
                    st.session_state.attempts += 1
                    st.write(f"The machine's new guess is {st.session_state.machine_guess}")


