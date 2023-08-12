import streamlit as st

def main():
    st.title("Number Square and Cube Calculator")
    
    # User input for the number
    number = st.number_input("Enter a number:", step=1)
    
    # Calculate square and cube
    square = number ** 2
    cube = number ** 3
    
    # Display results
    st.write(f"Square of {number} is: {square}")
    st.write(f"Cube of {number} is: {cube}")

if __name__ == "__main__":
    main()
