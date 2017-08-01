import sqlite3
 
con =sqlite3.connect("/movieRating.db")

print "opened the database successfully"
cur = con.cursor()
cur.execute("CREATE TABLE ratings(userId text,movieId text,rating int,rateTime text);")
cur.execute("CREATE TABLE movies(id text, name text);")
   
def loadMovieDetails():
    with open ("/u.data") as f:
        for line in f:
            fields = line.split()
            fields[2] = int(fields[2])
            cur.execute('INSERT INTO ratings(userId,movieId,rating,rateTime) values (?,?,?,?)', fields)
        con.commit()

def loadMovieNames():
    with open("/u.item") as p:
        for line2 in p:
            temp = line2.split("|")
            fields = [temp[0],temp[1].decode('utf8', 'ignore')]
            cur.execute('INSERT INTO movies(id, name) values (?,?)', fields)
        con.commit()
           

loadMovieDetails()

loadMovieNames()

