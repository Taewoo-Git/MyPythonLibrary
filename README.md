# MyPythonLibrary
Algorithm problem solving by python. <br/>

##### 문제 풀이 참고 <br/>
* CodeUp(https://www.codeup.kr/) <br/>
* Backjoon(https://www.acmicpc.net/)

<hr/>

### 스택(Stack)이란?

스택은 리스트의 한쪽 끝으로만 자료의 삽입, 삭제 작업이 이루어지는 자료구조. <br/>
스택은 가장 나중에 삽입된 자료가 가장 먼저 삭제되는 후입선출(LIFO)방식으로 자료를 처리.

##### Overflow
* 스택으로 할당받은 메모리 부분의 마지막 주소가 M번지라고 할 때, Top Pointer의 값이 M보다 커지면 <br/> 스택의 모든 기억장소가 꽉 채워져 있는 상태이므로 더 이상 자료를 삽입할 수 없어 Overflow를 발생.
##### Underflow
* Top Pointer가 주소 0을 가지고 있다면 스택에는 삭제할 자료가 없으므로 Underflow를 발생.  <br/> 즉, 스택에 기억되어 있는 자료를 삭제시킬 때는 제일 먼저 삭제할 자료가 있는지 없는지부터 확인.

<br/>
<pre>
pop(): 스택에서 가장 위에 있는 항목을 제거.
push(item): item 하나를 스택의 가장 윗 부분에 추가.
peek() 또는 top(): 스택의 가장 위에 있는 항목을 반환.
isEmpty(): 스택이 비어 있을 때에 true를 반환.
</pre>

<hr/>

### 완전 탐색(Brute-force)이란?
말 그대로 완전히 탐색, 답이 나올 때까지 샅샅이 찾는 방법. <br/>
컴퓨터의 순기능을 이용한 탐색 방법.  <br/>
즉, 계산이나 비교 그리고 탐색 등은 컴퓨터를 사용하여 빠르게 구하는 것이 가능. <br/>

* 장점: 답을 무조건 찾음. 
* 단점: 답을 찾는데 시간이 걸림.

완전 탐색을 구현하기 위한 대표적인 4가지 방법.
<pre>
1. for문 사용
2. 순열, 조합 사용
   순열(Permutation)이란, 서로 다른 n개의 원소에서 r개를 중복을 허용하지 않고 선택하여 순서대로 늘어 놓은 것. (nPr로 표기.)
   ex) [a, b, c, d]일 때, 2개를 뽑아서 일렬로 세우기.
       → ab, ac, ad, ba, bc, bd, ca, cb, cd, da, db, dc = 12가지
   조합(Combination)이란, 조합은 n개의 수 중에서 서로 다른 r개를 뽑아내어 집합을 만드는 방법. (nCr로 표기.)
   ex) [a, b, c, d]일 때, 2개씩 짝을 이뤄 집합 만들기.
       → ab, ac, ad, bc, bd, cd = 6가지
3. 재귀함수 사용
4. 비트마스크 사용
</pre>

for문과 재귀함수의 차이는 개인의 취향이나 문제의 유형에 따라 다르지만, 재귀함수를 사용해서 탐색하는 것을 선호. <br/>
이유는 비교해야 할 대상이 많아지면 비교대상만큼 for문을 써야하는 과정에서 가독성 저하.

<hr/>

### 이진 탐색(Binary Search)이란?
탐색 기법중에 하나로 원하는 탐색 범위를 두 부분으로 분할해서 찾는 방식. <br/>
전부를 탐색하는 탐색 속도에 비해 빠름. <br/>
이진 탐색을 하는 방법은 left , right , mid 값으로 탐색하는 것. <br/>
mid의 값은 (left + right)/2 으로 잡아주고 검색하고자 하는 값과 mid 값을 비교. <br/>

