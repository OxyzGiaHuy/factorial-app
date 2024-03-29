import streamlit as st
from factorial import factorial

def main():
    st.title("AIO 2024 - Factorial Calculator")
    number = st.number_input("Enter a number (from 0 to 900): ", 
                             min_value=0,
                             max_value=900)
    if st.button("Calculate"):
        result = factorial(number)
        st.write(f"The factorial of {number} is {result}.")
        st.balloons()

if __name__ == "__main__":
    main()

