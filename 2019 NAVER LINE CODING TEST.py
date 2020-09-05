# 2019 네이버 라인 코딩 테스트
# 출처: https://deepwelloper.tistory.com/118

# 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.

# 1. 코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
#    즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
# 2. 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 3. 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 4. 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.

# 표준 입력의 첫 줄에 코니의 위치 C와 브라운의 위치 B를 공백으로 구분하여 순서대로 읽는다.

# 브라운이 코니를 잡을 수 있는 최소시간 N초를 표준 출력한다. 단 브라운이 코니를 잡지 못한 경우에는 -1을 출력한다.

# 입력: 11 2
# 출력: 5
# 코니의 위치: 11 → 12 → 14 → 17 → 21 → 26
# 브라운의 위치: 2 → 3 → 6 → 12 → 13 → 26
# 브라운은 코니를 5초 만에 잡을 수 있다.

from collections import deque

def solution(cony, brown):
    loc = [False for _ in range(200001)]
    time = 0

    conyPos = cony

    dq = deque()
    dq.append((brown, 0))

    while dq:
        brownPos = dq.popleft()

        if time != brownPos[1]:
            time = brownPos[1]
            conyPos += time

            if conyPos > 200000:
                return(-1)

        if brownPos[0] == conyPos:
            return brownPos[1]

        if brownPos[0]-1 >= 0 and not loc[brownPos[0]-1]:
            dq.append((brownPos[0]-1, brownPos[1]+1))
            loc[brownPos[0]-1] = True
        if brownPos[0]+1 <= 200000 and not loc[brownPos[0]+1]:
            dq.append((brownPos[0]+1, brownPos[1]+1))
            loc[brownPos[0]+1] = True
        if brownPos[0]*2 <= 200000 and not loc[brownPos[0]*2]:
            dq.append((brownPos[0]*2, brownPos[1]+1))
            loc[brownPos[0]*2] = True

cony, brown = map(int, input().split())
print(solution(cony, brown))

# 반례로 C = 11, B = 1인 경우.
# 코드를 실행해 보면 1 → 2 → 4 → 5 → 10 → 20 → 40 → 39로 이동하여 7초 만에 잡는다.
# 하지만 실제로는 1 → 2 → 3 → 4 → 8 → 16 → 32로 이동하여 6초 만에도 잡을 수 있다.
# 이 코드에선 32 위치에 최초 5초에 도착하지만 6초에 도착하는 경우는 고려하지 않았기 때문에 최소 시간을 찾을 수 없게 된다.
# 아래의 풀이가 정답.

# def solve(conyPosition, brownPosition):
#     time = 0
#     visit = [[0]*2 for _ in range(200001)]
#     q = deque()
#     q.append((brownPosition, 0))
    
#     while 1:
#         conyPosition += time

#         if conyPosition > 200000:
#             return -1
#         if visit[conyPosition][time%2]:
#             return time
            
#         for i in range(0, len(q)):
#             current = q.popleft()
#             currentPosition = current[0]
#             newTime = (current[1]+1)%2
            
#             newPosition = currentPosition - 1
#             if newPosition >= 0 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))
                
#             newPosition = currentPosition + 1
#             if newPosition < 200001 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))
                
#             newPosition = currentPosition * 2
#             if newPosition < 200001 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))
                
#         time+=1

# 출처: https://deepwelloper.tistory.com/118