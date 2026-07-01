all_data = []
for i in range(1,4):
  params = {
    "language": "en-US",
    "page": i
  }
  movies = extract_data(endpoint,params)
  all_data.extend(movies['results'])
