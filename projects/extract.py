import requests
key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MWM0ZjkxMmQ0YzhhOGI1YmQyNzMzZGUwY2NjYjI0ZCIsIm5iZiI6MTc4MTg2NjI2Ny4yNzYsInN1YiI6IjZhMzUxZjFiNDk2YjY3YzlkMjUwZGRjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ltBil7T7gavR-QoyQSXr0w2JY-OLcCZIwS1ymUc291Q'
headers = {
     "accept": "application/json",
     "Authorization": f"Bearer {key}"
     }
base_url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
# base_url = "https://api.themoviedb.org/3/discover/movie?api_key=51c4f912d4c8a8b5bd2733de0cccb24d"
response = requests.get(base_url,headers=headers)
print(response.status_code)
data = response.json()
print(type(data))
print(data.keys())
