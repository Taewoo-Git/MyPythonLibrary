# BOJ 문제
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.
# - push X: 정수 X를 큐에 넣는 연산이다.
# - pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# - size: 큐에 들어있는 정수의 개수를 출력한다.
# - empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# - front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# - back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 첫째 줄에 주어지는 명령의 수 N이 주어진다. (1 ≤ N ≤ 10,000)
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.

# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

import sys

myQueue = []
num = int(sys.stdin.readline())

for i in range(num):
    command = sys.stdin.readline()
    if "push" in command:
        myQueue.insert(0, int(command.split()[1]))
    elif "pop" in command:
        if len(myQueue) == 0:
            print(-1)
        else:
            print(myQueue.pop())
    elif "size" in command:
        print(len(myQueue))
    elif "empty" in command:
        if len(myQueue) == 0:
            print(1)
        else:
            print(0)
    elif "front" in command:
        if len(myQueue) == 0:
            print(-1)
        else:
            print(myQueue[-1])
    elif "back" in command:
        if len(myQueue) == 0:
            print(-1)
        else:
            print(myQueue[0])
