# 어떤 수가 입력되면 천단위 구분 기호를 넣어 그 수를 다시 출력하는 프로그램을 작성하시오.

# 첫째 줄에 숫자의 길이 n이 입력 (1 ≤ n ≤ 200)
# 둘째 줄에 길이가 n인 숫자가 입력
# 천단위 구분기호 콤마를 넣어 출력

stack = []
a = int(input())
b = list(input())

for i in range(a):
    if(i % 3 == 0 and int(i/3) > 0):
        stack.append(',')
    stack.append(b.pop())

for i in range(len(stack)):
    print(stack.pop(), end='')
