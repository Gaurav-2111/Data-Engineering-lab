#load data
import mysql.connector
from database import get_connection

def load_data(clean_data):

  connection = get_connection()
  
  # cursor is going to connect our python with mysql
  cursor = connection.cursor()

  try:
    create_table_query = """CREATE TABLE IF NOT EXISTS movies (
        id INT PRIMARY KEY,
        title VARCHAR(200) NOT NULL,
        release_date date,
        popularity FLOAT NOT NULL,
        vote_average FLOAT NOT NULL,
        vote_count INT NOT NULL,
        original_language VARCHAR(10) NOT NULL,
        adult BOOLEAN NOT NULL,
        overview TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )"""

    # this is so that our table is created
    cursor.execute(create_table_query)


    insert_query = """insert ignore into movies (id,title,release_date,popularity,vote_average,vote_count,original_language,adult,overview)
      values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    # creating a list because executemany() uses combined data as it process data in a batch
    batch_data = []

    for movie in clean_data:


        values = (
              movie["id"],
              movie["title"],
              movie["release_date"],
              movie["popularity"],
              movie["vote_average"],
              movie["vote_count"],
              movie["original_language"],
              movie["adult"],
              movie["overview"]
          )
        # appending data of each row as a tuple inside a list
        # [(row 1),(row 2),(row 3)] every tuple is going to fill the place of those place holders we created in insert_query
        batch_data.append(values)

    # executemany to send all data at once
    cursor.executemany(insert_query,batch_data)
    connection.commit()

  # if there was a error in storing data in database
  except Exception as e:
    print(f"database transaction failed so rolling back changes , error : {e}")
    connection.rollback()

  # it does not matter what happened we always close are connectoin
  finally:
    cursor.close()
    connection.close()

