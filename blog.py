import streamlit as st

# Function to set page title and background color
def set_page_properties(title, background_color="#f4f4f4"):
    st.set_page_config(
        page_title=title,
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # Apply background color
    st.markdown(
        f"""
        <style>
            body {{
                background-color: {background_color};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Function to load markdown content from file
def load_markdown_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def home():
    set_page_properties("The Science of Insight Blog")
    st.title("Welcome to The Science of Insight Blog")
    st.write("Explore the fascinating world of data science!")

def display_content(title, file_path):
    set_page_properties(title)
    st.title(title)
    content = load_markdown_file(file_path)
    st.markdown(content)

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

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    if selected_page == "Home":
        pages[selected_page]()
    else:
        display_content(*pages[selected_page])

if __name__ == "__main__":
    main()

