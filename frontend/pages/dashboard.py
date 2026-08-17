
import streamlit as st
from services.api import analyze_resume


def show_dashboard():

    st.title("📄 AI Resume Analyzer")

    st.write("Upload your resume and paste the Job Description.")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "doc", "docx"]
    )

    job_description = st.text_area(
        "Job Description",
        height=250
    )

    if st.button("Analyze Resume", use_container_width=True):

        if uploaded_file is None:
            st.warning("Please upload a resume.")
            return

        if job_description.strip() == "":
            st.warning("Please enter a Job Description.")
            return

        with st.spinner("Analyzing Resume..."):

            response = analyze_resume(
                st.session_state["token"],
                uploaded_file,
                job_description
            )

        if response.status_code != 200:
            st.error(response.text)
            return

        result = response.json()

        st.success("Analysis Completed Successfully! ✅")

        st.divider()

        st.metric(
            "Match Score",
            f"{result['match_score']}%"
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Strengths")

            if result["strengths"]:
                for skill in result["strengths"]:
                    st.success(skill)
            else:
                st.info("No strengths found.")

        with col2:

            st.subheader("❌ Missing Skills")

            if result["missing_skills"]:
                for skill in result["missing_skills"]:
                    st.error(skill)
            else:
                st.info("No missing skills.")

        st.divider()

        st.subheader("💡 Suggestions")

        if result["suggestions"]:
            for suggestion in result["suggestions"]:
                st.info(suggestion)
        else:
            st.success("No suggestions. Great match!")