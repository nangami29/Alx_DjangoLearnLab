# Django Blog Project

This is a simple blog application built with Django. It allows users to create, read, update, and delete (CRUD) blog posts.  
It also includes permissions and access control to ensure only the right people can edit or delete posts.

## Features
# Post List (`/posts/`)
- Displays all blog posts.
- Open to everyone (no login required).
- Posts are ordered by newest first.

# Post Detail (`/posts/<id>/`)
- Displays a single post with full content.
- Open to everyone (no login required).
- If the logged-in user is the author, they will see **Edit** and **Delete** options.

# Create Post (`/posts/new/`)
- Available only to authenticated (logged-in) users.
- The logged-in user is automatically set as the **author**.
- Requires a **title** and **content**.

#Edit Post (`/posts/<id>/edit/`)
- Available only to the **author** of the post.
- Allows editing the title and content.
- Redirects back to the post list upon successful update.

#Delete Post (`/posts/<id>/delete/`)

 Permissions
- Anyone: Can view the post list and post detail pages.
- Logged-in users: Can create posts.
- Authors only: Can edit or delete their own posts.
- Unauthorized users trying to edit/delete are redirected.