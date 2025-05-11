# Quiz API with Django REST Framework 🧠📝
## Overview🌟 
This project is a fully functional quiz API built with Django REST Framework (DRF) and Django. It allows users to create, manage, and validate quizzes, questions, and answer options. Additionally, the API includes user authentication features, tracks quiz attempts, and provides advanced functionalities such as performance analysis and feedback systems.

## Table of Contents 📑
- [Overview🌟](#overview)
- [Features⚡](#features)
- [Main Components](#main-components)
- [Installation💻](#installation)
- [Additional Applications🚀](#additional-applications)
- [Usage🔧](usage)
- [API Endpoints🌐](api-endpoints)
- [Testing🧪](testing)
- [Authors👨‍💻](authors)
   
## Features⚡

- **CRUD Functionality for Quizzes, Questions, and Answer Options**.
- **User Management: User authentication and tracking quiz attempts through the Profile and QuizAttempt models**.
- **Categories and Tags: Organize quizzes by categories and tags to make them easier to search**.
- **Quiz Validation: Validates answers and calculates scores upon quiz completion**.
- **Quiz Analysis: Tracks quiz performance (e.g., question success rates and overall quiz activity)**.
- **Planned Improvements**.
   - **Time-limited quizzes**.
   - **Support for different question types (multiple choice, true/false, short answers)**.
   - **Access control (public and private quizzes)**.
   - **Multimedia support (images, audio, or video in questions)**.
   - **Immediate feedback system, with explanations for correct answers**.

## Main Components

Our API will consist of these key components:

```
Quiz API
├── analytics
│   ├── models.py       
│   ├── serializers.p
│   ├── urls.py         
│   └── views.py     
├── config
├── quizzes
│   ├── models.py       
│   ├── serializers.p
│   ├── urls.py         
│   └── views.py 
├── users
│   ├── models.py       
│   ├── serializers.p
│   ├── urls.py         
│   └── views.py 
├── manage.py
└── requirements.txt
```

## Installation💻
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Django and Django REST Framework

### Steps
1. **Clone the repository:**
    
    ```
   git clone https://github.com/frank-froz/G5DesAplEmp
   cd Semana08/quiz_api
    ```

2. **Set up a virtual environment:**

    ```
    python3 -m venv venv      # On macOS/Linux
    python -m venv venv       # On Windows
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
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

7. **Access the API** at `http://127.0.0.1:8000/api/`.

## Additional Applications🚀

### User Management System:
1. User authentication and tracking of quiz attempts have been implemented using the Profile and QuizAttempt models. This now allows for effective management of users and their quiz attempts.

   1. **Conseguir Tokens User**
      - URL: `/api/token/`
      - Method: `POST`
      - Payload:
      
          ```json
          {
            "username": "", //nombre de usuario
            "password": ""
          }
          ```

1.  **Quiz Categories and Tags**:
    Add categories and tags to organize quizzes. This will make it easier for users to filter and search for quizzes based on specific topics or themes.
    

2.  **Quiz Analytics**:
    Implement analytics to track quiz performance, including question success rates and quiz activity (e.g., views, starts, completions).

## Usage 🔧
You can interact with the API via HTTP requests. Below are the main operations you can perform with the endpoints.

## API Endpoints 🌐

### *Quizz*

1. **Create a Quiz:**
     - **URL**: `/api/quizzes/` 
     - **Method**: `POST`
     - **Payload**:

       ```json
       {
         "title": "Python Basics",
         "description": "Test your knowledge of Python fundamentals"
       }
       ```

2. **Get All Quizz:**
     - **URL**: `/api/quizzes/` 
     - **Method**: `GET`
      

3. **Create a Question:**
   
      - **URL**: `/api/questions/`
      - **Method**: `POST`
      - **Payload**:

        ```json
          {
            "quiz": 1,  // ID of the quiz
            "text": "What is the output of print(1 + 2)?"
          }   
         ```

4. **Get all Question:**
   
      - **URL**: `/api/questions/`
      - **Method**: `GET`
        

5. **Create Choices:**

     - URL: `/api/choices/`
     - Method: `POST`
     - Payload:
       
       ```json
       {
         "question": 1,  // ID of the question
         "text": "3",
         "is_correct": true
       }
       ```

6. **Get all Choices:**

     - URL: `/api/choices/`
     - Method: `GET`
       

7. **Validate Quiz Answers:**

     - URL: `/api/quizzes/<quiz_id>/validate/`
     - Method: `POST`
     - Payload:
   
       ```json
       {
         "answers": [
           {"question_id": 1, "choice_id": 1}
         ]
       }
       ```
   
     - Response:
   
       ```json
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

### *Users*

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
   
10. **Update a Quiz Attempt:**
       
      - **URL**: `/api/quizattempts/{attempt_id}/`
      - **Method**: `PUT`
      - **Payload**:

        ```json
           {
             "score": 9,
             "max_score": 10
           }
           ```
   
11. **Delete a Quiz Attempt:**
   
      - **URL**: `/api/quizattempts/{attempt_id}/`
      - **Method**: `DELETE`


### *Categories and Tags*

1. **Create a Categories:**
     - **URL**: `/api/categories/` 
     - **Method**: `POST`
     - **Payload**:

       ```json
       {
         "title": "Python",
         "description": "Python's scripts"
       }
       ```

2. **Get All Categories:**
     - **URL**: `/api/categories/` 
     - **Method**: `GET`
      

3. **Create a Tags:**
   
      - **URL**: `/api/tags/`
      - **Method**: `POST`
      - **Payload**:

        ```json
          {
            "name": "hard"
          }   
         ```

4. **Get all Tags:**
   
      - **URL**: `/api/tags/`
      - **Method**: `GET`
  

### *Analytics*

1. **Get Question stat**
   
      - **URL**: `/api/analytics/question-stats`
      - **Method**: `GET`


2. **Get Question Activities**
   
      - **URL**: `/api/analytics/quiz-activities`
      - **Method**: `GET`
        


## Authors 👨‍💻

Castro Peñaloza, Hector Hanmer – hector.castro@tecsup.edu.pe

Huaytalla Rodriguez, Franklin Alvaro - franklin.huaytalla@tecsup.edu.pe

Ramos Huaman, Jeyson Kenedy – jeyson.ramos@tecsup.edu.pe

- Desarrollo de Aplicaciones Empresariales
- TECSUP - 2025-1

<p align="center">Made with ❤️ by the KaiMaki team</p>
