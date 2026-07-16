#transform data
import logging


def transform_data(all_data):
  logging.info("------Starting data transformation process------")
  clean_data = []
  for movie in all_data:
      
      # data validation checks to ensure that the data is clean and valid before loading it into the database
      if movie['id'] is None or movie['title'] is None:
          logging.warning(f"movie with id {movie['id']} has missing values and will be skipped")
          continue
      
      # popularity and vote_average and vote_count should be non-negative
      if movie['popularity'] < 0:
          logging.warning(f"movie with id {movie['id']} has negative popularity and will be skipped")
          continue
      
      # rating are between 0 and 10
      if not (0 <= movie["vote_average"] <= 10):
          logging.warning(f"movie with id {movie['id']} has invalid vote_average and will be skipped")
          continue
      
      if movie['vote_count'] < 0:
          logging.warning(f"movie with id {movie['id']} has negative vote_count and will be skipped")
          continue
      
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
  logging.info(f"transformed {len(clean_data)} rows of data")
  return clean_data
