import streamlit as st

def home():
    st.set_page_config(page_title="Decoding Data Science Blog", page_icon=":guardsman:", layout="wide", initial_sidebar_state="expanded")
    st.title("Decoding Data Science Blog")
    st.write("This is the home page.")
    st.set_bg_color("#f5f5f5")

home = """
# Decoding Data Science Blog

Stay tuned for more updates!
"""

def display_page(page):
    if page == "Home":
        st.markdown(home)
        st.image("path/to/image.png", caption="Image caption")
    elif page == "Machine Learning":
        st.markdown("## Machine Learning: Transforming Data into Insights")
        st.markdown("Insert your article here.")
        st.image("path/to/image.png", caption="Image caption")
    elif page == "Data Visualization":
        st.markdown("## Data Visualization: Telling Stories with Data")
        st.markdown("Insert your article here.")
        st.image("path/to/image.png", caption="Image caption")
    elif page == "Code Crafted":
        st.markdown("## Code Crafted: Mastering the Art of Programming")
        st.markdown("Insert your article here.")
        st.image("path/to/image.png", caption="Image caption")
    elif page == "Analytics":
        st.markdown("## Analytics: Unveiling Trends and Patterns")
        st.markdown("Insert your article here.")
        st.image("path/to/image.png", caption="Image caption")
    elif page == "Contribution Guidelines":
        st.markdown("## Contribution Guidelines")
        st.markdown("Insert your article here.")
        st.image("path/to/image.png", caption="Image caption")
    elif page == "Code of Conduct":
        st.markdown("## Code of Conduct")
        st.markdown("Insert your article here.")
        st.image("path/to/image.png", caption="Image caption")

def main():
    pages = {
        "Home": home,
        "Machine Learning": ("Machine Learning: Transforming Data into Insights", "machine_learning.md"),
        "Data Visualization": ("Data Visualization: Telling Stories with Data", "data_visualization.md"),
        "Code Crafted": ("Code Crafted: Mastering the Art of Programming", "code_crafted.md"),
        "Analytics": ("Analytics: Unveiling Trends and Patterns", "analytics.md"),
        "Contribution Guidelines": ("Contribution Guidelines", "contribution_guidelines.md"),
        "Code of Conduct": ("Code of Conduct", "code_of_conduct.md"),
    }

    st.set_page_config(page_title="Decoding Data Science Blog")

    st.sidebar.title("Pages")
    page = st.sidebar.radio("", tuple(pages.keys()))

    display_page(page)

if __name__ == "__main__":
    main()






