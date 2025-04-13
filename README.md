# 🏨 SOA Final Project – Microservices-based Hotel/Cottage Booking Platform

[![CI](https://github.com/muneer7031/SOA-Final-Project/actions/workflows/ci.yml/badge.svg)](https://github.com/muneer7031/SOA-Final-Project/actions)

## 📘 Project Overview

This project simulates a real-world microservices-based hotel/cottage booking system. It demonstrates the core principles of:

- Modular microservice design
- RESTful API interaction
- Docker-based containerization
- Kubernetes-based orchestration
- CI/CD automation and monitoring

The system includes services for user registration, order handling, and notification delivery — all developed and deployed locally using Docker Desktop with Kubernetes support.

---

## 🔧 Key Activities Implemented

| Activity                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| ✅ Microservices        | Separate services for `user`, `order`, and `notification` with clear APIs  |
| ✅ Containerization     | Dockerfiles created and services containerized                             |
| ✅ Docker Compose       | Used for local multi-container development                                 |
| ✅ Kubernetes Setup     | YAML files created for deployments and services                            |
| ✅ CI/CD Pipeline       | GitHub Actions pipeline implemented for test and deploy                    |
| ✅ Monitoring           | HPA used with `kubectl` + logging via `kubectl logs`                       |

---

## 🧱 Microservices Overview

| Microservice          | Responsibility                                      |
|-----------------------|------------------------------------------------------|
| `user_service`        | Handles user registration and retrieval              |
| `order_service`       | Processes user bookings *(optional placeholder)*     |
| `notification_service`| Sends email-style notifications                      |

Each service is self-contained, RESTful, and scalable.

---

## 🐳 Docker Usage

### Build and Run with Docker Compose

```bash
docker-compose up --build
Access Locally:
User Service: http://localhost:5000/register

Notification Service: http://localhost:5001/send_notification

☸️ Kubernetes Deployment (Docker Desktop)
Apply Kubernetes Resources
bash
Copy
Edit
kubectl apply -f k8s/
Verify Pods & Services
bash
Copy
Edit
kubectl get pods
kubectl get services
Port Forward Services
bash
Copy
Edit
kubectl port-forward deployment/user-service 8080:5000
kubectl port-forward deployment/notification-service 8181:5001
✅ CI/CD – GitHub Actions
Workflow triggered on every push to main

Runs automated test cases for all microservices

File: .github/workflows/ci.yml

✅ Latest run status badge above

🧪 Testing
Unit and integration tests included:

bash
Copy
Edit
user_service/test_app.py
notification_service/test_app.py
Run locally:

bash
Copy
Edit
python test_app.py
CI pipeline also executes these automatically via GitHub Actions.

📊 Monitoring and Scaling
Horizontal Pod Autoscaler (HPA) for user-service:

bash
Copy
Edit
kubectl autoscale deployment user-service --cpu-percent=50 --min=1 --max=5
Basic logs available via:

bash
Copy
Edit
kubectl logs -l app=user-service
✅ Metrics Server installed and connected

📁 Folder Structure
sql
Copy
Edit
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
├── order_service/                 # (optional placeholder)
├── docker-compose.yml
├── k8s/
│   ├── user-deployment.yaml
│   ├── user-service.yaml
│   ├── notification-deployment.yaml
│   ├── notification-service.yaml
│   ├── order-deployment.yaml
│   └── order-service.yaml
└── .github/
    └── workflows/
        └── ci.yml
📦 Deliverables Summary
Deliverable	Status
Code Repository (GitHub)	✅ Complete
Docker Images (Local Build)	✅ Done
Kubernetes Manifests (YAML)	✅ Done
CI/CD Pipeline	✅ Done
Local Demo via Docker Desktop K8s	✅ Done
Documentation (This README)	✅ Done
Final Presentation (TBD)	🚧 Upcoming
🧠 Author
Mohammed Muneer
🔗 GitHub: https://github.com/muneer7031

