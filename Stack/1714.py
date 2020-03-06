# 어떤 수 n이 입력되면 그 수를 거꾸로 출력하는 프로그램을 작성하시오.

# 입력되는 수 n은 0이상의 정수
# 입력된 수를 거꾸로 출력

a = input()
stack = list(a)
for i in range(len(stack)):
    print(stack.pop(), end='')