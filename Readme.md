# Django Demo Project

This is a Django web application with a members management system.

## Project Structure

```
demo/
├── demo/               # Project configuration directory
│   ├── settings.py     # Project settings
│   ├── urls.py         # Project URL configuration
│   └── wsgi.py         # WSGI configuration
├── members/            # Members app directory
│   ├── admin.py        # Admin interface configuration
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── urls.py         # App URL configuration
│   └── templates/      # HTML templates
└── manage.py          # Django management script
```

## Prerequisites

- Python 3.13
- pip (Python package installer)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/HemantRaj-2005/django-demo.git
cd django_demo
```

2. Create a virtual environment:
```bash
python -m venv myenv
```

3. Activate the virtual environment:

For Windows:
```bash
myenv\Scripts\activate
```

For Unix or MacOS:
```bash
source myenv/bin/activate
```

4. Install required packages:
```bash
pip install django
```

5. Navigate to the project directory:
```bash
cd demo
```

6. Apply database migrations:
```bash
python manage.py migrate
```

7. Create a superuser (admin) account:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

## Accessing the Admin Interface

1. Go to `http://localhost:8000/admin`

2. Log in with your superuser credentials

## Development

- To create new database migrations:
```bash
python manage.py makemigrations
```

- To apply migrations:
```bash
python manage.py migrate
```

## Additional Notes

- The project uses SQLite as the default database
- Static files are served from the `staticfiles` directory
- Media files are stored in the `media` directory