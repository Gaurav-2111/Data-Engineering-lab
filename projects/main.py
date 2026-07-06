#main.py to run the pipeline
all_data = []
for i in range(1,4):
  params = {
    "language": "en-US",
    "page": i
  }
  movies = extract_data(endpoint,params)
  if movies is None:
    raise RuntimeError("pipeline stopped because data extraction failed")

  all_data.extend(movies['results'])

# calling save data with the file_name
today = date.today()
file_name = today.strftime("%Y-%m-%d")
save_data(all_data,file_name)

#calling the transform function
transform_data(all_data)

