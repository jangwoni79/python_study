# csv 읽기 사용 예제

import csv

tf = open('csv\ex_read_1.csv','r', encoding='utf-8-sig', newline='')
rf = csv.reader(tf)

for line in rf:
	print(line)

tf.close()