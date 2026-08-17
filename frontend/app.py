
import streamlit as st

from pages.login import show_login
from pages.register import show_register
from pages.dashboard import show_dashboard
from pages.history import show_history

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "login"

# ---------------- NOT LOGGED IN ---------------- #

if "token" not in st.session_state:

    st.sidebar.title("📄 AI Resume Analyzer")

    choice = st.sidebar.radio(
        "Menu",
        ["Login", "Register"]
    )

    if choice == "Login":
        show_login()

    else:
        show_register()

# ---------------- LOGGED IN ---------------- #

else:

    st.sidebar.title("📄 AI Resume Analyzer")

    page = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "History"]
    )

    if page == "Dashboard":
        show_dashboard()

    elif page == "History":
        show_history()

    st.sidebar.divider()

    if st.sidebar.button("Logout"):

        del st.session_state["token"]

        st.success("Logged out successfully.")

        st.rerun()