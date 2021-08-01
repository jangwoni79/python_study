import argparse

parser = argparse.ArgumentParser(description='사용법 테스트')

parser.add_argument('--target', required=True , help='어느 것을 요구하냐')
parser.add_argument('--env', required=False, default='dev', help='실행환경은 뭐냐')

args = parser.parse_args()

print(args.target)
print(args.env)