# CS410 CourseProject

## Overview
This project is a recommendation systems for movies based on a game. It takes the name of one game and recommend a list of movies related to that game. The recommendation systems is based on 2 aspects: 
relation of the descriptions bewteen movies and the game, and the genres of the game and the movies.

## How is this implemented
Datasets used to train this system: 
* Steam games: https://www.kaggle.com/datasets/trolukovich/steam-games-complete-dataset (data/steam_games.csv)
* Movies (tmdb top 5000): https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv (data/tmbd_5000_movies.csv)

Data cleaning (ParseData.py):
This file cleans and organized data into:
* Steam games: Name, Tags, Genres, Descriptions
* Movies: Title, Keywords, Genres, Descriptions

Recommendation system (Movie_Game_Recommender.ipynb):
The recommendation algorithm considers two factors of the relation between game and the movies: description, and genre.

Description of the games and the movies are encoded using symmetric SentenceTransformer with 'all-mpnet-base-v2' model. We used faiss for the inverted index search. 

Genre TBD


## How to use this
TBD

## Contributation
TBD