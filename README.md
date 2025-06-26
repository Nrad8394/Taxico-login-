# Taxico Login

This project is a web application for managing taxi company logins and related features. It is built using Django (Python) for the backend and includes a frontend with HTML, CSS, and JavaScript assets.

## Features
- User authentication and login system
- Responsive frontend design using Bootstrap
- Static and media file management
- SQLite3 database for development

## Project Structure
```
├── db.sqlite3                # SQLite database file
├── manage.py                 # Django management script
├── adpitor-html/             # Frontend HTML, CSS, JS assets
│   ├── index.html
│   ├── css/
│   ├── fonts/
│   ├── images/
│   └── js/
├── base/                     # Django app (core logic)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todo_list/                # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- (Optional) Virtual environment tool (venv, virtualenv, etc.)

### Installation
1. **Clone the repository:**
   ```powershell
   git clone <repository-url>
   cd Taxico-login-
   ```
2. **Create and activate a virtual environment (recommended):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install django
   ```
4. **Apply migrations:**
   ```powershell
   python manage.py migrate
   ```
5. **Run the development server:**
   ```powershell
   python manage.py runserver
   ```
6. **Access the app:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Frontend
- The `adpitor-html/` folder contains all static assets for the frontend, including HTML, CSS, JS, fonts, and images.
- You can customize the UI by editing files in this directory.

## Django Apps
- `base/`: Contains core Django app logic (models, views, admin, etc.)
- `todo_list/`: Project settings and configuration

## License
Specify your license here (e.g., MIT, GPL, etc.)

## Author
- Your Name

---
Feel free to update this README with more details as your project evolves.
