# **StudentProject**

This project is a Django-based web application containerized using Docker and integrated with a CI/CD pipeline via Jenkins. It demonstrates the use of Docker for containerization, Jenkins for automated builds, and Docker Hub for image storage and sharing.

---

## **Features**
- A Django-based web application.
- Docker containerization for easy deployment.
- CI/CD pipeline using Jenkins:
  - Pulls the code from a Git repository.
  - Builds the Docker image.
  - Pushes the Docker image to Docker Hub.
- Docker image hosted on Docker Hub.

---

## **Prerequisites**
Before running this project, ensure the following tools are installed on your system:
1. **Python 3.10 or higher** (for Django 5.x compatibility).
2. **Docker**.
3. **Jenkins** (for CI/CD pipeline).
4. **Git** (for pulling the project repository).

---

## **Getting Started**

### **Step 1: Clone the Repository**
Pull the source code from the Git repository:

git clone https://github.com/SRCEM-AIML/C47_Harsh-Vardhan-Khajuria.git
cd C47_Harsh-Vardhan-Khajuria/StudentProject

---

### **Step 2: Run the Django Development Server (Locally)**
1. Set up a Python virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
---
### **Install Dependencies**
2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
---
### **Start the Django Development Server**
3. Run the Django development server:
   ```bash
   python manage.py runserver
---
### **Open Your Browser and Visit**
http://127.0.0.1:8000/

---

### **Step 3: Run the Project Using Docker**
1. Build the Docker image:
   ```bash
   docker build -t studentproject .
---
### **Run the Docker Container**
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 studentproject
---
### **Access the Application**
3. Open your browser and visit : http://127.0.0.1:8000/

---

### **Step 4: CI/CD Pipeline with Jenkins**
1. Ensure Jenkins is set up and running.
2. Create a new pipeline job in Jenkins.
3. Configure the pipeline to use your `Jenkinsfile`:
   - **Stages**:
     - Pull the code from the Git repository.
     - Build the Docker image using the `Dockerfile`.
     - Push the Docker image to your Docker Hub repository.
4. Trigger the pipeline manually or via a webhook.

---

### **Step 5: Docker Hub**
1. Your Docker image is pushed to Docker Hub. You can pull it using:
   ```bash
   docker pull harshvardhan295/django_project:latest

