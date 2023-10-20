import csv
import random

f = open('data/raw_data.csv','r')
rdr = csv.reader(f)

rdr = list(rdr)
rdr[0].append("co2")
rdr[0].append("organic")
rdr[0].append("score")
for i in range(1, len(rdr)):
    rdr[i].append(random.randint(5, 20))
    rdr[i].append(random.randint(0, 4))
    rdr[i].append(0)
f.close()


f = open('data/processed_data.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerows(rdr)

f.close()