<pre>
1. 이진 탐색을 하고자 할 때 이미 정렬이 되어있어야 함.
2. left, right로 mid 값을 선택.
3. mid 값과 구하고자 하는 값을 비교.
4. mid 값보다 구하고자 하는 값이 높으면 left를 mid+1로 만들어주고 낮으면 right를 mid-1로 만들어 줌. 
5. left > right 가 될때까지 1~3번을 반복해서 구하고자 하는 값을 탐색.
</pre>

전체를 탐색하는 완전 탐색의 시간복잡도가 O(n)인 것에 비해 이진 탐색은 O(log(n))으로 적음.

<hr/>

### 해싱(Hashing)이란?
대부분의 탐색 방법들은 탐색 키를 저장된 키 값과 반복적으로 비교하면서 탐색을 원하는 항목에 접근. <br/>
반면 해싱은 키 값에 직접 산술적인 연산을 적용하여 항목이 저장되어 있는 테이블의 주소를 계산하여 항목에 접근. <br/>
이렇게 키 값의 연산에 의해 직접 접근이 가능한 구조를 해시 테이블(Hash Table)이라 부름. <br/>

해시 테이블(Hash Table)은 레코드를 한개 이상 보관할 수 있는 버킷(Bucket)들로 구성된 기억 공간으로 <br/>
보조기억장치에 구성할 수도 있고, 주기억장치에 구성할 수도 있음.
<pre>
버킷(Bucket): 하나의 주소를 갖는 파일의 한 구역을 의미하며, 버킷의 크기는 같은 주소에 포함될 수 있는 레코드 수를 의미.
슬롯(Slot): 한 개의 레코드를 저장할 수 있는 공간으로 n개의 슬롯이 모여 하나의 버킷을 형성.
Collision(충돌): 서로 다른 두 개 이상의 레코드가 같은 주소를 갖는 현상.
Synonym: 충돌로 인해 같은 Home Address를 갖는 레코드들의 집합.
Overflow: 계산된 Home Address의 Bucket 내에 저장할 기억 공간이 없는 상태로
          Bucket을 구성하는 Slot이 여러 개일 때 Collision은 발생해도 Overflow는 발생하지 않을 수 있음.
</pre>

키들의 비교에 의한 탐색 방법은 정렬이 안 되어 있다면 O(n)이고, 정렬이 되어 있다면 O(log(n)). <br/>
정렬되어 있는 경우의 시간 복잡도가 O(log(n))인 건 이진 탐색의 시간 복잡도를 생각하면 쉬움. <br/>

해싱은 이론적으로 O(1)의 시간 안에 탐색을 끝마칠 수 있으므로 <br/>
위와 같은 시간 복잡도 보다 더욱 빠른 탐색을 필요로 할 때 사용. <br/>

해싱은 다음과 같이 크게 세 가지로 구분.
<pre>
1. 완전 해싱(Perfect Hashing)
   완전 해싱은 나중에 좋은 해싱 기법으로 언급될 simple uniform 해싱을 의미.
   즉 서로 다른 키(key)값이 해싱에 의해 주소값을 할당받을 때, 주소값이 절대로 겹치지 않는 이상적인 해싱을 의미.
   물론 이런 방식은 일대일대응 이외에는 존재하지 않는 방식으로 이상적인 것.
2. 정형 해싱(Conventional Hashing)
   데이터 개수를 이미 알고 있어서, 데이터들이 저장될 주소 범위를 미리 데이터 개수만큼 지정해 두는 방식을 의미.
   즉, 필요한 메모리의 크기는 미리 측정되고 미리 할당받아야 함.
3. 동적 해싱(Dynamic Hashing)
   정형 해싱의 문제점은 데이터를 입력하기 이전에 데이터 개수에 대한 정보가 있어서 메모리를 미리 할당받아야 한다는 점.
   일반적으로 시간이 지남에 따라서 데이터의 양의 증가하게 되므로 잘못된 측정으로 데이터가 메모리의 범위를 넘게 되면,
   더 큰 메모리 크기를 잡고 다시 해싱을 해야 하는 시간적, 자원적 낭비가 일어나게 됨.
   동적 해싱은 이러한 데이터의 증감에 적응하기 위해서 나타난 것으로, 동적으로 메모리의 크기를 변화시키는 해싱 기법을 의미.
