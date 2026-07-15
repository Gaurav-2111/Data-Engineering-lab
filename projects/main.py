#main.py to run the pipeline
import time
from config import *
from datetime import date
from extract import extract_data
from transform import transform_data
from load import load_data
import logging 
from storage import save_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="pipeline.log",
    filemode="a"
)
all_data = []
# Starting time of pipeline
start_time = time.perf_counter()

logging.info("Pipeline started.")

for i in range(1,4):
  params = {
    "language": "en-US",
    "page": i
  }
  movies = extract_data(endpoint,params)
  if movies is None:
    logging.error("pipeline stopped because extraction failed.")
    raise RuntimeError("pipeline stopped because data extraction failed")

  logging.info(f"Extracted {len(movies['results'])} movies from page {i}")
  all_data.extend(movies['results'])
logging.info(f"Extracted {len(all_data)} movies in total")

# calling save data with the file_name
today = date.today()
file_name = today.strftime("%Y-%m-%d")
save_data(all_data,file_name)

#calling the transform function
clean_data = transform_data(all_data)

# calling the load function to load the clean data in the database
load_data(clean_data)

# ending time of pipeline
end_time = time.perf_counter()
execution_time = end_time - start_time
logging.info("---------pipeline succesfull-------------")
logging.info(f"seconds         : {execution_time:.2f} seconds")
logging.info(f"extracted Total : {len(all_data)} ")