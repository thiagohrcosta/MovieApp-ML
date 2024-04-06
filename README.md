# Movie APP 
![enter image description here](https://res.cloudinary.com/dloadb2bx/image/upload/v1712370449/Default_Generate_a_amazin_banner_for_a_Movie_APP_api_to_be_at_1_1_qbtvr4.jpg)
## Overview

The Movie APP is a project created to apply some of the concepts learned throughout the post-graduation degree at **[XP Educação](https://www.xpeducacao.com.br/)** in ***Artificial Intelligence with an emphasis on Machine Learning***. While this project is not integrated into the curriculum of the course, some of the concepts used were learned during the program.

## Objectives

The main objective was to create a Python API with Flask capable of consuming other external APIs, specifically from the website [TheMovieDB](https://www.themoviedb.org/). With this capability, our API can consume external data, storing it in its own MySQL database running in Docker, which contains a vast amount of movie information. Utilizing this data, our system can generate new movie recommendations for the user using Scikit-Learn.

## Features

-   Users can search for and add movies to their favorites.
-   If a movie entered by the user is not in our database, a new request is made by our API to TheMovieDB so that the indicated movie can be added immediately. This ensures that even if the desired movie is not initially in our database, it will be inserted based on the user's search.
-   Once the user has added some movies to their favorites, they can search for recommendations based on their choices. This is achieved using the cosine_similarity from [Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) to find the best results among the movies selected by the user.


## API endpoint

### Insomnia

For this first version, Insomnia was used to make the requests, but you can use any other API client that you prefer.

### User

1.  **Create User Account**
    -   Endpoint: `POST http://localhost:5000/user`
    -   Request Body:     `{
            "username": "John Doe",
            "password": "123456"
        }` 
        

### Categories (Movie Genres)

2.  **Fetch Categories**
    -   Endpoint: `POST http://localhost:5000/fetch_categories`
3.  **List Categories**
    -   Endpoint: `GET http://localhost:5000/categories`

### Movies

4.  **Fetch Movies**
    -   Endpoint: `POST http://localhost:5000/fetch_movies`
5.  **List Movies**
    -   Endpoint: `GET http://localhost:5000/movies`

### Favorites

6.  **Add Movie to Favorites**
    
    -   Endpoint: `POST http://localhost:5000/favorite`
    -   Request Body:  `{
            "user_id": 1,
            "movie_title": "The Expendables"
        }` 
        
7.  **Favorite Movies by User**
    
    -   Endpoint: `GET http://localhost:5000/favorite/user/1`
    -   Response: `{
            "favorites": [
                "Godzilla x Kong: The New Empire",
                "Dune",
                "Batman v Superman: Dawn of Justice",
                "Superman Returns",
                "Top Gun: Maverick",
                "First Blood",
                "The Expendables"
            ]
        }` 
        
8.  **Movie Recommendations**
    
    -   Endpoint: `GET http://localhost:5000/recommendations/user/1`

## Future Improvements

The ultimate goal is to create a project in a laid-back manner and practice Python development concepts. In this initial phase, the focus is not on creating code with Object-Oriented Programming (OOP), SOLID principles or other best practices, these aspects can be explored in other projects on my [GitHub](https://github.com/thiagohrcosta).

## How to Run

To run this application, ensure you have Docker and Python installed on your machine. Follow these steps:

1.  **Navigate to Project Folder:**
    
    -   Open your terminal/command prompt and navigate to the project folder.
2.  **Install Dependencies:**
    
    -   Before starting the application, install the required dependencies by running the following command:
                
        `pip install -r requirements.txt` 
        
3.  **Configure Python Environment:**
    
    -   After installing the dependencies, open a Python shell by running the following command:`flask shell` 
        
    -   Once in the Python shell, run the following commands to configure the database: `
        db.drop_all()
        db.create_all()
        db.session.commit()` 

3.  **Create .env File:**
    
    -   Create a `.env` file in the project folder and add the following line: `MOVIE_DATABASE_API_KEY="your_api_key"` 
        
    -   Replace `"your_api_key"` with your actual API key.
    -   **Remember to add .env at .gitignore file**.
        
4.  **Start the Application:**
    
    -   After configuring the Python environment, run the following command to start the application:  `python app.py` 
        
5.  **Start PostgreSQL Database:**
    
    -   Open a second terminal window and run the following command to start the PostgreSQL database using Docker:  `docker-compose up` 
        
6.  **Access the Application:**
    
    -   Once both the application and the database are running, you can access the project at `http://localhost:5000` in your web browser.

