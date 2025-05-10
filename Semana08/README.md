# Quiz API with Django REST Framework 🧠📝
## Overview🌟 
This project is a fully functional Quiz API built with Django REST Framework (DRF). It allows users to create, manage, and validate quizzes, questions, and answer choices. The API is designed to handle quiz-related operations, including user authentication, quiz creation, question management, and answer validation.

## Table of Contents 📑
- [Overview🌟](#overview)
- [Features⚡](#features)
- [Main Components](#main-components)
- [Installation💻](#installation)
- [Usage🔧](usage)
- [API Endpoints🌐](api-endpoints)
- [Testing🧪](testings)
- [Next Steps🚀](next-steps)
- [Authors👨‍💻](authors)
   
## Features⚡
- Create, Read, Update, Delete (CRUD) functionality for quizzes, questions, and choices.
- User Management: Handle user authentication and track quiz attempts.
- Categories & Tags: Organize quizzes by categories and tags.
- Quiz Validation: Validate quiz answers and calculate scores.
- Quiz Analytics: Track quiz performance (e.g., question success rates and quiz activity).
- Feature Enhancements:
    - Timed quizzes
    - Multiple question types (multiple-choice, true/false, short answers)
    - Access control (public vs. private quizzes)
    - Media support (images, audio, or video in questions)
    - Feedback system (immediate feedback and explanations for correct answers)

### Main Components

Our API will consist of these key components:

```
Quiz API
├── Models
│   ├── Quiz (title, description, etc.)
│   ├── Question (belongs to a quiz, contains text)
│   └── Choice (belongs to a question, has text and correctness flag)
├── Serializers
│   ├── Basic serializers for individual models
│   └── Nested serializers for related data
├── Views
│   ├── ViewSets for CRUD operations
│   └── Custom view for answer validation
└── URLs for routing requests
```

## Installation💻
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Django and Django REST Framework

### Steps
1. **Clone the repository:**
    
    ```
    git clone <repository_url>
    cd quiz_api
    ```

2. **Set up a virtual environment:**

    ```
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3. **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

4. **Apply migrations to set up the database:**

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser to access the admin panel:**

    ```
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```
    python manage.py runserver
    ```

7. **Access the API** at http://127.0.0.1:8000/.

## Usage 🔧
You can interact with the API via HTTP requests. Below are the main operations you can perform with the endpoints.

## API Endpoints 🌐
1. **Create a Quiz:**
  - URL: /api/quizzes/
  - Method: POST
  - Payload:

    ```
    {
      "title": "Python Basics",
      "description": "Test your knowledge of Python fundamentals"
    }
    ```

2. **Create a Question:**

  - URL: /api/questions/
  - Method: POST
  - Payload:

    ```
    {
      "quiz": 1,  // ID of the quiz
      "text": "What is the output of print(1 + 2)?"
    }
    ```

3. **Create Choices:**

  - URL: /api/choices/
  - Method: POST
  - Payload:

    ```
    {
      "question": 1,  // ID of the question
      "text": "3",
      "is_correct": true
    }
    ```

4. **Validate Quiz Answers:**

  - URL: /api/quizzes/<quiz_id>/validate/
  - Method: POST
  - Payload:

    ```
    {
      "answers": [
        {"question_id": 1, "choice_id": 1}
      ]
    }
    ```

  - Response:

    ```
    {
      "quiz_id": 1,
      "score": "1/1",
      "percentage": 100,
      "results": [
        {
          "question_id": 1,
          "correct": true,
          "correct_choice": null
        }
      ]
    }
    ```

## Testing 🧪
You can test the API using Postman, cURL, or any HTTP client.

### Examples:
1. **Creating a quiz** using cURL:

    ```
    curl -X POST http://127.0.0.1:8000/api/quizzes/ \
      -H "Content-Type: application/json" \
      -d '{"title": "Python Basics", "description": "Test your knowledge of Python fundamentals"}'
    ```

2. **Creating a question**:
    
    ```
    curl -X POST http://127.0.0.1:8000/api/questions/ \
      -H "Content-Type: application/json" \
      -d '{"quiz": 1, "text": "What is the output of print(1 + 2)?"}'
    ```
  
3. **Creating choices**:
    
    ```
    curl -X POST http://127.0.0.1:8000/api/choices/ \
      -H "Content-Type: application/json" \
      -d '{"question": 1, "text": "3", "is_correct": true}'
    ```
      
4. **Validating quiz answers**:

    ```
    curl -X POST http://127.0.0.1:8000/api/quizzes/1/validate/ \
      -H "Content-Type: application/json" \
      -d '{"answers": [{"question_id": 1, "choice_id": 1}]}'
    ```

## Next Steps 🚀
### Additional Applications

1. **User Management System**:
    Implement user authentication and track quiz attempts using a Profile and QuizAttempt model. This will allow you to manage users and their quiz attempts.
2. **Install dependencies:**

    ```
    pip install djangorestframework-simplejwt
    ```
3. **configure dependencies:**
  # settings.py

  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
      ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
      ],
  }
4. **Conseguir Tokens User**
  - URL: /api/token/
  - Method: POST
  - Payload:

    ```
    {
      "username": "", //nombre de usuario
      "password": ""
    }
    ```
    ## API Endpoints 🌐
    1. **Get All Users:**
      - **URL**: `/api/users/`
      - **Method**: `GET`

    2. **Get a Specific User:**
      - **URL**: `/api/users/{user_id}/`
      - **Method**: `GET`

    3. **Create a Profile:**
      - **URL**: `/api/profiles/`
      - **Method**: `POST`
      - **Payload**:
        ```json
        {
          "user": 1,  // ID of the user
          "bio": "A short bio about the user",
          "avatar": "url_to_avatar_image"
        }
        ```

    4. **Get a Specific User Profile:**
      - **URL**: `/api/profiles/{profile_id}/`
      - **Method**: `GET`

    5. **Update a User Profile:**
      - **URL**: `/api/profiles/{profile_id}/`
      - **Method**: `PUT`
      - **Payload**:
        ```json
        {
          "bio": "Updated bio for the user",
          "avatar": "new_url_to_avatar_image"
        }
        ```

    6. **Get All Quiz Attempts:**
      - **URL**: `/api/quizattempts/`
      - **Method**: `GET`

    7. **Get Quiz Attempts by User:**
      - **URL**: `/api/quizattempts/?user={user_id}`
      - **Method**: `GET`

    8. **Create a Quiz Attempt:**
      - **URL**: `/api/quizattempts/`
      - **Method**: `POST`
      - **Payload**:
        ```json
        {
          "user": 1,  // ID of the user
          "quiz": 1,  // ID of the quiz
          "score": 8,
          "max_score": 10
        }
        ```

    9. **Update a Quiz Attempt:**
      - **URL**: `/api/quizattempts/{attempt_id}/`
      - **Method**: `PUT`
      - **Payload**:
        ```json
        {
          "score": 9,
          "max_score": 10
        }
        ```

    10. **Delete a Quiz Attempt:**
        - **URL**: `/api/quizattempts/{attempt_id}/`
        - **Method**: `DELETE`
 

2. **Quiz Categories and Tags**:
    Add categories and tags to organize quizzes. This will make it easier for users to filter and search for quizzes based on specific topics or themes.

3. **Quiz Analytics**:
    Implement analytics to track quiz performance, including question success rates and quiz activity (e.g., views, starts, completions).

### Feature Enhancements
- Timed Quizzes: Add a time limit for quizzes, track time taken by users, and auto-submit when time expires.
- Question Types: Implement multiple question types (e.g., multiple-choice, true/false, short answer).
- Access Control: Add public vs. private quizzes, password-protected quizzes, and quiz invitations via email.
- Media Support: Allow media (images, audio, video) in quiz questions, and support file uploads for answers.
- Feedback System: Provide immediate feedback after each question, including explanations for correct answers and personalized improvement suggestions.

### Learning Challenges
- JWT Authentication: Implement JWT for user authentication in the API
- Permission Classes: Add permission classes to control who can create or edit quizzes.
- Custom Filters: Add a custom filter to search quizzes by difficulty level or topic.
- API Throttling: Prevent abuse by adding throttling to your API.
- API Versioning: Implement versioning to support multiple versions of the API.

By completing this project, you've learned how to create a fully functional Quiz API with Django REST Framework. The additional features and enhancements will help you expand your skills further as you continue to develop your API.

## Authors 👨‍💻

Castro Peñaloza, Hector Hanmer – hector.castro@tecsup.edu.pe

Huaytalla Rodriguez, Franklin Alvaro - franklin.huaytalla@tecsup.edu.pe

Ramos Huaman, Jeyson Kenedy – jeyson.ramos@tecsup.edu.pe

- Desarrollo de Aplicaciones Empresariales
- TECSUP - 2025-1

<p align="center">Made with ❤️ by the KaiMaki team</p>
