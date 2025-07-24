# Simple Django Web Project

This repository contains a simple Django web application structured for modular development and learning purposes.

## Project Structure

- `manage.py` — Django's command-line utility for administrative tasks.
- `db.sqlite3` — SQLite database file.
- `simple_test_site/` — Main project configuration (settings, URLs, WSGI/ASGI).
- `members/` — Django app for user/member management.
- `pages/` — Django app for static and contact pages.
- `polls/` — Django app for polls and voting functionality.

Each app contains:
- `models.py` — Database models.
- `views.py` — View logic.
- `urls.py` — URL routing.
- `admin.py` — Admin interface configuration.
- `templates/` — HTML templates.
- `migrations/` — Database migrations.