</pre>

즉, 해싱은 가변 크기의 입력값에서 고정된 크기의 출력값을 생성해 내는 과정을 의미하며, <br/>
해시 함수(Hash Function)라 알려진 수학적 공식을 따라 진행. <br/>

여기서 해시 함수(Hash Function)란, 레코드 키에 대한 해시 테이블(Hash Table)내의 홈 주소(Home Address)를 <br/>
계산한 후 주어진 레코드를 해당 기억장소에 저장하거나 검색 작업을 수행하는 것을 의미. <br/>
<pre>
1. 제산법(Division), 레코드 키로 해시표의 크기보다 큰 수 중에서 가장 작은 소수로 나눈 나머지를 홈 주소로 삼는 방식.
2. 제곱법(Mid-Square), 레코드 키값을 제곱한 후 그 중간 부분의 값을 홈 주소로 삼는 방식.
3. 폴딩법(Folding), 레코드 키값을 여러 부분으로 나눈 후 각 부분의 값을 더하거나 XOR(배타적 논리합)한 값을 홈 주소로 삼는 방식.
4. 기수 변환법(Radix Conversion), 키 숫자의 진수를 다른 진수로 변환시켜 주소 크기를 초과한 높은 자릿수를 절단하고,
   이를 다시 주소 범위에 맞게 조정하는 방식.
5. 대수적 코딩법(Algebraic Coding), 키값을 이루고 있는 각 자리의 비트 수를 한 다항식의 계수로 간주하고,
   이 다항식을 해시표의 크기에 의해 정의된 다항식으로 나누어 얻은 나머지 다항식의 계수를 홈 주소로 삼는 방식.
6. 계수(숫자) 분석법(Digit Analysis), 키값을 이루는 숫자의 분포를 분석하여
   비교적 고른 자리를 필요한 만큼 택해서 홈 주소로 삼는 방식.
7. 무작위법(Random), 난수(Random Number)를 발생시켜 나온 값을 홈 주소로 삼는 방식.
</pre>

##### 라빈 카프(Rabin-Karp) 알고리즘
항상 빠르지는 않지만 일반적인 경우 빠르게 작동하는 간단한 구조의 <br/> 문자열 매칭 알고리즘이라는 점에서 자주 사용되며, 해싱에 기반하고 있음.

라빈 카프 알고리즘에 사용되는 해시 함수는 다음과 같이 연산을 수행.
<pre>
abacaaba의 해시 값
= 97 * 2^7 +
  98 * 2^6 +
  97 * 2^5 +
  99 * 2^4 +
  97 * 2^3 +
  97 * 2^2 +
  98 * 2^1 +
  97 * 2^0
= 24,833

각 문자의 아스키 코드 값에 2의 제곱 수를 차례대로 곱하여 더해준 것.
이러한 방식을 이용하면 서로 다른 문자열의 경우 일반적으로 해시 값이 다르게 나옴.

abacaabb의 해시 값
= 97 * 2^7 +
  98 * 2^6 +
  97 * 2^5 +
  99 * 2^4 +
  97 * 2^3 +
  97 * 2^2 +
  98 * 2^1 +
  98 * 2^0
= 24,834
</pre>

문자열이 달라지면 결과로 출력되는 해시 값도 바뀌는 것을 알 수 있음. <br/>
물론 해시 값이 중복되는 경우도 발생할 수 있는데, 이것을 충돌(Collision)이라고 함. <br/>
보통 발생률이 높지 않기 때문에 무시하고 넘어가는 것, <br/> 실제로는 충돌이 발생하는 경우 포인터(Pointer)를 이용해 연결 자료구조를 이용해 해결. <br/>

