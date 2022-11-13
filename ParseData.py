from ast import keyword
import csv
import json

def parseGame():
    games = []
    with open('data/steam_top_100.csv') as csvfile:
        game_reader = csv.reader(csvfile)
        for row in game_reader:
            if not row[0].isnumeric():
                continue
            name = row[1]
            games.append(name)
            tags = row[7]
            tags = tags.split(':')

    rows = []
    with open('data/steam_games.csv') as csvfile:
        game_reader = csv.reader(csvfile)
        for row in game_reader:
            name = row[2]
            if not name in games:
                continue
            tags = row[9]
            genre = row[13]
            game_desc = row[14]
            rows.append([name, tags, genre, game_desc])

    # field names 
    fields = ['Name', 'Tag', 'Genre', 'Desc'] 
    with open('data/clean_steam_games.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(rows)

def parseMovie():
    rows = []
    with open('data/tmdb_5000_movies.csv') as csvfile:
        movie_reader = csv.reader(csvfile)
        for row in movie_reader:
            if row[0] == 'budget':
                continue
            title = row[6]
            keywords = []
            keyword_dict = row[4]
            keyword_dict = json.loads(keyword_dict)
            for dict in keyword_dict:
                keywords.append(dict['name'])
            genres = []
            genre_dict = row[1]
            genre_dict = json.loads(genre_dict)
            for dict in genre_dict:
                genres.append(dict['name'])
            desc = row[7]
            rows.append([title, keywords, genres, desc])

    # field names 
    fields = ['Title', 'Keywords', 'Genres', 'Desc'] 
    with open('data/clean_movies.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(rows)

if __name__ == "__main__":
    # parseGame()
    parseMovie()
