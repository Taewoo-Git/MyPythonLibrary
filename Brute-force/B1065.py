# BOJ 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

# 첫째 줄에 1,000보다 작거나 같은 자연수 N을 입력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력

import sys

num = int(input())
count = 0

def hansu(n):
    global count
    if n > num:
        return
    else:
        if n <= 99 :
            count += 1
        else :     
            nums = list(map(int, str(n)))
            if nums[0] - nums[1] == nums[1] - nums[2] :
                count += 1
        hansu(n+1)

sys.setrecursionlimit(1100)
hansu(1)
print(count)