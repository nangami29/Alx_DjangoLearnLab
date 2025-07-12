# Django Permissions & Groups Setup

## Custom Permissions
Defined in `Book` model:
- `can_view`: View books.
- `can_create`: Create books.
- `can_edit`: Edit books.
- `can_delete`: Delete books.

## Groups
Automatically created after migrations:
- **Editors** → `can_edit`, `can_create`, `can_view`
- **Viewers** → `can_view`
- **Admins** → `can_view`, `can_create`, `can_edit`, `can_delete`

## How to Use
1. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
