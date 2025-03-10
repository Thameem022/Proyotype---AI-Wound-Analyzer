# Proyotype---AI-Wound-Analyzer

## Features
-  **User Authentication**: Register and log in securely.
-  **API Integration**: Expose APIs for external applications.
-  **Dockerized Deployment**: Run using Docker and Docker Compose.
-  **AWS S3 Support**: Stores wound images in AWS S3.

---

## 🖥️ How to Run the Project

### **1. Clone the Repository**
```bash
git clone https://github.com/Thameem022/Proyotype---AI-Wound-Analyzer.git
cd Proyotype---AI-Wound-Analyzer

### **2. Modify the .env copy and update it**

### **3. Build & Run with Docker**
docker-compose up --build

Example cURL Commands:

1. curl -X POST http://127.0.0.1:5000/register \
    -H "Content-Type: application/json" \
    -d '{
        "username": "new_user",
        "email": "new_user@example.com",
        "password": "securepassword"
    }'

2. curl -X POST http://127.0.0.1:5000/login \
    -H "Content-Type: application/json" \
    -d '{
        "email": "new_user@example.com",
        "password": "securepassword"
    }'

3. curl -X POST http://127.0.0.1:5000/upload \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -F "file=@/path/to/image.jpg"

4. docker-compose down