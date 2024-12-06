# **To-Do List Application**

## **Overview**
This is a web-based To-Do List application that allows users to manage their tasks efficiently. The app includes functionalities for creating, reading, updating, and deleting tasks (CRUD operations). It also features REST API integration and supports task filtering and validation.

The project demonstrates a complete backend implementation with robust validation checks and testing to ensure reliability.

---

## **Features**
- **Task Management**:
  - Create, read, update, and delete tasks.
  - Validation to ensure the due date is not earlier than the creation timestamp.
- **REST APIs**:
  - Fully functional API endpoints for managing tasks.
- **Admin Interface**:
  - Manage tasks and users through the Django Admin interface.
- **Testing**:
  - Unit tests, integration tests, and E2E tests with 100% code coverage.
- **Live Deployment**:
  - Hosted on Heroku for easy access.

---

## **API Endpoints**
### **1. Task Endpoints**
| Method | Endpoint             | Description          |
|--------|-----------------------|----------------------|
| GET    | `/api/tasks/`         | Retrieve all tasks.  |
| POST   | `/api/tasks/`         | Create a new task.   |
| GET    | `/api/tasks/<id>/`    | Retrieve a task.     |
| PUT    | `/api/tasks/<id>/`    | Update a task.       |
| DELETE | `/api/tasks/<id>/`    | Delete a task.       |

### **Request/Response Examples**
#### **Create a Task (POST `/api/tasks/`)**
Request:
```json
{
  "title": "New Task",
  "description": "This is a new task.",
  "due_date": "2024-12-31",
  "status": "OPEN"
}
```
Response:
```json
{
  "id": 1,
  "title": "New Task",
  "description": "This is a new task.",
  "due_date": "2024-12-31",
  "status": "OPEN",
  "timestamp": "2024-12-05T10:00:00Z"
}
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/Krishnaparab0508/todo-app.git
cd todo-app
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set Up the Database**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **4. Create a Superuser (for Admin Access)**
```bash
python manage.py createsuperuser
```

### **5. Run the Development Server**
```bash
python manage.py runserver
```
- Access the app at `http://127.0.0.1:8000`.

---

## **Testing**
### **Run All Tests**
To ensure the code is working correctly:
```bash
python manage.py test
```

## **Deployment**
The application is hosted on **Heroku**:
- [Live Link](https://my-new-todo-app-6124f2bbfcdc.herokuapp.com/)

**Admin Credentials**:
- Username: `<your_admin_username>`
- Password: `<your_admin_password>`

---

## **Developer Information**
- **Developed by**: Krishna Dashrath Parab  
- **GitHub**: [Krishnaparab0508](https://github.com/Krishnaparab0508)  
- **LinkedIn**: [Krishna Parab](http://www.linkedin.com/in/parabkrishna/)  

---



