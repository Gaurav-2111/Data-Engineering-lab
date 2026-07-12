#config file
key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MWM0ZjkxMmQ0YzhhOGI1YmQyNzMzZGUwY2NjYjI0ZCIsIm5iZiI6MTc4MTg2NjI2Ny4yNzYsInN1YiI6IjZhMzUxZjFiNDk2YjY3YzlkMjUwZGRjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ltBil7T7gavR-QoyQSXr0w2JY-OLcCZIwS1ymUc291Q'
url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
headers = {
     "accept": "application/json",
     "Authorization": f"Bearer {key}"
     }
base_url = "https://api.themoviedb.org/3"
endpoint = "/discover/movie"
NON_RETRYABLE_STATUS_CODES = [400,401,403,404]
MAX_ATTEMPTS = 3

# database configration
host = 'localhost'
user = 'root'
password = '1234'
database = 'movies_db'
