# ------------- WAVE 1 --------------------
#adding a comment in the code to commit :)
def create_movie(title, genre, rating):
    
    user_data = {
        "watched": [],
        "watchlist": []
        }

    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if None in new_movie.values():
        return None

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"] += [movie]
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] += [movie]
    return user_data

def watch_movie(user_data, title):
    watchlist_length = len(user_data['watchlist']) #1
    movie_index = None

    for i in range(watchlist_length):
        if user_data['watchlist'][i]['title'] == title:
            movie_index = i
    
    
    user_data['watched'].append(user_data['watchlist'][movie_index])
    del user_data['watchlist'][movie_index]
    
    return user_data






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

