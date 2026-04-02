# 🚀 GitHub Connector API (FastAPI)

## 📌 Overview

This project is a backend API built using FastAPI that integrates with GitHub.
It allows users to perform actions like fetching repositories, creating issues, listing issues, creating pull requests, and fetching commits.

---

## ⚙️ Features

* Fetch repositories of any user
* List issues of a repository
* Create issues in a repository
* Create pull requests (bonus)
* Fetch commits from a repository
* Secure authentication using GitHub Personal Access Token (PAT)

---

## 🛠️ Tech Stack

* Backend: Python
* Framework: FastAPI
* HTTP Client: Requests
* Environment Management: python-dotenv

---

## 🔐 Authentication

This project uses a GitHub Personal Access Token (PAT) for authentication.
The token is stored securely in a `.env` file and not hardcoded in the source code.

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/pradeepprasad12/github-connector.git
cd github-connector
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install fastapi uvicorn requests python-dotenv
```

---

### 4. Create `.env` file

```env
GITHUB_TOKEN=your_personal_access_token
```

---

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

---

## ▶️ How to Run

After starting the server, open:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This opens the interactive Swagger UI where you can test all APIs.

---

## 🌐 API Endpoints

### 🔹 1. Fetch Repositories

```http
GET /github/repos/{username}

```

---

### 🔹 2. List Issues

```http
GET /github/issues/{owner}/{repo}
```

---

### 🔹 3. Create Issue

```http
POST /github/create-issue
```

#### Request Body:

```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "Issue title",
  "body": "Issue description"
}
```

---

### 🔹 4. Create Pull Request (Bonus)

```http
POST /github/create-pr
```

#### Request Body:

```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "PR title",
  "body": "PR description",
  "head": "feature-branch",
  "base": "main"
}
```

---

### 🔹 5. Fetch Commits

```http
GET /github/commits/{owner}/{repo}
```

---

## ⚠️ Important Notes

* Ensure your GitHub token has `repo` permissions
* Pull requests require:
  * Existing branches
  * New commits in the source branch
* Private repositories require proper access permissions

---

## 🎯 Conclusion

This project demonstrates:

* API integration with GitHub
* Secure authentication handling
* Clean backend architecture using FastAPI
* Real-world backend development practices
