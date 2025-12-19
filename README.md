# Simple To-Do List App

A clean and simple To-Do List application built with **Django 5.2**. This app allows users to manage their daily tasks with a modern, mobile-friendly interface.

## 🚀 Features

-   **Create Tasks**: Add tasks with a title and optional description.
-   **Read Tasks**: View all valid tasks in a clean list layout.
-   **Update Tasks**: Edit task details easily.
-   **Delete Tasks**: Remove tasks with a confirmation prompt.
-   **Toggle Status**: Mark tasks as completed or pending directly from the list.
-   **Visual Feedback**: Completed tasks are visually distinct (strikethrough styling).
-   **Responsive Design**: Works great on mobile and desktop.

## 🛠️ Tech Stack

-   **Backend**: Python, Django 5.2
-   **Frontend**: HTML5, CSS3 (Custom styling, no heavy frameworks)
-   **Database**: SQLite (Default)

## 📦 Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository
If you have the project folder, simply navigate into it:
```bash
cd "1. Simple To-Do List"
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
Set up the database tables.
```bash
python manage.py migrate
```

### 5. Run the Server
Start the development server.
```bash
python manage.py runserver
```

Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📂 Project Structure

-   `tasks/`: Main application directory containing models, views, and templates.
-   `tasks/templates/tasks/`: HTML templates for the UI.
-   `tasks/static/tasks/`: CSS and static assets.
-   `todo_project/`: Project configuration (settings, URLs).
-   `db.sqlite3`: Local development database.
