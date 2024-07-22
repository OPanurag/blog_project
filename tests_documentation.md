### `tests.py` Documentation

The `tests.py` file includes basic tests for your models and API views.
Here's a breakdown of what each test does and how you can run them:

#### `PostModelTest` Class

    - Purpose: To test the `Post` model.
    - Tests Included:
      - `test_title_content`: Ensures the post title is correctly saved and retrieved.
      - `test_string_representation`: Ensures the string representation of the post is correct.
      - `test_get_absolute_url`: Ensures the `get_absolute_url` method generates the correct URL.

#### `CommentModelTest` Class

    - Purpose: To test the `Comment` model.
    - Tests Included:
      - `test_text_content`: Ensures the comment text is correctly saved and retrieved.
      - `test_string_representation`: Ensures the string representation of the comment is correct.

#### `PostAPITest` Class

    - Purpose: To test the API endpoints related to posts.
    - Tests Included:
      - `test_get_posts`: Ensures the `GET /posts/` endpoint returns all posts.
      - `test_get_single_post`: Ensures the `GET /posts/<id>/` endpoint returns a specific post.
      - `test_create_post`: Ensures the `POST /posts/` endpoint creates a new post.
      - `test_update_post`: Ensures the `PUT /posts/<id>/` endpoint updates an existing post.
      - `test_delete_post`: Ensures the `DELETE /posts/<id>/` endpoint deletes a specific post.

### How to Run Tests

    1. Make sure you have created and migrated your database.
    2. Create a superuser for accessing the admin site if necessary.
    3. Activate your virtual environment.
    4. Run the tests with the following command in terminal:
        python manage.py test
        

The command will output the test results, showing which tests passed and which failed.

By following this guide, you should be able to set up, run, and test your Django application effectively.
