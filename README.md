# 🚀 Smart ML-Powered CI/CD Pipeline
### Developed by **Krrish Chopra**

A simple but impressive CI/CD pipeline that uses **Machine Learning** to predict build failure before running the pipeline.  
If the model predicts high risk, the pipeline automatically **stops the build**, saving time and preventing bad deployments.

This project also builds a Docker image and pushes it to **GitHub Container Registry (GHCR)** using GitHub Actions.

---

##  Features
- **ML-based risk prediction** using build logs  
- **Smart CI/CD** (auto-stop on high-risk builds)  
- **Dockerized Flask app**  
- **Automatic image push to GHCR**  
- **Fully automated GitHub Actions workflow**

---

## Architecture
```
Push to GitHub → GitHub Actions
      │
      ▼
 Train ML Model → Predict Risk
      │
      ├── High Risk (>0.5) → ❌ Stop Pipeline
      ▼
 Build Docker Image
      ▼
 Push to GHCR
```

---

##  Docker (Local Usage)

```
docker build -t smart-ci-app .
docker run -p 5000:5000 smart-ci-app
```

---

##  Tech Stack
- Python, Flask  
- Scikit-learn (ML)  
- Docker  
- GitHub Actions  
- GitHub Container Registry (GHCR)

---

##  Short Summary

> Built a **Machine Learning enabled CI/CD pipeline** that automatically predicts build failure risk and blocks unsafe builds.  
> Automated Docker image creation and publishing to **GitHub Container Registry (GHCR)** using GitHub Actions.

---
