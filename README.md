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
