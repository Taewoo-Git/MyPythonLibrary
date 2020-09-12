# BOJ 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1≤M≤100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
search_list = list(map(int, input().split()))

num_list.sort()

def search(num):
    left = 0
    right = len(num_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == i:
            return 1
        elif num_list[mid] > i:
            right = mid - 1
        elif num_list[mid] < i:
            left = mid + 1
    
    return 0

for i in search_list:
    print(search(i))