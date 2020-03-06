# 데이터의 개수가 n개가 들어오고, n개의 데이터를 거꾸로 출력하는 프로그램을 작성하시오.

# 첫째 줄에 데이터의 개수 n이 입력 (n <= 1,000)
# 둘째 줄에 공백을 기준으로 n개 데이터가 입력
# n개의 데이터를 입력의 역순으로 출력

a = int(input())
stack = input().split()

for i in range(a):
    print(stack.pop(), end=' ')