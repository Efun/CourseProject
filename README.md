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

Description of the games and the movies are encoded using symmetric SentenceTransformer with 'all-mpnet-base-v2' model. We used faiss IndexIDMap for the inverted index ranking. 

Movie that shares the same genres with the game is also rewarded in ranking. The score get's a factor of rewarding each time when genre matches.


## How to use this
Open Movie_Game_Recommender.ipynb and start from "Creating Inverted Index" section. Run the code to the end. 
Inference API is called 'recommend_movies_from_game'. It takes the name of the game and prints out top 10 recommended movies that's related to this game. 

There're also two examples given at the end of the notebook. 

### Example: PLAYERUNKNOWN'S BATTLEGROUNDS
Top recommended movies are "The World's End", 'Gamer', 'Pixels', 'Stay Alive', etc. Those movies are all survival movies and most of the movies involves shooting/action. They are aligned with the game content that players need to fight each other and survive to the last.

## Contributation
* Data cleaning + parsing: Zhekun Zhang, Micheal Xu
* Description recommendation system: Micheal Xu
* Genre rewarding mechnism: Zhekun Zhang
* Documentation: Zhekun Zhang
* Presentation: Ethan Ma