
import streamlit as st
from services.api import register


def show_register():

    st.title("📄 AI Resume Analyzer")

    st.subheader("Create Account")

    name = st.text_input("Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Register", use_container_width=True):

        if (
            name.strip() == ""
            or email.strip() == ""
            or password.strip() == ""
            or confirm_password.strip() == ""
        ):
            st.warning("Please fill all fields.")
            return

        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        with st.spinner("Creating account..."):

            response = register(
                name,
                email,
                password
            )

        if response.status_code not in (200, 201):

            try:
                st.error(response.json()["detail"])
            except Exception:
                st.error("Registration failed.")

            return

        st.success("Registration Successful! ✅")

        st.info("Please go to the Login page and sign in.")