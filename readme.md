# Blog Project

## Setup

### Prerequisites

    - Python 3.6+
    - Django 4.2.14
    - Virtual environment (optional but recommended)

### Installation

    1. Clone the repository:
        Terminal....
            git clone https://github.com/OPanurag/blog_project.git
            cd blog_project


    2. Create and activate a virtual environment:
        Terminal....
            python -m venv venv
            source venv/bin/activate  # On Windows use `venv\Scripts\activate`


    3. Install the dependencies:
        Terminal....
            pip install -r requirements.txt


    4. Apply the migrations:
        Terminal....
            python manage.py migrate


    5. Create a superuser:
        Terminal....
            python manage.py createsuperuser


    6. Run the development server:
        Terminal....
            python manage.py runserver


    7. Access the application at `http://127.0.0.1:8000/`

    8. Deployment

        I have deployed this project on 'Render'.

        You can use following link to use this application as a fully deployed website
            Link -> https://blogproject-rrfr.onrender.com



## Running Tests

    To ensure that everything is working correctly, you can run the tests provided in the `tests.py` file.

### Running Tests

    1. Ensure your virtual environment is activated.
    2. Run the tests:
        ```bash
        python manage.py test
        ```

    The tests will automatically discover and run all test cases defined in `tests.py` files across your project.

## API Endpoints

### List of API Endpoints

    - `GET /posts/` - List all posts
    - `GET /posts/<id>/` - Retrieve a specific post
    - `POST /posts/` - Create a new post
    - `PUT /posts/<id>/` - Update a specific post
    - `DELETE /posts/<id>/` - Delete a specific post
