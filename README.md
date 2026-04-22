# Kubernetes Voting App

A production-style microservices voting application orchestrated with Kubernetes and automated via GitHub Actions.

## 🏗️ Architecture
The application consists of five microservices communicating in real-time:
- Vote Service: Python (Flask) frontend for user voting.
- Result Service
- Worker Service
- Redis: In-memory message queue.
- PostgreSQL: Persistent database storage.

## CI/CD Pipeline
This project features a fully automated CI/CD workflow:
- GitHub Actions: Automatically builds and pushes Docker images to Docker Hub on every push to the `main` branch.
- Docker Hub: Hosts the custom images under the `isrealdev` namespace.

## Kubernetes Deployment
To deploy this application to a cluster (like Minikube):

1. Clone the repo and navigate to the `k8s` directory.
2. Apply the manifests:
   ```bash
   kubectl apply -f k8s/