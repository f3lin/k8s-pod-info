# k8s-pod-info

A FastAPI-based web application that displays key Kubernetes cluster information such as Pod name, Namespace, Pod IP, and Node name. This app dynamically retrieves these details from the Kubernetes environment using fieldRef and presents them in a simple web interface.

## Features

- Displays Kubernetes Pod and Cluster information:
  - Pod Name
  - Namespace
  - Pod IP
  - Node Name
- Responsive web UI built with Jinja2 templates
- Easily deployable in any Kubernetes cluster
- Environment variables are dynamically populated via Kubernetes field references
- Built using FastAPI for high performance and flexibility

## Technologies Used

- **FastAPI**: For building the web application
- **Jinja2**: For templating the HTML output
- **Kubernetes**: To retrieve and display the cluster and pod information
- **Docker**: For containerizing the application

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/f3lin/k8-cluster-info.git
   cd k8-cluster-info
   ```
2. Build the Docker image:
   ```bash
   docker build -t k8s-pod-info .
   ```
3. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 k8s-pod-info
   ```
4. Deploy in a Kubernetes cluster (example YAML provided):
   ```bash
   cd k8s 
   kubectl apply -f k8s-pod-info.yaml
   ```

[Docker image](https://hub.docker.com/layers/f3lin/cluster-info/v0.1.1/images/sha256:6387c98c5e40db45ed3cc3f4eac8b5a8753f086deb29951af5535518d3a27407?uuid=7123C56A-6193-43DD-A3DF-70B2678620CC)