즉, 라빈 카프 알고리즘은 문자열의 해시 값을 비교하여 그 일치 여부를 검사하는 알고리즘이며, O(N)의 시간 복잡도를 갖음. <br/>

이렇게 빠르게 계산할 수 있는 이유는 '비교 대상'을 구하는 연속적인 과정이 연결된 수학적 수식에 의해 반복되기 때문.
<pre>
1. [a  b  a  b  a  c  a  b]  a  c  a  a  b  a  c  a  a  b  a

2. a  [b  a  b  a  c  a  b  a]  c  a  a  b  a  c  a  a  b  a

위 과정에서 바로 가장 앞에 있는 문자 'a' 만큼의 수치를 빼 준 뒤 2를 곱하고
새롭게 뒤에 들어온 'a'의 수치를 더해줌.

새로운 비교 대상 = 2 * (기존 비교 대상 - 가장 앞에 있는 문자의 수치) + 새롭게 들어온 문자의 수치
</pre>

정확하게 해시 값의 일치 여부를 검증하기 위해서 나머지 연산(MOD)를 사용하는 경우가 많으나, <br/>
일반적으로 오버 플로우(Over Flow)가 발생해도 해시 값 자체는 동일하기 때문에 나머지 연산을 굳이 사용해주지 않아도 되긴 함. <br/>

하지만 더 안정적인 프로그램을 작성하고자 할 때는 나머지 연산(MOD)를 사용하는 것을 추천. <br/>

<hr/>

### 트라이(Trie)란?
트라이란 문자열 검색을 빠르게 할 수 있는 알고리즘. <br/>
예를 들어 영어사전이 있을 때 특정 단어가 있는 지 빠르게 찾을 수 있음. <br/>
문자열을 특정 키값으로 변환해서 그 값으로 찾는 방법인 해시 테이블을 대체하기 위해 트라이를 사용할 수 있음. <br/>
불완전한 해시 테이블의 최악의 검색속도는 모든 데이터를 다 확인하는 것으로 O(N)이지만, <br/>
트라이를 사용하게 되면 문자열 길이 만큼의 O(M)의 속도가 걸리기 때문에 훨씬 더 빠르게 적용이 될 수 있음. <br/>

<img src='https://user-images.githubusercontent.com/59400030/86998582-a81a6980-c1eb-11ea-9375-3c59c1e0dddd.png' width='50%'/>

보통 트라이 알고리즘을 사용할 때 고려해야할 점이 단어의 길이, 그리고 파생되는 노드 child의 개수. <br/>
위에 영어사전으로 예를 들었는데 영어는 알파벳이 26가지로 child 노드는 26개를 갖고 있을 수 있음. <br/>
전화번호 목록같은 경우도 0부터 9가지 10가지의 수를 가지고 있을 수 있음. <br/>

이처럼 적은 child 개수를 가지고 있는 데이터 구조일 경우에 사용하는 것이 유용. <br/>
만약 차수가 그 이상으로 크고, 단어길이가 길면 그만큼 메모리 낭비가 많고, 검색 속도가 느려질 수 있다. <br/>

위의 그림에서 보여주는 것은 알파벳을 트라이구조를 활용해 단어를 찾는 과정. <br/>
실제 각 노드가 가지는 차수는 26개로 Root에서 접근해 내가 찾고자 하는 단어가 있는지 확인이 가능. <br/>

트라이를 구현하기 위해서는 데이터를 삽입하는 함수와 데이터를 찾는 두 가지 함수 구현이 필요.  <br/>

<hr/>

### 탐욕법(Greedy)이란?
여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식. <br/>
코딩이 쉽고, 구현이 쉬운건 사실이지만 적용할 수 있는 예는 많지 않음. <br/>

특성을 가지는 문제들을 해결하는데 강점이 있다. <br/>
즉, 한번의 선택이 다음 선택에는 전혀 무관한 값이여야 하며, <br/>
매 순간의 최적해가 문제에 대한 최적의 해여야 한다는 의미. <br/>

