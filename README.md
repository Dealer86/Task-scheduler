# Task Scheduler

Task Scheduler is a web application built using Django that allows users to manage their tasks efficiently. It consists of two main apps, `tasks` and `users`, enabling users to create, update, delete, and search for tasks. Users can also register, log in, and log out, ensuring a personalized experience.

## Features

- **User Registration and Authentication:** Users can register for an account and log in to access their tasks.
- **Task Management:** Users can create, update, and delete tasks, including specifying a task name and deadline.
- **Task Search:** Users can search for tasks using keywords.
- **Task Export:** Users can export their tasks in CSV format.
- **User Logout:** Users can log out of their accounts.
- **About Page:** A simple "About" page providing information about the application.

## Installation

Follow these steps to set up the Task Scheduler project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/Dealer86/Task-scheduler.git>

2. **Create a virtual environment**
   ```bash
   python -m venv venv

3. **Activate the virtual environment**
   ```bash
   venv\Scripts\activate

4. **Install project dependencies:**
   ```bash
   pip install -r requirements.txt

5. **Navigate to the project directory:**
    ```bash
   cd task_scheduler

6. **Apply database migrations:**
   ```bash
   python manage.py migrate

7. **Start the development server:**
   ```bash
   python manage.py runserver

8. **Access the application in your web browser at your [localhost](http://127.0.0.1:8000/)**

## Usage
- Visit the application in your web browser.
Register a new account or log in with your existing credentials.
Create, update, and delete tasks on the "Home" page.
Use the search bar to find tasks by keyword.
Access the "About" page for information about the application.
Log out when done.

## Technology Stack

Task Scheduler is a web application developed using a technology stack that combines various tools and frameworks to create a robust and functional project. Here's an overview of the key components in the technology stack used for Task Scheduler:



**Django** is the primary web framework used to build Task Scheduler.



**Python** is the programming language in which Task Scheduler is implemented.



**Bootstrap 4** is used for the application's user interface and styling.



**jQuery** is a JavaScript library that simplifies handling client-side interactions and events on web pages.



**django-crispy-forms** is a package that enhances the rendering of Django forms.



**SQLite** is the default database system used by Django.



**Git** is used for version control.



**GitHub** for hosting and collaborating on Git repositories.



Standard **HTML and CSS** for creating web pages and defining the application's visual style. 



**Task Scheduler** utilizes various **third-party Django packages** to simplify and enhance specific functionalities, such as:

- `bootstrap_datepicker_plus`: Provides date and time picker widgets in forms.
- `django.contrib.auth`: Handles user authentication and authorization.
## Testing
- **Unit Tests**: Using Django's built-in testing framework.
- **Continuous Integration**: This project uses GitHub Actions for automated continuous integration.
[![Django CI](https://github.com/Dealer86/Task-scheduler/actions/workflows/django.yml/badge.svg)](https://github.com/Dealer86/Task-scheduler/actions/workflows/django.yml)