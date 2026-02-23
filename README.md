📚 CS3337 Spring Project – Book Exchange Web Application
📌 Overview

This project is a full-stack Book Exchange and Management Web Application developed as part of the CS3337 Software Engineering course.

The application allows users to browse, manage, and maintain book listings through a web interface built with Django. It demonstrates backend development, database integration, and core software engineering principles.

🚀 Features
  📖 View available book listings
  ➕ Add new books to the system
  ✏️ Edit and update existing book records
  ❌ Delete books from the database
  🗄️ Persistent data storage using SQLite
  🌐 Dynamic page rendering using Django templates

🏗️ Architecture
  The application follows the Model-View-Template (MVT) architecture provided by Django:
    Models – Define the database schema and structure for books
    Views – Handle request logic and backend processing
    Templates – Render dynamic HTML pages for users
    URLs – Route incoming requests to appropriate views

🛠️ Technologies Used
  Python
  Django
  SQLite
  HTML
  CSS

Git & GitHub

📂 Project Structure
CS3337Spring2Project/
│
├── manage.py
├── db.sqlite3
├── bookEx/        # Main project configuration
├── bookMng/       # Application for book management
└── templates/     # HTML templates
⚙️ Installation & Setup

Follow these steps to run the project locally:

1️⃣ Clone the Repository
  git clone https://github.com/carlosromero9970/CS3337Spring2Project.git
  cd CS3337Spring2Project

2️⃣ Create Virtual Environment (Optional but Recommended)
  python -m venv venv
  source venv/bin/activate   # Mac/Linux
  venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
  pip install django

4️⃣ Run Migrations
  python manage.py migrate

5️⃣ Start the Development Server
  python manage.py runserver

Then open your browser and go to:
  http://127.0.0.1:8000/
🎯 Learning Outcomes

Through this project, I:
  Implemented a full-stack web application using Django
  Designed and connected a relational database using Django ORM
  Applied CRUD operations in a real-world web application
  Practiced modular software design and MVC/MVT architecture
  Used Git for version control and project management