하지만 그리디 알고리즘은 항상 최적해를 보장해주는 것은 아님. <br/>
따라서, "근사치 추정"을 위해 최적이 아닌 "되는가" 또는 "적당히 괜찮은 방법"을 찾을 때 사용. <br/>
계산 속도가 정확한 알고리즘에 비해서 빠른 경우가 많기 때문에 <br/>
실용적으로 사용이 가능하나 정확한 증명이 수반되어야 함. <br/>
또, 해답을 찾아가는 과정에 있어 구한 값을 비교 값으로 설정 가능.

<pre>
1. 해 선택(Selection Procedure): 지금 당시에 가장 최적인 해를 구한뒤, 이를 부분해 집합에 추가.
2. 적절성 검사(Feasibility Check): 새로운 부분해 집합이 적절한지 검사.
3. 해 검사(Solution Check): 새로운 부분해 집합이 문제의 해가 되는지 검사 및 아직 문제의 해가 완성되지 않았다면 1번부터 다시 시작.
</pre>

<hr/>

### 동적 계획법(Dynamic Programming)이란?
큰 문제를 작은문제로 나누어 푸는 문제를 일컫는 말. <br/>
즉, 전체 문제를 작은 문제로 단순화한 다음 점화식으로 만들어 재귀적인 구조를 활용해서 전체 문제를 해결하는 방식.

<pre>
1. 전체 문제를 작은 문제로 단순화. → 부분 문제를 정의.
2. 재귀적인 구조를 활용. → 점화식을 만듦.
3. 작은 문제를 해결한 방법으로 전체 문제를 해결. → 문제 해결.
</pre>

메모이제이션(Memoization)은 동적 계획법에서 아주 중요한 개념. <br/>
함수의 값을 계산한 뒤 계산된 값을 배열에 저장하는 방식. <br/>
이러한 메모이제이션은 필요한 때마다 함수를 다시 호출하지 않고 값을 빠르게 가져옴. <br/>

동적 계획법이란 말 때문에 어떤 부분에서 동적으로 프로그래밍이 이루어지는지 찾아볼 필요가 없음. <br/>
동적 프로그래밍이란 말을 창조한 사람도 이것이 단지 멋있어서 부여한 이름이라고 함.

<hr/>

### 그래프(Graph)란?
정점과 간선으로 이루어진 자료구조의 일종. → G = ( V, E )

##### 그래프 탐색이란?
하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것.

<hr/>

### 깊이 우선 탐색(DFS, Depth-First Search)이란?
루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 <br/>
해당 분기를 완벽하게 탐색하는 방법.

<pre>
1. 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면
   다시 가장 가까운 갈림길로 돌아와서 다른 방향으로 다시 탐색을 진행하는 방법과 유사함.
2. 즉 넓게(wide) 탐색하기 전에 깊게(deep) 탐색함.
3. 모든 노드를 방문하고자 하는 경우에 이 방법을 선택함.
4. 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 좀 더 간단함.
5. 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 느림.
</pre>

자기 자신을 호출하는 순환 알고리즘의 형태를 지님. <br/>
이 알고리즘을 구현할 때 가장 큰 차이점은 그래프 탐색의 경우 <br/>
어떤 노드를 방문했었는지 여부를 반드시 검사해야한다는 것. <br/>
이를 검사하지 않을 경우 무한루프에 빠질 위험이 있음.

<hr/>

### 너비 우선 탐색(BFS, Breadth-First Search)이란?
루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법.

<pre>
1. 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법.
2. 즉 깊게(deep) 탐색하기 전에 넓게(wide) 탐색하는 것.
3. 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택함.
</pre>

