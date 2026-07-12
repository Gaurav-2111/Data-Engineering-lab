#data storage
import json
def save_data(all_data,file_name):
  with open(f'movies_{file_name}.json','w') as f:
    json.dump(all_data,f,indent=4)