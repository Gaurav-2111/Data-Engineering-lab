#transform data
def transform_data(all_data):
  clean_data = []
  for movie in all_data:
      clean_data.append({
        "id":movie['id'],
        "title":movie['title'],
        "release_date":movie['release_date'],
        "popularity":movie['popularity'],
        "vote_average":movie['vote_average'],
        "vote_count":movie['vote_count'],
        "original_language":movie['original_language'],
        "adult":movie['adult'],
        "overview":movie['overview']
        })
