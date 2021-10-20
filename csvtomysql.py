import scipy.io
import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',
                       db='daesogal', charset='utf8')

curs = conn.cursor()
conn.commit()
f = open('insert.csv', 'r')
csvReader = csv.reader(f)

i = 0
for row in csvReader:
    if i == 0:
        i = i+1
        continue
    sql = """INSERT INTO cert
    (cert_id,     reg_time,     update_time,     created_by,     modified_by,
     cert_gubun,     cert_name,     cert_part,     city,     take_age,
     take_month,     take_number,     take_year,    gender)
    VALUES
    (%s,  %s,   %s,   %s,    %s,
     %s,  %s,   %s,   %s,    %s,
     %s,  %s,   %s,   %s)"""
    curs.execute(sql, ( i , "20211019", "200330", 'python', 'python',
                       row[5], row[7], row[6], row[2], row[3],
                       row[1], row[8], row[0], row[4]))
    i = i+1
conn.commit()
f.close()
conn.close()