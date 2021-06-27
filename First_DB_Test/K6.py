import sqlite3

conn = sqlite3.connect(r"k6_DB.db")

cur=conn.cursor()
sql="SELECT * FROM K6 where date between '{}' and '{}' and mode = {}".format('24/05/2021', '29/05/2021', 10)
print(sql)
cur.execute(sql)


names = [description[0] for description in cur.description]
all_result=cur.fetchall()
f = open('output.txt', 'w')
f.write("\t".join(names))
f.write("\n")
for row in all_result:
    f.write("\t".join([str(x) for x in row]))
    f.write("\n")
f.close()