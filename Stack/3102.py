# STL stack 명령어
# n개의 명령어가 입력되면, 순서대로 동작하는 프로그램을 작성하시오.

# push( x ) : x를 스택에 넣는다.(x는 정수) 괄호와 x사이에 공백이 반드시 존재한다.
# top() : 스택의 top 포인터가 가리키는 값을 출력한다.  만약 원소가 없다면 -1을 출력한다.
# pop() : 스택의 마지막에 들어온 원소를 삭제한다.
# size() : 스택안의 원소 개수를 출력한다.
# empty() : 스택이 비어있으면 true, 비어 있지 않으면 false 를 출력한다.

# 첫째 줄에 n이 입력 (1 <= n <= 200)
# 둘째 줄 부터 각 줄에 하나씩 명령어 n개가 입력
# 명령어에 따라 동작결과를 순서대로 출력, push와 pop은 출력되는 결과가 없음에 유의

stack = []
command = []
a = int(input())

for i in range(a):
    b = input()
    command.append(b)

for i in command:
    if "push" in i:
        c = int(i[5:len(i)-1])
        stack.append(c)
    elif "pop" in i:
        if(len(stack) != 0):
            stack.pop()
    elif "top" in i:
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
    elif "empty" in i:
        if(len(stack) == 0):
            print("true")
        else:
            print("false")
    elif "size" in i:
        print(len(stack))
