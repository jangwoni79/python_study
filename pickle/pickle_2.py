# 예시2

import pickle
ID = 'mobigen'
PW = '1234'

# 피클링
with open ("data.b","wb") as wf:
	pickle.dump(ID, wf)
	pickle.dump(PW, wf)

# 언피클링
with open ("data.b","rb") as rf:
	ID = pickle.load(rf)
	PW = pickle.load(rf)
	print(ID)
	print(PW)