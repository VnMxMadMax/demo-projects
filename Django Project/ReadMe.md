# 📝 Django Blog App

A fully functional blog web application built with **Django**, featuring:

- User registration & authentication
- Post creation and detail view
- Like button with animation
- Commenting system
- Dark theme UI with Bootstrap
- Media support (images, videos)
- Clean and modular folder structure

---

## 🚀 Features

- 🔐 User Registration and Login
- 📰 Post List and Detailed View
- ❤️ Like System (with real-time UI update)
- 💬 Comment Section per Post
- 🌙 Dark Mode Layout (via Bootstrap)
- 📁 Media File Handling (Images & Videos)
- ⚙️ Separate Apps: `blog/`, `users/`

---

## 🗂️ Project Structure

```
django-blog/
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── media/
│   ├── images/
│   └── videos/
├── personal_blog/
│   └── settings.py (in original project, this folder holds settings)
├── templates/
│   └── base.html
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── venv/
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

---

## 🔐 Admin Access

Create a superuser to access the Django admin dashboard:

```bash
python manage.py createsuperuser
```

---

## 📸 Screenshots

- Home Page
  
  ![image](https://github.com/user-attachments/assets/fb969a33-e663-404b-b4a8-c1d914f26629)

- Post Blog or Content Page

  ![image](https://github.com/user-attachments/assets/76933a94-dd4c-460a-acbd-15f69e331790)

- Like + Comment System

  ![image](https://github.com/user-attachments/assets/8f0b0bde-6936-43df-9bac-7c116ff1dbee)

- Register Page

  ![image](https://github.com/user-attachments/assets/d9170fb6-91c6-4558-958a-29c1f311eba2)

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📦 Tech Stack

- **Backend:** Django 5.2.1
- **Frontend:** HTML, CSS, Bootstrap 5, Font Awesome
- **Database:** SQLite
- **Python Version:** 3.13.2

---

## 📁 .gitignore Example

```gitignore
venv/
__pycache__/
*.pyc
db.sqlite3
media/
.env
```

---

## 🙌 Acknowledgements

- Inspired by modern blogging platforms
- Thanks to the Django open-source community

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📽️ Demo Video
https://www.loom.com/share/eb7727ab4e554f88ba16f0d90f1d8cae
https://www.loom.com/share/88e5935dd6af4baca75cc19b979143ca

