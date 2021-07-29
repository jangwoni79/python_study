# csv 파일 데이터 모두 삭제하고 쓰기사용 예제

import csv

f = open('csv\ex_write_2.csv','w', encoding='utf-8-sig', newline='')
wf = csv.writer(f)

wf.writerow(['test3','test4'])
wf.writerow(['D',4])
wf.writerow(['E',5])

f.close()