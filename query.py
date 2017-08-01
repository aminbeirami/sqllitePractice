from collections import OrderedDict
import sqlite3 
con =sqlite3.connect("/MovieRating.db")
con2 =sqlite3.connect("/MovieNames.db")
cur = con.cursor()
cur2 = con2.cursor()
def initializeA():
    cur.execute("SELECT movieid,rating FROM ratings")
    for row in cur.fetchall():
        a.append(row)
    
def reduce_By_Key(ls): #Trimming the list based on Key
    d = OrderedDict()
    for key,sublist in ls:
        d.setdefault(key, []).extend(sublist)
    return list(d.items())

def findMax(old):
    NewList = list(map(lambda x: (x[0],len(x[1])), old))
    Maximum = max(NewList,key=lambda item:item[1])
    return Maximum

def returnName(ID):
    cur2.execute("SELECT FilmName FROM FimNames WHERE Filmid ="+ID)
    for row in cur2.fetchall():
        return row

a= [];
initializeA()
#print a
T= reduce_By_Key(a)
#for elements in T:
#   print elements
MaximumRate = findMax(T)
#print MaximumRate
Movie=returnName(MaximumRate[0])
print ("The Most Rated Movie has been "+Movie[0]+" with "+ str(MaximumRate[1]) + " number of ratings" )