
# 한 줄씩 실행 shift + Enter

import os

access_F = os.access('pickle', os.F_OK) #F_OK : 해당 path의 존재 여부 확인
print(access_F)

access2 = os.access('pickle' , os.W_OK | os.X_OK | os.R_OK) # W_OK : path의 쓰기 가능 여부 확인
print(access2)                                              # X_OK : path의 실행 가능 여부 확인
                                                            # R_OK : path의 읽기 가능 여부 확인

os.mkdir('test') # 디렉토리 생성

os.makedirs('test1/ex1/ex2/empty') #재귀적 디렉토리 생성

os.makedirs('test1/ex1/ex2/empty') # 같은 디렉토리 생성 시 오류 발생

os.remove('test.txt') # 파일 삭제

os.unlink('empty.txt') #파일 삭제   

os.rmdir('test') # 디렉토리 삭제

os.removedirs('test1/ex1/ex2/empty') # 재귀적 디렉토리 삭제

os.rename('empty.txt', 'ex.txt') # 파일, 디렉토리 이름 변경 및 이동

os.rename('empty\\empty1','empty\\empty3')

os.renames('ex.txt', 'test/test2.txt') #파일, 디렉토리 이름 변경 및 이동

os.stat('empty.txt') #path에 해당하는 정보를 얻어옵니다.
