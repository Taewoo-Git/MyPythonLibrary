# BOJ 문제
# 루트 없는 트리가 주어진다.
# 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

import sys
input = sys.stdin.readline

n = int(input())

tree = { i: set() for i in range(1, n+ 1 ) }
parents = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    n, m = map(int, input().split())
    tree[n] = tree[n] | set([m])
    tree[m] = tree[m] | set([n])

def dfs(tree, root, parents):
    stack = [root]
    while stack:
        n = stack.pop()
        stack += tree[n] - set(parents)
        for i in tree[n]:
            tree[i] = tree[i] - set([n])
            parents[i] = n
    
    for j in range(2, len(parents)):
        print(parents[j])

dfs(tree, 1, parents)

# 시간 초과...