# BOJ 문제
# 트리(tree)는 사이클이 없는 무방향 그래프이다.
# 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다.
# 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다.
# 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.

# 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 
# 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오.

# 파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다.
# 둘째 줄부터 n번째 줄까지 각 간선에 대한 정보가 들어온다.
# 간선에 대한 정보는 세 개의 정수로 이루어져 있다.
# 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다.
# 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다.
# 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

# 첫째 줄에 트리의 지름을 출력한다.

node = int(input())
tree_info = [[] for _ in range(node + 1)]

for _ in range(node - 1):
    parent, child, length = map(int, input().split())
    tree_info[parent].append((child, length))

#BFS함수로 정렬하기
def bfs(graph_list, start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        visited.append(node)
        for child in graph_list[node]:
            queue.append(child[0])
            
    return visited

#정렬에 쓸 리스트 생성
bfs_node = bfs(tree_info, 1)
max_node = [0 for _ in range(node + 1)]
diameter = [[0] for _ in range(node + 1)]
max_diameter = [0 for _ in range(node + 1)]

#최하단의 노드부터 일방향 최댓값, 지름 최댓값 추출
while bfs_node:
    temp = bfs_node.pop()
    
    for child in tree_info[temp]:
        try:
            child_length = max_node[child[0]] + child[1]
        except:
            child_length = child[1]
        diameter[temp].append(child_length)
        max_node[temp] = max(diameter[temp])
        
    max_diameter[temp] += max(diameter[temp])
    diameter[temp].remove(max(diameter[temp]))
    try:
        max_diameter[temp] += max(diameter[temp])
    except:
        pass

#추출한 지름 값들 중 최댓값 출력
print(max(max_diameter))

# 출처: https://claude-u.tistory.com/194

# 작성자의 풀이
# 1) BFS로 최상단(1) 부터 최하단 까지 정렬
# 2) 정렬된 bfs_node함수의 끝부터 pop하기
# 3) 최하단에서 각 node에 도달하는 단방향 값들 산출(diameter)
# 4) 최하단에서 각 node에 도달하는 단방향 최댓값 산출(max_node)
# 5) 각 node의 지름 최댓값 산출(max_diameter)
# 6) 지름 값 중 최댓값 출력(max(max_diameter))