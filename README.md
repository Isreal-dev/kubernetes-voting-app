# Kubernetes Voting App

A microservices-based voting application deployed using Docker and Kubernetes.

## Tech Stack
- Python (Flask)
- Redis
- PostgreSQL
- Docker
- Kubernetes

## Features
- Vote between Cats and Dogs
- Real-time result processing
- Multi-container architecture

## Run with Docker Compose
docker-compose up --build

## Run with Kubernetes
kubectl apply -f k8s/

## Access App
kubectl port-forward service/vote-service 5000:80