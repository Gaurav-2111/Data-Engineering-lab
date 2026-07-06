#extract file
def extract_data(endpoint , params):

  url = base_url + endpoint
  # If any issue retry logic
  for attempts in range(1,MAX_ATTEMPTS + 1):

    response = requests.get(url,params=params,headers=headers)
    
    # Checking the status if 200 move forward
    if response.status_code == 200:
      data = response.json()
      print(f"Attempt : {attempts} succeeded")
      return data

    # if too many requests then we are going to wait
    if response.status_code == 429:
      time.sleep(5)

    # stoping the retry if status code are unimprovable
    if response.status_code in NON_RETRYABLE_STATUS_CODES:
      break
    

    # keeping notes where we needed retries
    print(
    f"Attempt {attempts}/{MAX_ATTEMPTS} failed "
    f"(Status: {response.status_code})."
    )

  # return none if response code is not 200
  print(f"Error: {response.status_code} |"
        f"Endpoint :{endpoint}|"
        f"Parameter :{params}"
        )
  return None
