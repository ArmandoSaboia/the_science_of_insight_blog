# app.py
import streamlit as st

def home():
    st.title("The Science of Insight Blog")
    st.write("Explore the fascinating world of data science!")

def machine_learning():
    st.title("Machine Learning: Transforming Data into Insights")
    with open("machine_learning.md", "r") as file:
        st.markdown(file.read())

def data_visualization():
    st.title("Data Visualization: Telling Stories with Data")
    with open("data_visualization.md", "r") as file:
        st.markdown(file.read())

def main():
    pages = {
        "Home": home,
        "Machine Learning": machine_learning,
        "Data Visualization": data_visualization,
    }

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    pages[selected_page]()

if __name__ == "__main__":
    main()

