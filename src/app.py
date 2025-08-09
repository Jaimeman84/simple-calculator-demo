import streamlit as st
from calculator import Calculator

def main():
    st.set_page_config(
        page_title="Simple Calculator",
        page_icon="🧮",
        layout="centered"
    )
    
    st.title("Simple Calculator 🧮")
    st.write("A clean and simple calculator built with Streamlit")
    
    # Initialize calculator
    calc = Calculator()
    
    # Create three columns for input and operation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        num1 = st.number_input("First Number", value=0.0, step=0.1)
    
    with col2:
        operation = st.selectbox(
            "Operation",
            ["+", "-", "*", "/"],
            index=0
        )
    
    with col3:
        num2 = st.number_input("Second Number", value=0.0, step=0.1)
    
    # Add some spacing
    st.write("")
    
    # Center the calculate button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        calculate = st.button("Calculate", use_container_width=True)
    
    # Show result in a nice box
    if calculate:
        try:
            result = calc.calculate(num1, num2, operation)
            st.success(f"Result: {result}")
        except ValueError as e:
            st.error(str(e))
    
    # Add a simple footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Built with ❤️ using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 