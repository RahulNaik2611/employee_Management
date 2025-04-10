
# Employee Management System

A complete CRUD (Create, Read, Update, Delete) application built with Django 5.2 for managing employee records.

---

## Features
- ✅ Create, Read, Update, Delete employee records  
- 🖥️ Responsive web interface with Bootstrap 5  
- 🔐 Admin interface for advanced management  
- 📊 Employee model with comprehensive fields

---

## Project Structure

```
Employee-Management/
└── Curd/
    ├── manage.py
    ├── DjangoCurd/
    │   ├── settings.py         # Django project settings
    │   └── urls.py             # Main URL configuration
    └── employee/
        ├── migrations/         # Database migrations
        ├── templates/          # HTML templates
        │   ├── base.html       # Base template (inherited by others)
        │   ├── create.html     # Employee creation/editing form
        │   ├── list.html       # Employee listing table
        │   └── delete.html     # Delete confirmation page
        ├── models.py           # Employee model definition
        ├── views.py            # CRUD operation logic
        ├── urls.py             # App-specific URLs
        └── admin.py            # Admin panel configuration
```

---

## Templates Overview

- **base.html**  
  • Main template that all other templates inherit from  
  • Bootstrap 5 integration  
  • Navigation bar  
  • Consistent layout across all pages

- **list.html**  
  • Displays all employees in a table  
  • Sortable employee data  
  • Action buttons (Edit/Delete)  
  • "Add New Employee" button

- **create.html**  
  • Handles both creating and updating employees  
  • Dynamic title (Create/Update)  
  • Django form rendering  
  • Save/Cancel buttons

- **delete.html**  
  • Confirmation page before deletion  
  • Warning message  
  • Confirm/Cancel options  
  • Prevents accidental deletions

---

## Installation
1. **Clone the repository and navigate into it:**
   ```bash
   git clone https://github.com/RahulNaik2611/Employee-Management.git
   cd Employee-Management
   ```
2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install django
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

---

## Accessing the Application
- **Admin Interface:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Employee List:** [http://localhost:8000/employees/](http://localhost:8000/employees/)
- **Add Employee:** [http://localhost:8000/employees/create/](http://localhost:8000/employees/create/)

---

## License
MIT License

---

## Contributing
1. Fork the repository  
2. Create your feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/your-feature
   ```
5. Create a pull request

---

## 👋 About Me

I’m **B Rahul Naik**, a 💻 tech enthusiast with a background in **Mechanical Engineering (B.Tech, 2022)** and a passion for building real-world software solutions. After discovering my strong interest in **computer science and technology**, I transitioned into software development and data analytics.

🛠️ My toolkit includes **Python, Java, Spring Boot, SQL (PostgreSQL, MS SQL Server, MongoDB)**, and **Power BI**. I'm actively sharpening my skills in **SQL**, exploring advanced topics like **Joins, Window Functions, CTEs, Stored Procedures**, and **Performance Tuning**.

🚀 I’ve built projects using **Django** and **Bootstrap**, such as the *Employee Management System*, showcasing my ability to create scalable web apps with clean, user-friendly interfaces.

🔍 I'm driven by curiosity, love solving problems, and am always looking to grow as a developer and data professional.
```
