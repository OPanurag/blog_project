Overview

    This document provides an overview of the test cases implemented for the Django blog project. 
    The tests cover model validations, view logic, and API endpoints to ensure the application 
    behaves as expected.

Tests Included

    PostUpdateDeleteTest
    
        This test case verifies the functionality of updating and deleting posts, 
        as well as ensuring users cannot modify or delete posts they do not own.
    
        1. setUp:
    
            Creates two users (testuser and otheruser) and logs in as testuser.
            Creates a post authored by testuser.
    
        2. test_update_post:
    
            Tests the ability to update a post's title and content.
            Verifies the post is updated correctly and the user is 
            redirected to the post detail page.
    
        3. test_delete_post:
    
            Tests the ability to delete a post.
            Verifies the post is deleted and the user is redirected 
            to the home page.
    
        4. test_cannot_update_other_users_post:
    
            Verifies otheruser cannot update testuser's post.
            Checks the response status code and ensures the post 
            remains unchanged.
    
        5. test_cannot_delete_other_users_post:
    
            Verifies otheruser cannot delete testuser's post.
            Checks the response status code and ensures the post 
            is not deleted.
    
    PostModelTest
    
        This test case ensures the Post model works as expected.
    
        1. setUpTestData:
    
            Creates a user and a post.
    
        2. test_title_content:
    
            Verifies the title and content of the post.
    
        3. test_string_representation:
    
            Checks the string representation of the post.
    
        4. test_get_absolute_url:
    
            Verifies the get_absolute_url method returns the 
            correct URL for the post.
    
    CommentModelTest
    
        This test case ensures the Comment model works as expected.
    
        1. setUpTestData:
    
            Creates a user, a post, and a comment on the post.
    
        2. test_text_content:
    
            Verifies the text content of the comment.
    
        3. test_string_representation:
    
            Checks the string representation of the comment.
    
    PostAPITest
    
        This test case verifies the API endpoints for managing posts.
    
        1. setUpTestData:
    
            Creates a user and a post.
    
        2. setUp:
    
            Logs in as the created user.
    
        3. test_get_posts:
    
            Verifies the endpoint to get a list of posts.
            Checks the response status code and content.
    
        4. test_get_single_post:
    
            Verifies the endpoint to get a single post.
            Checks the response status code and content.
    
        5. test_create_post:
    
            Verifies the endpoint to create a new post.
            Checks the response status code and content.
    
        6. test_update_post:
    
            Verifies the endpoint to update an existing post.
            Checks the response status code and updated content.
    
        7. test_delete_post:
    
            Verifies the endpoint to delete a post.
            Checks the response status code and ensures the post is deleted.
    
        8. Running the Tests
    
            To run the tests, use the following command:
                "python manage.py test"
    
    This will execute all the test cases and provide a summary of the results.

Conclusion

    The test cases provided cover a range of scenarios to ensure the 
    integrity and reliability of the Django blog project. 
    Regularly running these tests will help maintain the application's 
    quality and identify potential issues early in the development process.
