# 🏨 SOA Final Project – Online Hotel/Cottage Booking Platform

[![CI](https://github.com/muneer7031/SOA-Final-Project/actions/workflows/ci.yml/badge.svg)](https://github.com/muneer7031/SOA-Final-Project/actions)

## 📘 Project Description

A microservices-based hotel/cottage booking service that allows users to register and receive booking-related notifications via email. Built using Python (Flask), Docker, and Kubernetes.

---

## 🧱 Microservices Overview

| Service              | Description                                      |
|----------------------|--------------------------------------------------|
| `user_service`       | Handles user registration, authentication        |
| `notification_service` | Sends email/SMS notifications to users         |
| `order_service` *(optional)* | (Placeholder for booking logic)           |

Each service is independently containerized and exposed using Kubernetes deployments and services.

---

## 🐳 How to Run (Docker Compose)

```bash
docker-compose up --build



Access Services:
Visit: http://localhost:5000/register – User Service

Visit: http://localhost:5001/send_notification – Notification Service

☸️ Kubernetes Deployment
To deploy all services in your local Kubernetes cluster:


kubectl apply -f k8s/
To verify deployments:


kubectl get pods
kubectl get services
To access endpoints via port forwarding:


kubectl port-forward deployment/user-service 8080:5000
kubectl port-forward deployment/notification-service 8081:5001
✅ CI/CD – GitHub Actions
Every push to the main branch triggers automated CI tests

Status badge reflects real-time build status

Workflow file path: .github/workflows/ci.yml

🧪 Testing
Unit tests are included for both services:


user_service/test_app.py
notification_service/test_app.py
Run locally:


python test_app.py
Or automatically via GitHub Actions CI pipeline.

📊 Monitoring
Horizontal Pod Autoscaling (HPA):


kubectl autoscale deployment user-service --cpu-percent=50 --min=1 --max=5
View logs:

kubectl logs -l app=user-service
Optional: Use Metrics Server to track CPU and memory usage for autoscaling.

📁 Folder Structure

SOA-Final-Project/
├── user_service/
│   ├── app.py
│   ├── test_app.py
│   ├── Dockerfile
│   └── requirements.txt
├── notification_service/
│   ├── app.py
│   ├── test_app.py
│   ├── Dockerfile
│   └── requirements.txt
├── order_service/                 # (Optional placeholder)
├── docker-compose.yml
├── k8s/                           # Kubernetes YAMLs
│   ├── user-deployment.yaml
│   ├── user-service.yaml
│   ├── notification-deployment.yaml
│   ├── notification-service.yaml
│   ├── order-deployment.yaml
│   └── order-service.yaml
└── .github/
    └── workflows/
        └── ci.yml
🧠 Author
Muneer7031
🔗 GitHub: https://github.com/muneer7031