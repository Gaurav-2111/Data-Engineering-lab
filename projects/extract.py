#extract file
import requests
import time
from config import *

def extract_data(endpoint , params):
  url = base_url + endpoint
  RETRY_DELAY = 3
  MAX_ATTEMPTS = 3
  # If any issue retry logic
  for attempts in range(1,MAX_ATTEMPTS + 1):
    try:
      response = requests.get(url,params=params,headers=headers)

      # Checking the status if 200 move forward
      if response.status_code == 200:
        data = response.json()
        print(f"Attempt : {attempts} succeeded")
        return data

      # if too many requests then we are going to wait
      if response.status_code == 429:
        print(f"attempt: {attempts}/{MAX_ATTEMPTS} , retrying after {RETRY_DELAY} seconds")
        time.sleep(RETRY_DELAY)

      # stoping the retry if status code are unimprovable
      if response.status_code in NON_RETRYABLE_STATUS_CODES:
        break


      # keeping notes where we needed retries
      print(
      f"Attempt {attempts}/{MAX_ATTEMPTS} failed "
      f"(Status: {response.status_code})."
      )

    #handling connection errors
    except requests.exceptions.ConnectionError:
      print(f"attempt: {attempts}/{MAX_ATTEMPTS} , failed due to connection error")

    #handling timeouts
    except requests.exceptions.Timeout:
      print(f"attempt: {attempts}/{MAX_ATTEMPTS} , failed due to connection timeouts")

    # return none if response code is not 200
  print(f"Extraction failed after {MAX_ATTEMPTS} attempts. "
          f"Endpoint :{endpoint}|"
          f"Parameter :{params}"
          )
  return None
