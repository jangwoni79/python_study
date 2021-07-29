# 예시1

import pickle
test = ['A', 'B', 'C']

# 피클링
with open ("data.p","wb") as f1:
		pickle.dump(test,f1)

# 언피클링
with open ("data.p","rb") as f2:
		data = pickle.load(f2)
print(data)
