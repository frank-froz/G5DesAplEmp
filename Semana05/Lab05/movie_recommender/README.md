<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" width="100" alt="Django Logo">
</p>

<h1 align="center">🎬 Movie Recommender</h1>

<p align="center">
  A Django-based movie recommendation system with authentication, reviews, and dynamic UI.
</p>

---

## 🚀 Project Overview

This project is a **Movie Recommender System** built with Django 5.0. It allows users to:

- Explore a list of movies 🎥
- View movie details, posters, and genres 🧾
- Register, log in, and log out securely 🔐
- Leave ratings and reviews ⭐
- Add, edit, and delete movies (admin) 🛠️

---

## 🛠️ Features Implemented

- ✅ Movies app with list and detail views
- ✅ Beautiful movie grid view styled like Netflix
- ✅ Image handling with default fallback
- ✅ Django Admin site configured for models
- ✅ Authentication system (login, register, logout)
- ✅ Responsive layout with Bootstrap

---

## 🧪 Tech Stack

- **Backend:** Django 5.0
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (default)
- **Auth:** Django Authentication System

---

## 🧰 Setup Instructions


##### 1. Clone the repository

    git clone https://github.com/frank-froz/G5DesAplEmp.git
    
    cd G5DesAplEmp/Semana05/Lab05/movie_recommender
    
##### 2. (Optional) Create a virtual environment
    python -m venv venv
    source venv/bin/activate        # On Linux/Mac
    venv\Scripts\activate           # On Windows

##### 3. Install dependencies
	pip install -r requirements.txt

##### 4. Apply migrations
	python manage.py migrate

##### 5. Create superuser (optional for admin access)
	python manage.py createsuperuser

##### 6. Run the development server
	python manage.py runserver

## 📸 Screenshots 
<details> <summary>Movie List View (slide) </summary> 
	
![](https://github.com/frank-froz/G5DesAplEmp/blob/main/Semana05/Lab05/movie_recommender/static/screenshots/movie-list.png )

</details>

## 📌 To Do (Coming Soon)
- Movie search by title or genre
- User profile pages
- Personalized recommendations
- Like/Dislike system
- Follow other users

## 📜 License
MIT License – see the LICENSE file for details.
<p align="center">Made with ❤️ by the KaiMaki team</p>
