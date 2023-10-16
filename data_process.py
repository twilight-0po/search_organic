import csv
import random

f = open('data.csv','r')
rdr = csv.reader(f)

rdr = list(rdr)
rdr[0].append("co2")
rdr[0].append("organic")
for i in range(1, len(rdr)):
    rdr[i].append(random.randint(5, 20))
    rdr[i].append(random.randint(0, 4))
f.close()


f = open('processed_data.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerows(rdr)

f.close()

