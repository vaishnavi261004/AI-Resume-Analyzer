
import requests

API_URL = "http://127.0.0.1:8000"


# ---------------- LOGIN ---------------- #

def login(email, password):

    return requests.post(
        f"{API_URL}/auth/login",
        json={
            "email": email,
            "password": password
        }
    )


# ---------------- REGISTER ---------------- #

def register(name, email, password):

    return requests.post(
        f"{API_URL}/auth/register",
        json={
            "name": name,
            "email": email,
            "password": password
        }
    )


# ---------------- ANALYZE ---------------- #

def analyze_resume(token, uploaded_file, job_description):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    data = {
        "job_description": job_description
    }

    return requests.post(
        f"{API_URL}/resume/analyze",
        headers=headers,
        files=files,
        data=data
    )


# ---------------- HISTORY ---------------- #

def get_history(token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/history/",
        headers=headers
    )