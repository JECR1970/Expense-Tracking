import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab


st.title("Expense Tracking System")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFF0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()


#to run: streamlit run app.py