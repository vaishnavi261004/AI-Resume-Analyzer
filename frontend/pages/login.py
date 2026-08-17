
import streamlit as st
from services.api import login


def show_login():

    st.title("📄 AI Resume Analyzer")

    st.subheader("Login")

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        if email.strip() == "" or password.strip() == "":
            st.warning("Please fill all fields.")
            return

        with st.spinner("Logging in..."):

            response = login(
                email,
                password
            )

        if response.status_code != 200:

            try:
                st.error(response.json()["detail"])
            except:
                st.error("Login Failed")

            return

        data = response.json()

        st.session_state["token"] = data["access_token"]

        st.success("Login Successful ✅")

        st.rerun()