# AI Reflections Blog (Django)


A compact Django blog used for Module 2 deliverables: Auth, CRUD (Post/Comment), role-based permissions, Bootstrap 5 UI, HTMX (inline edit + live search), WCAG 2.2 notes, and GitHub Actions CI.


## Quickstart (local)
```bash
cd django_blog
python -m venv .venv && source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
