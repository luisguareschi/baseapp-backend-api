# BaseApp Backend API

A Django-based REST API witth custom user authentication.

## Features

- Custom user authentication using JWT (JSON Web Tokens)
- Email-based authentication
- Django admin interface with custom theme
- CORS support for frontend integration
- RESTful API endpoints

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository:
2. Create a virtual enviroment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Install theme: 

```bash
python manage.py loaddata admin_interface_theme_uswds.json
```

5. Create superuser:

```bash
python manage.py createsuperuser
```

6. Run development server:

```bash
python manage.py runserver
```
