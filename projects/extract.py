def extract_data(endpoint , params):

  base_url = "https://api.themoviedb.org/3"
  url = base_url + endpoint
  response = requests.get(url,params=params,headers=headers)
  print(response.status_code)
  data = response.json()
  print(response.text)
  print(response.headers)
  return data