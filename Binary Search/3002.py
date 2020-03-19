# 주현이 엄마는 주현이를 영재로 키우기 위해 매일 혹독한 기억력 테스트를 하고 있다.
# n개의 숫자를 먼저 말해주고, m개의 질문을 하면서 그 숫자를 몇 번째로 불렀는지 테스트한다.
# 이번 테스트가 어려울 것을 예상하여 n개의 데이터를 부를 때 오름차순으로 부른다. (단, 질문은 오름차순으로 묻지 않는다.)
# 이 테스트를 통과할 경우 주현이는 최신 장난감 "또봇 W 쉴드온"을 받을 수 있다.
# 주현이를 도와 줄수 있는 프로그램을 작성하시오.

# 첫째 줄에 n이 입력 (1 ≤ n ≤ 1,000,000)
# 둘째 줄에 n개의 서로 다른 숫자가 공백으로 구분되어 오름차순으로 입력 (데이터 값의 범위 : 1 ~ 100,000,000)
# 셋째 줄에 질문의 수 m이 입력 (1 ≤ m ≤ 100,000)
# 넷째 줄에 m개의 질문이 공백으로 구분되어 입력
# m개의 질문에 대해 그 숫자가 있었으면 그 숫자의 위치를 출력, 없었으면 -1을 차례대로 출력

a = int(input())
b = list(map(int, input().split()))
b.sort()

c = int(input())
d = list(map(int, input().split()))

mid = 0
left = 0
right = a - 1

for i in d:
    while left <= right:
        mid = int((left + right) / 2)

        if(b[mid] < i):
            left = mid + 1
        elif(b[mid] > i):
            right = mid - 1
        else:
            break

    if(b[mid] == i):
        print(mid+1, end=" ")
    else:
        print(-1, end=" ")
    
    left = 0
    right = a - 1
