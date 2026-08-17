
import os
import json
from urllib import response
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def analyze_resume(resume_text: str,job_description: str):
    prompt = f"""
You are an ATS Resume Analyzer.

Compare the resume with the given job description.

Return ONLY valid JSON.

JSON format:

{{
    "match_score": 0,
    "missing_skills": [],
    "strengths": [],
    "suggestions": []
}}

Resume:

{resume_text}

Job Description:

{job_description}

"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )
    content = response.choices[0].message.content.strip()
    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        return {
            "error": "AI returned invalid JSON",
            "raw_response": content
        }

 