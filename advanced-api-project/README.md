
## Customizations
### 1. **Form Validation**
- `publication_year` cannot be set to a future year.
- Implemented in both `BookCreateView` and `BookUpdateView` using the `perform_create` and `perform_update` hooks.

### 2. **Permissions**
- `ListView` and `DetailView` → open to all users (`AllowAny`).
- `CreateView`, `UpdateView`, and `DeleteView` → restricted to authenticated users only (`IsAuthenticated`).

### 3. **Filters**
- Search functionality added for `title` and `author` fields using DRF's `SearchFilter`.

---

## Settings
In `settings.py`, ensure the following for global permissions and authentication:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
