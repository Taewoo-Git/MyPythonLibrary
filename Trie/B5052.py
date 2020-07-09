# BOJ 문제
# 전화번호 목록이 주어진다. 
# 이때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램을 작성하시오.
# 전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

# 예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자.
# 긴급전화: 911
# 상근: 97 625 999
# 선영: 91 12 54 26
# 이 경우에 선영이에게 전화를 걸 수 있는 방법이 없다.
# 전화기를 들고 선영이 번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다.
# 따라서, 이 목록은 일관성이 없는 목록이다. 

# 첫째 줄에 테스트 케이스의 개수 t가 주어진다. (1 ≤ t ≤ 50)
# 각 테스트 케이스의 첫째 줄에는 전화번호의 수 n이 주어진다. (1 ≤ n ≤ 10000)
# 다음 n개의 줄에는 목록에 포함되어 있는 전화번호가 하나씩 주어진다.
# 전화번호의 길이는 길어야 10자리이며, 목록에 있는 두 전화번호가 같은 경우는 없다.

# 각 테스트 케이스에 대해서, 일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력한다.

import sys
 
class Node:
    def __init__(self,data):
        self.data=data
        self.child=[None for _ in range(10)]
        self.check=False
 
class Trie:
    def __init__(self):
        self.root=Node('')
 
    def insert(self,phone):
        tmp=self.root
        for i in phone:
            if tmp.child[i] != None:    # 비어있지 않다면
                tmp=tmp.child[i]
            else:
                new=Node(i)
                tmp.child[i]=new
                tmp=new            
        tmp.check=True
        
    def consistency(self,phone):
        tmp=self.root
        for i in range(len(phone)):
            if tmp.check:               # 다른문자열을 포함하고 있다면
                return False
            tmp=tmp.child[phone[i]]
        return True

for _ in range(int(input())):
    n=int(input())
    phone_list = []
    trie=Trie()
    for _ in range(n):
        phone=list(map(int,sys.stdin.readline().rstrip()))
        trie.insert(phone)
        phone_list.append(phone)
    result=True
    for p in phone_list:
        result*=trie.consistency(p)
 
    if result:
        print('YES')
    else:
        print('NO')

# 출처: https://developmentdiary.tistory.com/461?category=876569