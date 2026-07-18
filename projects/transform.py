#transform data
import logging

def transform_data(all_data):
  logging.info("------Starting data transformation process------")
  clean_data = []
  total_movies = 0
  invalid_movies = 0
  valid_movies = 0
  for movie in all_data:
      
      #counting total number of movies processed
      total_movies += 1
      
      # data validation checks to ensure that the data is clean and valid before loading it into the database
      if movie['id'] is None or movie['title'] is None:
          logging.warning(f"movie with id {movie['id']} has missing values and will be skipped")
          invalid_movies += 1
          continue
      
      # popularity and vote_average and vote_count should be non-negative
      if movie['popularity'] < 0:
          logging.warning(f"movie with id {movie['id']} has negative popularity and will be skipped")
          invalid_movies += 1
          continue
      
      # rating are between 0 and 10
      if not (0 <= movie["vote_average"] <= 10):
          logging.warning(f"movie with id {movie['id']} has invalid vote_average and will be skipped")
          invalid_movies += 1
          continue
      
      if movie['vote_count'] < 0:
          logging.warning(f"movie with id {movie['id']} has negative vote_count and will be skipped")
          invalid_movies += 1
          continue
      
      valid_movies += 1
      
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
  logging.info(f"Total records received : {total_movies}")
  logging.info(f"Valid records          : {valid_movies}")
  logging.info(f"Invalid records        : {invalid_movies}")
  logging.info("------Data transformation completed------")
  return clean_data


