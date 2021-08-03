import argparse

# 파서 만들기
parser = argparse.ArgumentParser(description = '테스트')

# 인자 추가하기
parser.add_argument('--a', required=True , action='append', help='입력1')
parser.add_argument('--b', required=False, default='dev', help='입력2')
parser.add_argument('--zoo1', type=str, nargs=2, help='입력3')

# 인자 파싱하기
args = parser.parse_args()

print(args.a)
print(args.b)