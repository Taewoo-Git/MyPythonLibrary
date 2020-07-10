# BOJ 문제
# 상근이는 꿈에서 길이가 L인 문자열을 외웠다.
# 꿈에서 깬 상근이는 이 문자열을 종이에 적던 중에 어떤 문자열은 두 번 이상 등장하는 것 같은 느낌을 받았다.
# 문자열이 주어졌을 때, 두 번 이상 등장한 부분 문자열 중 가장 길이가 긴 것을 찾는 프로그램을 작성하시오. (부분 문자열은 겹쳐서 등장할 수도 있다.)

# 첫째 줄에 L이 주어진다. (1 ≤ L ≤ 200,000)
# 다음 줄에는 길이가 L이면서 알파벳 소문자로 이루어진 문자열이 주어진다.

# 첫째 줄에 두 번 이상 등장하는 부분 문자열 중 길이가 가장 긴 것의 길이를 출력한다. 만약 그러한 문자열이 없을 때는 0을 출력한다.

import sys

def find(origin, target):
    origin_size = len(origin)
    target_size = len(target)
    origin_hash, target_hash, count = 0, 0, 0
    for i in range(origin_size - target_size):
        if i == 0:
            for j in range(target_size):
                origin_hash += ord(origin[j]) * (2**(target_size-(j+1)))
                target_hash += ord(target[j]) * (2**(target_size-(j+1)))
        else:
            origin_hash = 2 * (origin_hash - ord(origin[i-1]) * (2**(target_size-1))) + ord(origin[target_size+i-1])
        
        if(origin_hash == target_hash):
            check = True
            for j in range(target_size):
                if(origin[i+j] != target[j]):
                    check = False
                    break
            if check:
                count += 1
    return count

num = int(sys.stdin.readline())
string = sys.stdin.readline()
length = 0

for i in range(2, len(string)-1):
    for j in range(len(string)-i):
        findedCount = find(string, string[j:j+i])
        if findedCount >= 2:
            length = i

print(length)

# 라빈 카프 알고리즘으로 풀었으나 시간 초과...