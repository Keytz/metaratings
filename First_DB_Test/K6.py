import sqlite3

conn = sqlite3.connect(r"k6_DB.db")

cur=conn.cursor()
cur.execute("select * from k6;")

all_result=cur.fetchall()
# print(all_result)
print("<elements>")
for row in all_result:
    print("""    <element>
        <id>{}</id>
        <date>{}</date>
        <page>{}</page>
        <mode>{}</mode>
        <req_total>{}</req_total>
        <rec_min>{}</rec_min>
        <rec_avg>{}</rec_avg>
        <rec_max>{}</rec_max>
        <req_0_220>{}</req_0_220>
        <req_220_400>{}</req_220_400>
        <req_400_600>{}</req_400_600>
        <req_600_800>{}</req_600_800>
        <rec_800_1000>{}</rec_800_1000>
        <req_1000>{}</req_1000>
    </element>""".format(row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13] )
          )
print("</elements>")