
# Flask CRUD Application

A simple and lightweight CRUD (Create, Read, Update, Delete) web application built using Python's Flask framework. This project demonstrates basic CRUD operations with a relational database and provides a clean foundation for learning Flask.

---

## Features

- **Create**: Add new records to the database  
- **Read**: Retrieve and display records  
- **Update**: Modify existing records  
- **Delete**: Remove records from the database  
- Responsive interface using HTML and Bootstrap  

---

## Technologies Used

- **Backend:** Python 3.x, Flask  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Forms & Validation:** Flask-WTF  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database Migrations:** Flask-Migrate  

---

## Project Structure

```
app.py           → Main application file  
models.py        → Database models  
forms.py         → Web forms  
templates/       → HTML templates  
    layout.html  → Base layout template  
    index.html   → Homepage to list records  
    add.html     → Form to add a record  
    edit.html    → Form to edit a record  
    delete.html  → Delete confirmation page  
migrations/      → Database migrations  
requirements.txt → Project dependencies  
README.md        → Project documentation  
```

---

## Installation

### Prerequisites

- Python 3.x  
- pip (Python package installer)  

### Setup Steps

1. **Clone the repository:**

```bash
git clone https://github.com/khansaurooj/flask-CRUD-app.git
cd flask-CRUD-app
```

2. **Create a virtual environment:**

```bash
python -m venv venv
```

3. **Activate the virtual environment:**

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

4. **Install dependencies:**

```bash
pip install -r requirements.txt
```

5. **Initialize the database:**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Run the application:**

```bash
flask run
```

7. **Open your browser:**  
Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Usage

- **Homepage:** View all records  
- **Add:** Create a new record  
- **Edit:** Update an existing record  
- **Delete:** Remove a record  

All changes are saved to the SQLite database.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)  
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)  
- [Bootstrap Framework](https://getbootstrap.com/)  
