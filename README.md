# 🚀 SupaChat – Conversational Analytics App

SupaChat is a full-stack DevOps project that enables users to query a PostgreSQL database (Supabase) using natural language and visualize results as tables and charts.

---

## 🎯 Project Overview

SupaChat allows users to:
- Ask questions in plain English
- Convert queries → SQL
- Fetch data from Supabase PostgreSQL
- Display results as:
  - Chat responses
  - Tables
  - Graphs (Recharts)

---

## 🏗️ Architecture

```

User (Browser)
↓
Frontend (Next.js)
↓
Nginx Reverse Proxy
↓
Backend (FastAPI)
↓
Supabase PostgreSQL

````

### Components:

- **Frontend**: Next.js (React UI)
- **Backend**: FastAPI (API + query processing)
- **Database**: Supabase PostgreSQL
- **Reverse Proxy**: Nginx
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana

---

## ⚙️ Features

### ✅ Frontend
- Chatbot UI
- Query input box
- Query history
- Results table
- Graphs using Recharts
- Loading & error states

### ✅ Backend
- Natural language → SQL conversion
- Supabase integration
- API endpoints:
  - `/query`
  - `/health`

---

## 🛠️ Tech Stack

### Frontend
- Next.js
- React
- Recharts
- Tailwind CSS

### Backend
- FastAPI
- Python
- Supabase client

### DevOps / Infra
- Docker
- Docker Compose
- Nginx
- AWS EC2
- GitHub Actions

### Monitoring
- Prometheus
- Grafana

---

## 🚀 Setup (Local Development)

### 1️⃣ Clone Repo
```bash
git clone https://github.com/muthuraj-rajarathinam/supachat.git
cd supachat
````

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env`:

```
SUPABASE_URL=your_url
SUPABASE_ANON_KEY=your_key
```

Run:

```bash
uvicorn app.main:app --reload
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🐳 Docker Setup

```bash
docker-compose up --build
```

App will run on:

* Frontend → [http://localhost:3000](http://localhost:3000)
* Backend → [http://localhost:8000](http://localhost:8000)

---

## 🌐 Deployment (AWS EC2)

### Steps:

1. Launch EC2 instance (Amazon Linux)
2. Install:

   * Docker
   * Docker Compose
3. Clone repo:

```bash
git clone https://github.com/YOUR_USERNAME/supachat.git
cd supachat
```

4. Run containers:

```bash
docker-compose up -d
```

---

## 🔁 CI/CD Pipeline

### GitHub Actions

Pipeline automates:

* Code checkout
* Frontend build
* Backend setup
* SSH deployment to EC2

### Workflow:

```
Push → GitHub Actions → SSH → EC2 → Deploy
```

---

## 🌐 Nginx Reverse Proxy

Routing:

* `/` → Frontend
* `/api` → Backend

Features:

* Gzip compression
* WebSocket support
* API routing

---

## 📊 Monitoring

### Prometheus

* Collects metrics:

  * CPU usage
  * Memory usage
  * Container stats

### Grafana

* Dashboards for:

  * System health
  * API performance
  * Container metrics

---

## 📸 Dashboards
Check Screenshot Folder for all images

---

## 🤖 AI Tools Used

* ChatGPT (architecture, debugging, DevOps guidance)
* GitHub Copilot (code assistance)
* Claude (Debuging Long Log Error)

---

## ⚠️ Challenges Faced

* Docker Buildx compatibility issue on Amazon Linux
* Resolved by:

  * Using `docker build`
  * Updating compose to use prebuilt images
    
* Secrets Passing problem:
  *  Use Github Secrets to pass Key encrypted privately


---

## 📈 Future Improvements

* Add authentication and keep chat history
* Improve NLP → SQL accuracy
* Add caching layer
* Add alerting system
* Kubernetes deployment
* Use Devops Agent

---

---

## 💡 Key Highlight

This project demonstrates:

* Full-stack development
* Real-world DevOps practices
* CI/CD automation
* Cloud deployment
* Monitoring setup

---

## 👨‍💻 Author

Muthuraj
---
