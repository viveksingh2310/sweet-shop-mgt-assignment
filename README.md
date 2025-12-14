**Sweet Shop Management System**
# DEPLOYED LINK :- https://sweet-shop-mgt-assignment-2.onrender.com/
## IMPORTANT INSTRUCTION FOR ACCESSING ADMIN ROUTES
### Register using "admin@gmail.com" with password as "admin". THEN ONLY YOU CAN ACCESS THE ADMIN ROUTES.
# **MY AI USAGE**
-Used AI to select best backend and frontend technology that I should use to make the best of my known and worked technology. AI told me to use Fastapi + Vue (because i already worked in MERN)
-making decision about which database should i use that should be simpler for me to avoid learning new thing.
-knowing command to initiate project both in backend and frontend
-understanding developing diff server for backend and frontend
-understanding and implementing hashing though correct syntax.
-developing some prior test cases.
-interpreting the various api endpoints (converting the given task documnet api endpoint to simpler words)
-designing ideas and resolving issues in forntend connectivity to backend on render.

## What is the Project?

The **Sweet Shop Management System** is a full-stack web application designed to manage sweets mgt.
Contains user authentication, role-based access control, and complete CRUD operations for sweets along with purchasing and restocking of sweet.

The system distinguishes between **regular users** and **admin users**:
- Regular users can view sweets and purchase them.
- Admin users can add, update, restock, and delete sweets.

The application is built using a **FastAPI** and **Vue.js**, making it scalable, secure, and easy to maintain.

---
# **OUTPUT**

<img width="807" height="376" alt="Screenshot 2025-12-14 204907" src="https://github.com/user-attachments/assets/5ee9b703-75a8-4a25-ae67-7fe568277315" />

<img width="717" height="414" alt="Screenshot 2025-12-14 204912" src="https://github.com/user-attachments/assets/cedbb4bf-7b61-4720-b69f-3d5a7eae510a" />


<img width="1053" height="511" alt="Screenshot 2025-12-14 204941" src="https://github.com/user-attachments/assets/2ad234d5-fd6f-4c18-a0aa-e35197bbf59e" />

<img width="978" height="553" alt="Screenshot 2025-12-14 204919" src="https://github.com/user-attachments/assets/08800212-0775-4836-b3da-26b9165f9ef5" />

<img width="1053" height="511" alt="Screenshot 2025-12-14 204941" src="https://github.com/user-attachments/assets/6e6cde9f-7f19-41f4-a824-057f9636c425" />


## 🛠️ Technologies Used

### Backend
- **FastAPI** – REST API framework
- **Python 3.13**
- **PostgreSQL** – Database (Render managed DB)
- **SQLAlchemy (Async)** – ORM
- **asyncpg** – Async PostgreSQL driver
- **JWT Authentication** – Secure login
- **Argon2** – Password hashing
- **Uvicorn** – ASGI server

### Frontend
- **Vue.js (Vite)** – Frontend framework
- **Axios** – API communication
- **JavaScript / HTML / CSS**

### Dev & Testing
- **Pytest** – Automated testing
- **pytest-asyncio** – Async test support
- **HTTPX** – API testing
- **Render** – Cloud deployment

---

## TEST CASES RESULT
Total 16 test cases where there and all were passed through pytest.

<img width="1685" height="679" alt="test cases result" src="https://github.com/user-attachments/assets/7ff4944f-c6f7-428e-9ef7-dd06b5e218dc" />

## ⚙️ Setup Instructions

## IMPORTANT INSTRUCTION FOR ACCESSING ADMIN ROUTES
### Register using "admin@gmail.com" with password as "admin". THEN ONLY YOU CAN ACCESS THE ADMIN ROUTES.
### 1 Backend Setup
First install all deps.
Go to the backend and run pytest to evaluate the outcome of various python test cases. Later run this command --> python -m uvicorn app.main:app --reload
### 2 Frontend Setup 
npm install 
npm run dev


