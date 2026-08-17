
# 📄 AI Resume Analyzer

An AI-powered full-stack web application that analyzes resumes against job descriptions and provides an ATS-style match score, missing skills, strengths, and improvement suggestions.

## 🚀 Features

- 🔐 User registration and login
- 🔑 JWT-based authentication
- 📄 PDF and DOCX resume upload
- 🤖 AI-powered resume analysis using Groq LLM
- 📊 Resume-to-job-description match score
- ✅ Identifies resume strengths
- ❌ Identifies missing skills
- 💡 Provides AI-generated improvement suggestions
- 📚 User-specific analysis history
- 🗄️ PostgreSQL database
- 🖥️ Streamlit frontend
- ⚡ FastAPI backend

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT Authentication
- Pydantic

### Frontend
- Streamlit

### AI
- Groq API
- Llama 3.3 70B

### Other
- Git
- GitHub

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
               FastAPI REST API
                      │
                      ▼
              JWT Authentication
                      │
                      ▼
                Resume Parser
                      │
                      ▼
                  Groq LLM
                      │
                      ▼
              Analysis Result
                 ┌────┴────┐
                 ▼         ▼
          PostgreSQL    Streamlit
                 │         │
                 ▼         ▼
        Analysis History  Dashboard
```

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── backend/
│   ├── apps/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── resume.py
│   │   │   └── history.py
│   │   │
│   │   ├── database/
│   │   │   ├── base.py
│   │   │   └── database.py
│   │   │
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   │   ├── ai/
│   │   │   ├── analysis/
│   │   │   ├── auth/
│   │   │   └── resume/
│   │   │
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── alembic.ini
│   └── requirements.txt
│
├── frontend/
│   ├── pages/
│   │   ├── login.py
│   │   ├── register.py
│   │   ├── dashboard.py
│   │   └── history.py
│   │
│   ├── services/
│   │   └── api.py
│   │
│   ├── assets/
│   │   └── style.css
│   │
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔄 Application Flow

1. User registers an account.
2. User logs in and receives a JWT token.
3. User uploads a resume in PDF or DOCX format.
4. User enters a job description.
5. Streamlit sends the resume and job description to the FastAPI backend.
6. FastAPI authenticates the user using JWT.
7. The backend extracts text from the uploaded resume.
8. The resume text and job description are sent to the Groq LLM.
9. The AI generates:
   - Match score
   - Strengths
   - Missing skills
   - Improvement suggestions
10. The analysis is stored in PostgreSQL.
11. The analysis result is displayed on the Streamlit dashboard.
12. Previous analyses can be viewed through the History section.

## 🔐 Authentication & Security

- JWT authentication is used to protect authenticated API endpoints.
- User passwords are securely hashed before storage.
- Environment variables are used for API keys, database credentials, and application secrets.
- Analysis history is associated with the authenticated user.
- Personal resume files are excluded from Git using `.gitignore`.
- Sensitive configuration files such as `.env` are not committed to the repository.

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/vaishnavi261004/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file with the required configuration:

```env
DATABASE_URL=your_postgresql_connection_string
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_secret_key
```

Do not commit the `.env` file or expose API keys publicly.

### 6. Start the FastAPI Backend

Open a terminal:

```bash
cd backend
python -m uvicorn apps.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

### 7. Start the Streamlit Frontend

Open a second terminal:

```bash
cd frontend
streamlit run app.py
```

The frontend will run at:

```text
http://localhost:8501
```

## 🤖 AI Analysis

The application uses the Groq API with the Llama 3.3 70B model to compare resume content with a provided job description.

The AI generates a structured analysis containing:

```text
Match Score
     ↓
Strengths
     ↓
Missing Skills
     ↓
Improvement Suggestions
```

The model is instructed to return structured JSON so that the backend can process and display the results in the Streamlit interface.

## 🗄️ Database

PostgreSQL is used to store application data.

SQLAlchemy is used as the ORM layer, while Alembic is used to manage database schema migrations.

The application maintains user-specific analysis history so that authenticated users can access their previous resume analyses.

## 🔌 API Endpoints

The backend provides RESTful API endpoints for:

- User registration
- User login
- Resume analysis
- Analysis history
- Database health testing

Interactive API documentation is available through FastAPI Swagger UI:

```text
http://127.0.0.1:8000/docs
```


## 🚧 Future Improvements

- Resume improvement and rewriting suggestions
- Resume keyword optimization
- Downloadable analysis reports
- Multiple job-description comparison
- Cloud deployment
- Improved ATS scoring methodology
- More detailed analytics dashboard
- Support for additional resume formats

## 👩‍💻 Author

**Vaishnavi**

GitHub:  
https://github.com/vaishnavi261004