BFS 는 재귀적으로 동작하지 않음. <br/>
이 알고리즘을 구현할 때 가장 큰 차이점은 그래프 탐색의 경우 <br/>
어떤 노드를 방문했었는지 여부를 반드시 검사해야한다는 것. <br/>
이를 검사하지 않을 경우 무한 루프에 빠질 위험이 있음. <br/>
BFS 는 방문한 노드들을 차례로 저장한 후 꺼낼 수 있는 자료 구조인 큐(Queue)를 사용하므로 <br/>
선입선출(FIFO) 원칙으로 탐색. <br/>
깊이가 1인 모든 노드를 방문하고 나서 그 다음에는 깊이가 2인 모든 노드를, <br/>
그 다음에는 깊이가 3인 모든 노드를 방문하는 식으로 계속 방문하다가 더 이상 방문할 곳이 없으면 탐색을 마침.

<hr/>

### 되추적(Backtracking)이란?
한정 조건을 가진 문제를 풀려는 전략으로 퇴각검색이라고도 함. <br/>
문제가 한정 조건을 가진 경우 원소의 순서는 해결 방법과 무관하며, 이런 문제는 변수 집합으로 이뤄지는데 <br/>
한정 조건을 구성하려면 각각의 변수들은 값이 있어야 함. <br/>
즉, 퇴각검색은 모든 조합을 시도해서 문제의 해를 찾음. <br/>
이것이 장점이 될 수 있는 이유는 퇴각검색 구현 방법들이 많은 부분 조합들을 배제하기 때문이며, <br/>
결국 풀이 시간이 단축. <br/>

어떤 노드의 유망성, 즉 해가 될 만한지 판단한 후 유망하지 않다고 결정되면 <br/>
그 노드의 이전 노드(부모)로 돌아가(Backtracking) 다음 자식 노드로 감. <br/>
해가 될 가능성이 있으면 '유망하다(promising)'고 하며, <br/>
유망하지 않은 노드에 가지 않는 것을 '가지치기(pruning)' 라고 함. <br/>

<pre>
4-Queens Problem이라는 예를 통해서 되추적의 개념을 알 수 있음.
4-Queens Problem은 4개의 Queen을 서로 상대방을 위협하지 않도록 4 * 4 체스판에 위치시키는 문제.
이 문제는 앞에서 배운 깊이우선탐색(Stack)과 넓이우선탐색(Queue)을 사용하여 해결하며,
되추적은 깊이우선탐색(Depth-First Search)과 마찬가지로 스택을 사용.

첫 번째 Queen을 좌표 (1, 1)에 위치 및 스택에 (1, 2), (1, 3), (1, 4)를 삽입.
스택에 자식노드를 넣기 전에 유망한지 즉, 해답이 될 가능성이 있는지 확인한 뒤 스택에 넣으므로
좌표 (2, 1)과 (2, 2)는 해답이 될 가능성이 전혀 없기 때문에 (Queen의 특성상 그 위치에 놓으면 죽으므로) 아예 가능성에서 배제.

스택에서 꺼낸 좌표 (2, 3)에 두 번째 Queen을 놓고 유망한 노드를 검사해보면 아무것도 없으므로 이 또한 배제.
그러나 좌표 (2, 4)에 두 번째 Queen을 위치시킨 후 스택에서 (3, 2)를 꺼내 Queen을 놓아도 네 번째 Queen이 들어갈 유망한 자식 노드가 없음.
즉, 좌표 (1, 1)에 Queen을 놓았을 때 해답이 없으므로 (1, 1)은 유망하지 않다는 결론이 나옴.

다음 유망한 자식인 좌표 (1, 2)를 스택에서 꺼내 Queen을 놓고 위에서 했던 방식을 다시 진행.
그럼 (1, 2), (2, 4), (3, 1), (4, 3)이라는 결론이 나오므로 해답을 찾음.
</pre>

이처럼 되추적은 해답을 찾는 과정에서 유망한지 즉, 해답이 될 가능성이 있는지를 확인하고 유망하지 않다면 <br/>
더 이상 깊게 들어가지 않고 부모 노드로 돌아오는 방식을 취함. <br/>

즉, 되추적은 "스택을 사용하고 스택에 넣기 전에 유망성 검사를 한다."는 것이 중요.
