import os

os.chdir('pickle')

chdir = os.getcwd() # 디렉토리 이동
print(chdir)

listdir = os.listdir() # 작업 디렉토리의 파일 목록
print(listdir)

os.chdir('..')
chdir2 = os.getcwd()
print(chdir2)