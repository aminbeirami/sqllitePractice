# Sqlite Practice with Python
this project reads two pile files, u.item and u.data, clean their records and store them in a sqlite database and at the end
run a query between the stored data.

#u.item
this file contains 100,000 records about the ratings (form 1 star to 5 star) which the users have given to different movies

#u.data
this file includes the name, id and address of the movies on IMDB

#instructions:
to run the code, 
1. run the importData.py file. an sqlite database with two tables will be created. one table to store the movie details, another to store the ratings
2. type this command : > sqlite3 movieRating.db
3. in the sqlite3 interface type: > .read mostRated.sql
