
import streamlit as st
from services.api import get_history


def show_history():

    st.title("📜 Analysis History")

    response = get_history(st.session_state["token"])

    if response.status_code != 200:
        st.error("Unable to load history.")
        return

    history = response.json()

    if len(history) == 0:
        st.info("No previous analyses found.")
        return

    for item in history:

        with st.container(border=True):

            st.subheader(item["resume_name"])

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Match Score",
                    f"{item['match_score']}%"
                )

            with col2:
                st.write("**Analyzed On**")
                st.write(item["created_at"])

            st.write("### ✅ Strengths")

            if item["strengths"]:
                strengths = item["strengths"].split("\n")

                for skill in strengths:
                    if skill.strip():
                        st.write(f"• {skill}")

            st.write("### ❌ Missing Skills")

            if item["missing_skills"]:
                missing = item["missing_skills"].split("\n")

                for skill in missing:
                    if skill.strip():
                        st.write(f"• {skill}")

            st.write("### 💡 Suggestions")

            if item["suggestions"]:
                suggestions = item["suggestions"].split("\n")

                for suggestion in suggestions:
                    if suggestion.strip():
                        st.write(f"• {suggestion}")

            st.divider()