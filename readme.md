# Kaffa - Coffee Shop Web Application

Kaffa is a full-stack web application for a modern coffee shop, built with Django and styled with Tailwind CSS. It aims to provide a seamless online experience for customers to browse the menu, learn about the shop, manage their orders, and for administrators to manage the shop's offerings.

## Features

*   **User Authentication:** Secure sign-up, sign-in, and sign-out functionality for customers.
*   **Menu Display:** Browse a dynamic menu of coffee, beverages, and other items.
*   **Product Details:** View detailed information for each menu item.
*   **Shopping Cart:** Add items to a cart and manage cart contents.
*   **Order Management:** (Assumed based on "Orders" link) Place orders and view order history.
*   **About Us Page:** Learn more about Kaffa coffee shop.
*   **Responsive Design:** Styled with Tailwind CSS for a consistent experience across devices.
*   **Admin Interface:** Django's built-in admin panel for easy management of data (users, products, categories, orders, etc.).

## Technologies Used

*   **Backend:**
    *   Python
    *   Django
    *   Django REST framework (if APIs are planned/used, otherwise remove)
*   **Frontend:**
    *   HTML
    *   Tailwind CSS (via `django-tailwind`)
    *   JavaScript (for any client-side interactivity)
*   **Database:**
    *   SQLite (for development, as configured in `settings.py`)
*   **Development Tools:**
    *   `django-browser-reload` for live reloading during development.

## Project Structure

The project follows a standard Django application structure:

```
kaffa/
├── kaffa/          # Main Django project configuration (settings.py, urls.py)
├── base/           # Core app, likely for base templates, static assets
├── menu/           # App for handling menu items, categories, products
├── users/          # App for user authentication and profiles (custom User model)
├── theme/          # Django-tailwind theme app (static_src for Tailwind config, input.css)
├── static/         # Collected static files (managed by Django)
├── media/          # User-uploaded media files (if any)
├── venv/           # Virtual environment (recommended)
├── db.sqlite3      # Development database
├── manage.py       # Django's command-line utility
└── README.md       # This file
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd kaffa
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file: `pip freeze > requirements.txt`)*

4.  **Install Node.js and npm/yarn** (if not already installed). This is required by `django-tailwind`.

5.  **Install Tailwind CSS dependencies:**
    Navigate to your theme app directory (where `package.json` would be, typically `theme/`) and run:
    ```bash
    # If you have a package.json from django-tailwind init
    # cd theme
    # npm install 
    # cd .. 
    # Or, django-tailwind might handle this internally during build.
    # For a fresh setup, you might need to initialize tailwind in the theme app:
    # python manage.py tailwind init
    ```

6.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

8.  **Build Tailwind CSS:**
    ```bash
    python manage.py tailwind build
    ```

## Running the Application

1.  **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```
2.  **Start the Tailwind CSS watch process (for development, in a separate terminal):**
    ```bash
    python manage.py tailwind start
    ```
3.  Open your browser and navigate to `http://127.0.0.1:8000/`.

## Future Enhancements

*   Online payment integration.
*   Real-time order tracking.
*   Customer reviews and ratings.
*   Admin dashboard for analytics.
*   Deployment to a production environment (e.g., Heroku, AWS, DigitalOcean).

---

Happy Kaffanating! ☕

```

**Key things I've included:**

*   **Project Title and Description:** A brief overview.
*   **Features:** Based on your `base.html` and common coffee shop app features.
*   **Technologies Used:** Pulled from your `settings.py` and `tailwind.config.js`.
*   **Project Structure:** A simplified view of a typical Django project like yours.
*   **Setup and Installation:** Standard steps for a Django project, including `django-tailwind` considerations. I've added a note about creating `requirements.txt`.
*   **Running the Application:** How to start the dev server and Tailwind.
*   **Future Enhancements:** Some ideas to inspire further development.