# MyPythonLibrary
Algorithm problem solving by python. <br/>

#### 문제 풀이 참고
* CodeUp(https://www.codeup.kr/) <br/>
* Backjoon(https://www.acmicpc.net/)

#### 아래 이론에 대한 출처
* https://gmlwjd9405.github.io/

<hr/>

### 스택(Stack)이란?

스택은 리스트의 한쪽 끝으로만 자료의 삽입, 삭제 작업이 이루어지는 자료구조. <br/>
스택은 가장 나중에 삽입된 자료가 가장 먼저 삭제되는 후입선출(LIFO)방식으로 자료를 처리.

#### Overflow
* 스택으로 할당받은 메모리 부분의 마지막 주소가 M번지라고 할 때, Top Pointer의 값이 M보다 커지면 <br/> 스택의 모든 기억장소가 꽉 채워져 있는 상태이므로 더 이상 자료를 삽입할 수 없어 Overflow를 발생.
#### Underflow
* Top Pointer가 주소 0을 가지고 있다면 스택에는 삭제할 자료가 없으므로 Underflow를 발생.  <br/> 즉, 스택에 기억되어 있는 자료를 삭제시킬 때는 제일 먼저 삭제할 자료가 있는지 없는지부터 확인.

<br/>

<pre>
push: 데이터를 스택의 가장 윗 부분에 삽입.
pop: 스택에서 가장 위에 있는 데이터를 삭제.
peek, top: 스택의 가장 위에 있는 데이터를 삭제하지 않고 반환.
isEmpty: 스택이 비어 있을 때 true를 반환.
</pre>

<hr/>

### 큐(Queue)란?
큐는 스택과 마찬가지로 일종의 리스트. <br/>
데이터 삽입은 한쪽 끝에서, 삭제는 반대쪽 끝에서만 수행하는 선입선출(FIFO)방식. <br/>
삽입이 일어나는 쪽을 rear, 삭제가 일어나는 쪽을 front라고 부름.

<img src='https://user-images.githubusercontent.com/59400030/87432263-b8cf4300-c622-11ea-987e-89349099757e.png' width='30%'/>

<pre>
insert, enqueue, offer, push: queue의 rear에 새로운 데이터를 삽입.
remove, dequeue, poll, pop: queue의 front에 있는 데이터를 삭제.
peek, element, front: 큐의 front에 있는 데이터를 삭제하지 않고 반환.
isEmpty: 큐가 비어 있을 때 true를 반환.
</pre>

<hr/>

### 분할 정복법(Divide and Conquer)이란?
분할 정복법은 주어진 문제를 작은 사례로 나누고(Divide) 각각의 작은 문제들을 해결하여 정복(Conquer)하는 방법. <br/>
분할 정복법은 문제의 사례를 2개 이상의 더 작은 사례로 나누고, <br/>
나눈 작은 사례의 해답을 바로 얻을 수 있으면 해를 구하고 아니면 더 작은 사례로 나누어 해결하는 방법. <br/>
분할 정복법은 하향식(top-down) 접근 방법으로 최상위 사례의 해답은 <br/> 아래로 내려가면서 작은 사례에 대한 해답을 구함. <br/>

#### 분할 정복법의 설계 전략
<pre>
1. 문제 사례를 하나 이상의 작은 사례로 분할(Divide).
2. 작은 사례들을 각각 정복(Conquer)한다. 작은 사례가 충분히 작지 않은 이상 재귀를 사용.
3. 필요하다면, 작은 사례에 대한 해답을 통합(Combine)하여 원래 사례의 해답을 구함.
</pre>

분할 정복법이 쓰이는 예) 이분검색, 합병정렬, 퀵정렬, 최대값 찾기, 임계값의 결정, 쉬트라센 행렬곱셈 알고리즘 등 <br/>

#### 분할 정복법의 장단점
* 장점
    - 문제를 나눔으로써 어려운 문제를 해결할 수 있다는 것이 엄청나게 중요한 장점. <br/>
      이 방식이 그대로 사용되는 효율적인 알고리즘도 여럿 있으며, <br/>
      문제를 나누어 해결한다는 특징상 병렬적으로 문제를 해결하는 데 큰 강점이 존재.
* 단점
    - 함수를 재귀적으로 호출한다는 점에서 함수 호출로 인한 오버헤드가 발생하며, <br/>
      스택에 다양한 데이터를 보관하고 있어야 하므로 스택 오버플로우가 발생하거나 <br/>
      과도한 메모리 사용을 하게 되는 단점이 존재.

<hr/>

### 완전 탐색(Brute-force)이란?
말 그대로 완전히 탐색, 답이 나올 때까지 샅샅이 찾는 방법. <br/>
컴퓨터의 순기능을 이용한 탐색 방법.  <br/>
즉, 계산이나 비교 그리고 탐색 등은 컴퓨터를 사용하여 빠르게 구하는 것이 가능. <br/>

* 장점
    - 답을 무조건 찾음. 
* 단점
    - 답을 찾는데 시간이 걸림.

#### 완전 탐색을 구현하기 위한 대표적인 4가지 방법.
<pre>
1. for문 사용
2. 순열, 조합 사용
   순열(Permutation)이란, 서로 다른 n개의 원소에서 r개를 중복 없이 선택하여 순서대로 늘어놓은 것. (nPr로 표기.)
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

### 위상 정렬(Topological Sort)이란?
어떤 일을 하는 순서를 찾는 알고리즘. <br/>
즉, '순서가 정해져있는 작업'을 차례로 수행해야 할 때 그 순서를 결정해주기 위해 사용하는 알고리즘이며, <br/>
방향 그래프에 존재하는 각 정점들의 선행 순서를 위배하지 않으면서 모든 정점을 나열하는 것. <br/>

#### 위상 정렬의 특징
* 하나의 방향 그래프에는 여러 위상 정렬이 가능.
* 위상 정렬의 과정에서 선택되는 정점의 순서를 위상 순서(Topological Order)라 함.
* 위상 정렬의 과정에서 그래프에 남아 있는 정점 중에 진입 차수가 0인 정점이 없다면, <br/> 위상 정렬 알고리즘은 중단되고 이러한 그래프로 표현된 문제는 실행이 불가능한 문제가 됨.

<br/><img src='https://user-images.githubusercontent.com/59400030/87441630-43696f80-c62e-11ea-9e0b-fdd282631401.png' width='80%'/>

<pre>
1. 진입 차수가 0인 정점(즉, 들어오는 간선의 수가 0)을 선택.
   · 진입 차수가 0인 정점이 여러 개 존재할 경우 어느 정점을 선택해도 무방.
   · 초기에 간선의 수가 0인 모든 정점을 큐에 삽입.
2. 선택된 정점과 여기에 부속된 모든 간선을 삭제.
   · 선택된 정점을 큐에서 삭제.
   · 선택된 정점에 부속된 모든 간선에 대해 간선의 수를 감소.
3. 위의 과정을 반복해서 모든 정점이 선택, 삭제되면 알고리즘 종료.
</pre>

위상 정렬의 시간 복잡도는 O(V + E). <br/>
즉, 정점의 갯수 + 간선의 갯수만큼 소요되므로 매우 빠른 알고리즘 중 하나.

<hr/>

### 삽입 정렬(Insertion Sort)이란?
자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, <br/>
자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘. <br/>

매 순서마다 해당 원소를 삽입할 수 있는 위치를 찾아 해당 위치에 넣음. <br/>

두 번째 자료부터 시작하여 그 앞(왼쪽)의 자료들과 비교하여 삽입할 위치를 지정한 후, <br/>
자료를 뒤로 옮기고 지정한 자리에 자료를 삽입하여 정렬. <br/>

즉, 두 번째 자료는 첫 번째 자료, 세 번째 자료는 두 번째와 첫 번째 자료, <br/>
네 번째 자료는 세 번째, 두 번째, 첫 번째 자료와 비교한 후 자료가 삽입될 위치를 찾음. <br/>
자료가 삽입될 위치를 찾았다면 그 위치에 자료를 삽입하기 위해 자료를 한 칸씩 뒤로 이동. <br/>

처음 Key값은 두 번째 자료부터 시작. <br/>

<br/><img src='https://user-images.githubusercontent.com/59400030/88255753-3e728300-ccf4-11ea-8645-c22bc5555b1a.png' width='70%'/>
<pre>
1회전
: 두 번째 자료인 5를 Key값으로 해서 그 이전의 자료들과 비교.
  Key값 5와 첫 번째 자료인 8을 비교.
  8이 5보다 크므로 8을 5자리에 넣고 Key값 5를 8의 자리인 첫 번째에 위치.
2회전
: 세 번째 자료인 6을 Key값으로 해서 그 이전의 자료들과 비교.
  Key값 6과 두 번째 자료인 8을 비교.
  8이 Key값보다 크므로 8을 6이 있던 세 번째 자리에 위치.
  Key값 6과 첫 번째 자료인 5를 비교.
  5가 Key값보다 작으므로 Key값 6을 두 번째 자리에 위치.
3회전
: 네 번째 자료인 2를 Key값으로 해서 그 이전의 자료들과 비교.
  Key값 2와 세 번째 자료인 8을 비교.
  8이 Key값보다 크므로 8을 2가 있던 네 번째 자리에 위치.
  Key값 2와 두 번째 자료인 6을 비교.
  6이 Key값보다 크므로 6을 세 번째 자리에 위치.
  Key값 2와 첫 번째 자료인 5를 비교.
  5가 Key값보다 크므로 5를 두 번째 자리에 넣고 그 자리에 Key값 2를 위치.
4회전
: 다섯 번째 자료인 4를 Key값으로 해서 그 이전의 자료들과 비교.
  Key값 4와 네 번째 자료인 8을 비교.
  8이 Key값보다 크므로 8을 다섯 번째 자리에 위치.
  Key값 4와 세 번째 자료인 6을 비교.
  6이 Key값보다 크므로 6을 네 번째 자리에 위치.
  Key값 4와 두 번째 자료인 5를 비교.
  5가 Key값보다 크므로 5를 세 번째 자리에 위치.
  Key값 4와 첫 번째 자료인 2를 비교.
  2가 Key값보다 작으므로 4를 두 번째 자리에 위치.
</pre>

* 장점
    - 안정적인 정렬 방법.
    - 레코드의 수가 적을 경우 알고리즘 자체가 매우 간단하므로 다른 복잡한 정렬 방법보다 유리.
    - 대부분위 레코드가 이미 정렬되어 있는 경우에 매우 효율적.
* 단점
    - 비교적 많은 레코드들의 이동을 포함.
    - 레코드 수가 많고 레코드 크기가 클 경우에 적합하지 않음.
 
#### 시간복잡도
* 최선의 경우
    - 비교 횟수
        + 이동 없이 1번의 비교만 이루어짐.
        + 외부 루프: (n-1)번
    - T(n) = O(n)
* 최악의 경우(입력 자료가 역순일 경우)
    - 비교 횟수
        + 외부 루프 안의 각 반복마다 i번의 비교 수행.
        + 외부 루프: (n-1) + (n-2) + … + 2 + 1 = n(n-1)/2 = O(n^2)
    - 교환 횟수
        + 외부 루프의 각 단계마다 (i+2)번의 이동 발생.
        + n(n-1)/2 + 2(n-1) = (n^2+3n-4)/2 = O(n^2)
    - T(n) = O(n^2)

<hr/>

### 선택 정렬(Selection Sort)이란?
해당 순서에 원소를 넣을 위치는 이미 정해져 있고, 어떤 원소를 넣을지 선택하는 알고리즘. <br/>
입력 배열(정렬되지 않은 값들) 이외에 다른 추가 메모리를 요구하지 않는 정렬 방법. <br/>

<pre>
1. 주어진 배열 중에서 최솟값을 찾기.
2. 그 값을 맨 앞에 위치한 값과 교체(패스(pass)).
3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체.
4. 하나의 원소만 남을 때까지 위의 1~3 과정을 반복.
</pre>

첫 번째 자료를 두 번째 자료부터 마지막 자료까지 차례대로 비교하여 가장 작은 값을 찾아 첫 번째에 놓고, <br/>
두 번째 자료를 세 번째 자료부터 마지막 자료까지와 차례대로 비교하여 그 중 가장 작은 값을 찾아 <br/>
두 번째 위치에 놓는 과정을 반복하며 정렬을 수행. <br/>

1회전을 수행하고 나면 가장 작은 값의 자료가 맨 앞에 오게 되므로 그 다음 회전에서는 두 번째 자료를 가지고 비교. <br/>
마찬가지로 3회전에서는 세 번째 자료를 정렬. <br/>

<br/><img src='https://user-images.githubusercontent.com/59400030/88254807-5f85a480-ccf1-11ea-868e-5c6ee60a99cd.png' width='50%'/>
<pre>
1회전
: 첫 번째 자료 9를 두 번째 자료부터 마지막 자료까지와 비교하여 가장 작은 값을 첫 번째 위치에 옮겨 위치.
  이 과정에서 자료를 4번 비교.
2회전
: 두 번째 자료 6을 세 번째 자료부터 마지막 자료까지와 비교하여 가장 작은 값을 두 번째 위치에 옮겨 위치.
  이 과정에서 자료를 3번 비교.
3회전
: 세 번째 자료 7을 네 번째 자료부터 마지막 자료까지와 비교하여 가장 작은 값을 세 번째 위치에 옮겨 위치.
  이 과정에서 자료를 2번 비교.
4회전
: 네 번째 자료 9와 마지막에 있는 7을 비교하여 서로 교환.
</pre>

* 장점
    - 자료 이동 횟수가 미리 결정.
* 단점
    - 안정성을 만족하지 않음.
    - 즉, 값이 같은 레코드가 있는 경우에 상대적인 위치가 변경될 수 있음.

#### 시간복잡도
* 비교 횟수
    - 두 개의 for 루프의 실행 횟수
    - 외부 루프: (n-1)번
    - 내부 루프(최솟값 찾기): (n-1, n-2, … , 2, 1)번
* 교환 횟수
    - 외부 루프의 실행 횟수와 동일. (즉, 상수 시간 작업.)
    - 한 번 교환하기 위하여 3번의 이동(SWAP 함수의 작업)이 필요하므로, 3(n-1)번
* T(n) = (n-1) + (n-2) + … + 2 + 1 = n(n-1)/2 = O(n^2)

<hr/>

### 버블 정렬(Bubble Sort)이란?
서로 인접한 두 원소를 검사하여 정렬하는 알고리즘. <br/>
인접한 2개의 레코드를 비교하여 크기가 순서대로 되어 있지 않으면 서로 교환. <br/>
선택 정렬과 기본 개념이 유사. <br/>

첫 번째 자료와 두 번째 자료를, 두 번째 자료와 세 번째 자료를, 세 번째와 네 번째를, … <br/>
이런 식으로 (마지막-1)번째 자료와 마지막 자료를 비교하여 교환하면서 자료를 정렬. <br/>

오름차순이라는 가정하에 1회전을 수행하고 나면 가장 큰 자료가 맨 뒤로 이동하므로 <br/>
2회전에서는 맨 끝에 있는 자료는 정렬에서 제외되고, <br/>
2회전을 수행하고 나면 끝에서 두 번째 자료까지는 정렬에서 제외. <br/>
이렇게 정렬을 1회전 수행할 때마다 정렬에서 제외되는 데이터가 하나씩 증가. <br/>

일반적으로 자료의 교환 작업(SWAP)이 자료의 이동 작업(MOVE)보다 더 복잡하기 때문에 <br/>
버블 정렬은 단순성에도 불구하고 거의 쓰이지 않음. <br/>

<br/><img src='https://user-images.githubusercontent.com/59400030/88251776-d6697000-cce6-11ea-95f5-37bb8cc9786b.png' width='70%'/>
<pre>
1회전
: 첫 번째 자료 7을 두 번째 자료 4와 비교하여 교환하고, 두 번째의 7과 세 번째의 5를 비교하여 교환하고,
  세 번째의 7과 네 번째의 1을 비교하여 교환하고, 네 번째의 7과 다섯 번째의 3을 비교하여 교환.
  이 과정에서 자료를 네 번 비교, 가장 큰 자료가 맨 끝으로 이동하므로
  다음 회전에서는 맨 끝에 있는 자료는 비교할 필요가 없음.
2회전
: 첫 번째의 4을 두 번째 5와 비교하여 교환하지 않고, 두 번째의 5와 세 번째의 1을 비교하여 교환하고,
  세 번째의 5와 네 번째의 3을 비교하여 교환.
  이 과정에서 자료를 세 번 비교, 비교한 자료 중 가장 큰 자료가 끝에서 두 번째에 위치.
3회전
: 첫 번째의 4를 두 번째 1과 비교하여 교환하고, 두 번째의 4와 세 번째의 3을 비교하여 교환.
  이 과정에서 자료를 두 번 비교, 비교한 자료 중 가장 큰 자료가 끝에서 세 번째에 위치.
4회전
: 첫 번째의 1과 두 번째의 3을 비교하여 교환하지 않음.
</pre>

* 장점
   - 구현이 매우 간단.
* 단점
   - 순서에 맞지 않은 요소를 인접한 요소와 교환. <br/>
     하나의 요소가 가장 왼쪽에서 가장 오른쪽으로 이동하기 위해서는 <br/> 배열에서 모든 다른 요소들과 교환 작업을 수행. <br/>
     특히 특정 요소가 최종 정렬 위치에 이미 있는 경우라도 교환되는 일이 발생. <br/>  
  
#### 시간복잡도
* 비교 횟수
   - 최상, 평균, 최악 모두 일정. <br/>
     (n-1, n-2, … , 2, 1)번 = n(n-1)/2
* 교환 횟수
   - 입력 자료가 역순으로 정렬되어 있는 최악의 경우, <br/> 한 번 교환하기 위하여 3번의 이동(SWAP 함수의 작업)이 필요. <br/>
     (비교 횟수 * 3)번 = 3n(n-1)/2
   - 입력 자료가 이미 정렬되어 있는 최상의 경우, 자료의 이동이 발생하지 않음.
* T(n) = O(n^2)
   - O(n)으로 하기 위해서는 교환이 일어나지 않을 때, 빠져나가는 탈출 조건이 필요.

<hr/>

### 퀵 정렬(Quick Sort)이란?
‘찰스 앤터니 리처드 호어(Charles Antony Richard Hoare)’가 개발한 정렬 알고리즘. <br/>
퀵 정렬은 불안정 정렬에 속하며, 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬에 속함. <br/>
분할 정복 알고리즘의 하나로, 평균적으로 매우 빠른 수행 속도를 자랑하는 정렬 방법. <br/>
합병 정렬(Merge Sort)과 달리 퀵 정렬은 리스트를 비균등하게 분할. <br/>

<pre>
분할(Divide): 입력 배열을 피벗을 기준으로 비균등하게 2개의 부분 배열로 분할.
             (피벗을 중심으로 왼쪽: 피벗보다 작은 요소들, 오른쪽: 피벗보다 큰 요소들)
정복(Conquer): 부분 배열을 정렬, 부분 배열의 크기가 충분히 작지 않으면 순환 호출을 이용하여 다시 분할.
결합(Combine): 정렬된 부분 배열들을 하나의 배열로 병합.
</pre>

<br/><img src='https://user-images.githubusercontent.com/59400030/87672956-b6015900-c7ae-11ea-8352-ad6497d6963f.png' width='50%'/><br/>

<pre>
1. 리스트 안에 있는 한 요소를 선택하며, 이렇게 고른 원소를 피벗(pivot) 이라고 함.
2. 피벗을 기준으로 피벗보다 작은 요소들은 모두 피벗의 왼쪽으로 옮겨지고,
   피벗보다 큰 요소들은 모두 피벗의 오른쪽으로 옮김.
   (피벗을 중심으로 왼쪽: 피벗보다 작은 요소들, 오른쪽: 피벗보다 큰 요소들)
3. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬.
   분할된 부분 리스트에 대하여 순환 호출을 이용하여 정렬을 반복.
   부분 리스트에서도 다시 피벗을 정하고 피벗을 기준으로 2개의 부분 리스트로 나누는 과정을 반복.
4. 부분 리스트들이 더 이상 분할이 불가능할 때까지 반복.
   리스트의 크기가 0이나 1이 될 때까지 반복.
</pre>

즉, 하나의 리스트를 피벗(pivot)을 기준으로 두 개의 비균등한 크기로 분할하고 <br/>
분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 <br/>
전체가 정렬된 리스트가 되게 하는 방법. <br/>

순환 호출이 한번 진행될 때마다 최소한 하나의 원소(피벗)는 최종적으로 위치가 정해지므로, <br/>
이 알고리즘은 반드시 끝난다는 것을 보장.

#### 시간복잡도
- 최선의 경우 T(n) = O(nlog₂n)
- 최악의 경우 T(n) = O(n^2)
- 평균 T(n) = O(nlog₂n)

<hr/>

### 합병 정렬(Merge Sort)이란?
전체 원소를 하나의 단위로 분할한 후, 분할한 원소를 다시 병합하는 정렬 방식. <br/>
즉, 일단 정확히 반으로 나누고 나중에 정렬하는 것. <br/>

<pre>
1. 리스트의 길이가 1이 될때까지 반으로 잘게 분할(Divide).
2. 다 나누어 졌다면, 데이터를 정렬하면서 병합(Merge). → 작은 숫자를 앞에 놓고 큰 숫자를 뒤에 놓음.
</pre>

<br/><img src='https://user-images.githubusercontent.com/59400030/87448318-a5c66e00-c636-11ea-9499-415524502016.png' width='50%'/><br/>

분할 과정은 매번 반씩 감소하므로 밑이 2인 logN만큼 반복해야 크기가 1인 배열로 분할 가능. <br/>
각 분할 별로 병합하므로 합병 정렬의 시간복잡도는 O(NlogN). <br/>
즉, 합병 정렬은 일반적인 경우 퀵 정렬보다 느리지만 어떠한 상황에서도 <br/>
정확히 O(NlogN)을 보장할 수 있다는 점에서 몹시 효율적인 알고리즘. <br/>

합병 정렬을 구현할 때 신경써야 하는 부분은 반드시 정렬에 사용되는 배열은 '전역 변수'로 선언해야 한다는 것. <br/>
만약 함수 안에서 배열을 선언하게 된다면 매번 배열을 선언해야 한다는 점에서 메모리 자원의 낭비가 발생. <br/>
이와 같이 합병 정렬은 '기존의 데이터를 담을 추가적인 배열 공간이 필요하다'는 점에서 <br/>
메모리 활용이 비효율적이라는 문제가 있음.

<hr/>

### 힙 정렬(Heap Sort)이란?

#### 힙(Heap)이란?
* 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조.
* 여러 개의 값들 중에서 최댓값이나 최솟값을 쉽고, 빠르게 찾아내도록 만들어진 자료구조.
* 힙은 일종의 반정렬 상태(느슨한 정렬 상태)를 유지.
    - 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있다는 정도.
    - 간단히 말하면 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰(작은) 이진 트리를 말함.
* 힙 트리에서는 중복된 값을 허용. (이진 탐색 트리에서는 중복된 값을 허용하지 않는다.)

#### 힙(Heap)의 종류
* 최대 힙(Max Heap)
    - 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리.
    - key(부모 노드) >= key(자식 노드)
* 최소 힙(Min Heap)
    - 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리.
    - key(부모 노드) <= key(자식 노드)
<br/><br/><img src='https://user-images.githubusercontent.com/59400030/88256733-fe60cf80-ccf6-11ea-8b52-983dcb737096.png' width='70%'/><br/>

#### 힙(Heap)의 구현
* 힙을 저장하는 표준적인 자료구조는 배열.
* 구현을 쉽게 하기 위하여 배열의 첫 번째 인덱스인 0은 사용되지 않음.
* 특정 위치의 노드 번호는 새로운 노드가 추가되어도 변하지 않음.
    - 예를 들어, 루트 노드의 오른쪽 노드의 번호는 항상 3.
* 힙에서의 부모 노드와 자식 노드의 관계
    - 왼쪽 자식의 인덱스 = (부모의 인덱스) * 2
    - 오른쪽 자식의 인덱스 = (부모의 인덱스) * 2 + 1
    - 부모의 인덱스 = (자식의 인덱스) / 2
<br/><br/><img src='https://user-images.githubusercontent.com/59400030/88258290-c6f42200-ccfa-11ea-91d2-4435078ef02c.png' width='70%'/><br/>

따라서 힙 정렬(Heap Sort)이란, 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 하는 방법. <br/>
내림차순 정렬을 위해서는 최대 힙(Max Heap)을 구성하고, <br/> 오름차순 정렬을 위해서는 최소 힙(Min Heap)을 구성. <br/>

<pre>
1. 정렬해야 할 n개의 요소들로 최대 힙(완전 이진 트리 형태)을 구현. (내림차순을 기준으로 정렬.)
2. 그 다음으로 한 번에 하나씩 요소를 힙에서 꺼내서 배열의 뒤부터 저장.
3. 삭제되는 요소들(최댓값부터 삭제)은 값이 감소되는 순서로 정렬.
</pre>

힙(Heap)은 1차원 배열로 쉽게 구현. <br/>
정렬해야 할 n개의 요소들을 1차원 배열에 기억한 후 최대 힙 삽입을 통해 차례대로 삽입. <br/>
최대 힙으로 구성된 배열에서 최댓값부터 삭제. <br/>

#### 최대 힙(Max Heap)의 삽입
힙에 새로운 요소가 들어오면, 일단 새로운 노드를 힙의 마지막 노드에 이어서 삽입. <br/>
새로운 노드를 부모 노드들과 교환해서 힙의 성질을 만족. <br/>
<br/><img src='https://user-images.githubusercontent.com/59400030/88256969-9fe82100-ccf7-11ea-9a17-924cbb5c2b13.png' width='70%'/><br/>

#### 최대 힙(Max Heap)의 삭제
최대 힙에서 최댓값은 루트 노드이므로 루트 노드가 삭제. <br/>
최대 힙(Max Heap)에서 삭제 연산은 최댓값을 가진 요소를 삭제하는 것. <br/>
삭제된 루트 노드에는 힙의 마지막 노드를 가져오고, 힙을 재구성. <br/>
<br/><img src='https://user-images.githubusercontent.com/59400030/88257059-df167200-ccf7-11ea-9111-0c1178df5943.png' width='70%'/><br/>

#### 힙 정렬의 특징
* 시간 복잡도가 좋은 편.
* 힙 정렬이 가장 유용한 경우는 전체 자료를 정렬하는 것이 아닌 가장 큰 값 몇개만 필요할 때.

#### 시간복잡도
* 힙 트리의 전체 높이가 거의 log₂n(완전 이진 트리이므로)이므로 하나의 요소를 <br/>
  힙에 삽입하거나 삭제할 때 힙을 재정비하는 시간이 log₂n만큼 소요.
* 요소의 개수가 n개 이므로 전체적으로 O(nlog₂n)의 시간이 걸림.
* T(n) = O(nlog₂n)

<hr/>

### 정렬 알고리즘 시간복잡도 비교
<img src='https://user-images.githubusercontent.com/59400030/87674758-683a2000-c7b1-11ea-9a97-38641f8f913b.png' width='70%'/><br/>

* 단순(구현 간단)하지만 비효율적인 방법
    - 삽입 정렬, 선택 정렬, 버블 정렬
* 복잡하지만 효율적인 방법
    - 퀵 정렬, 힙 정렬, 합병 정렬

<hr/>

### 트리(Tree)란?
트리는 노드로 이루어진 자료구조. <br/>
트리는 하나의 루트 노드를 갖으며, 루트 노드는 0개 이상의 자식 노드를 갖고 있음. <br/>
그 자식 노드 또한 0개 이상의 자식 노드를 갖고 있고, 이는 반복적으로 정의됨. <br/>

노드(node)들과 노드들을 연결하는 간선(edge)들로 구성. <br/>
트리에는 사이클(cycle)이 존재할 수 없음. <br/>
노드들은 특정 순서로 나열될 수도 있고 그럴 수 없을 수도 있음. <br/>
각 노드는 부모 노드로의 연결이 있을 수도 있고 없을 수도 있음. <br/>
각 노드는 어떤 자료형으로도 표현 가능. <br/>

비선형 자료구조로 계층적 관계를 표현. (디렉터리 구조, 조직도 등) <br/>

사이클(cycle)이 없는 하나의 연결 그래프(Connected Graph) <br/>
또는 DAG(Directed Acyclic Graph, 방향성이 있는 비순환 그래프)의 한 종류. <br/>

#### 트리(Tree)와 관련된 용어
<br/><img src='https://user-images.githubusercontent.com/59400030/88365194-3718ab80-cdc0-11ea-8429-9e9c73c3c140.png' width='50%'/><br/>
* 루트 노드(root node): 부모가 없는 노드, 트리는 하나의 루트 노드만을 가짐.
* 단말 노드(leaf node): 자식이 없는 노드, ‘말단 노드’ 또는 ‘잎 노드’라고도 부름.
* 내부(internal) 노드: 단말 노드가 아닌 노드.
* 간선(edge): 노드를 연결하는 선. ('link', 'branch'라고도 부름.)
* 형제(sibling): 같은 부모를 가지는 노드.
* 노드의 크기(size): 자신을 포함한 모든 자손 노드의 개수.
* 노드의 깊이(depth): 루트에서 어떤 노드에 도달하기 위해 거쳐야 하는 간선의 수.
* 노드의 레벨(level): 트리의 특정 깊이를 가지는 노드의 집합.
* 노드의 차수(degree): 하위 트리 개수 / 간선 수 (degree) = 각 노드가 지닌 가지의 수.
* 트리의 차수(degree of tree): 트리의 최대 차수.
* 트리의 높이(height): 루트 노드에서 가장 깊숙히 있는 노드의 깊이.

#### 트리(Tree)의 특징
* 그래프의 한 종류로 ‘최소 연결 트리’라고도 부름.
* 트리는 계층 모델이며, DAG(Directed Acyclic Graphs, 방향성이 있는 비순환 그래프)의 한 종류.
* loop, circuit, self-loop와 같은 사이클이 없음.
* 노드가 N개인 트리는 항상 N-1개의 간선(edge)을 가짐. <br/> 즉, 간선은 항상 (정점의 개수 - 1)만큼을 가짐.
* 루트에서 어떤 노드로 가는 경로는 유일하며, 임의의 두 노드 간의 경로도 유일. <br/> 즉, 두 개의 정점 사이에 반드시 1개의 경로만을 가짐.
* 한 개의 루트 노드만이 존재하며 모든 자식 노드는 한 개의 부모 노드만을 가짐.
* 부모-자식 관계이므로 흐름은 top-bottom 아니면 bottom-top으로 이루어짐.
* 순회는 Pre-order, In-order 아니면 Post-order로 이루어짐. (이 3가지 모두 DFS/BFS 안에 있음.)
* 트리는 이진 트리, 이진 탐색 트리, 균형 트리(AVL 트리, 레드-블랙 트리 등), 이진 힙(최대 힙, 최소 힙) 등이 있음.

#### 트리(Tree)의 종류

##### 이진 트리(Binary Tree)
* 각 노드가 최대 두 개의 자식을 갖는 트리.
* 모든 트리가 이진 트리는 아님.
* 이진 트리 순회
    - 중위 순회(in-order traversal): 왼쪽 가지 → 현재 노드 → 오른쪽 가지
    - 전위 순회(pre-order traversal): 현재 노드 → 왼쪽 가지 → 오른쪽 가지
    - 후위 순회(post-order traversal): 왼쪽 가지 → 오른쪽 가지 → 현재 노드
    
##### 이진 탐색 트리(Binary Search Tree)
* 모든 노드가 특정 순서를 따르는 속성이 있는 이진 트리.
    - 모든 왼쪽 자식들 < n < 모든 오른쪽 자식들 (모든 노드는 n(부모 노드)에 대해서 반드시 참.)
        + 각 노드의 왼쪽 서브트리에는 해당 노드의 값보다 작은 값을 지닌 노드들로 이루어짐.
        + 각 노드의 오른쪽 서브트리에는 해당 노드의 값보다 큰 값을 지닌 노드들로 이루어짐.
    - 중복된 노드가 없음.

##### 균형 이진 트리(Balance Binary Tree)
* 빠른 시간(O(logN)) 안에 삽입, 삭제 그리고 탐색을 할 수 있을 정도로 균형이 잘 잡혀 있는 경우.
    - 예) 레드-블랙 트리, AVL 트리 등
    - 불균형 트리라면 O(n)의 시간복잡도를 가짐.

##### 완전 이진 트리(Complete Binary Tree)
<br/><img src='https://user-images.githubusercontent.com/59400030/88366741-efe0e980-cdc4-11ea-8b54-22a055b90a26.png' width='70%'/><br/>
* 트리의 모든 높이에서 노드가 꽉 차 있는 이진 트리. <br/> 즉, 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있음.
* 마지막 레벨은 꽉 차 있지 않아도 되자만 노드가 왼쪽에서 오른쪽으로 채워져야 함.
* 마지막 레벨 h에서 (1 ~ 2h-1)개의 노드를 가질 수 있음.
* 또 다른 정의는 가장 오른쪽의 잎 노드가 (아마도 모두) 제거된 포화 이진 트리.
* 완전 이진 트리는 배열을 사용해 효율적으로 표현 가능.

##### 전 이진 트리(Full Binary Tree 또는 Strictly Binary Tree)
<br/><img src='https://user-images.githubusercontent.com/59400030/88366777-05eeaa00-cdc5-11ea-8d25-2b4965ef1dcc.png' width='70%'/><br/>
* 모든 노드가 0개 또는 2개의 자식 노드를 갖는 트리.

##### 포화 이진 트리(Perfect Binary Tree)
<br/><img src='https://user-images.githubusercontent.com/59400030/88366791-12730280-cdc5-11ea-8a94-be9b79f7488b.png' width='70%'/><br/>
* 전 이진 트리이면서 완전 이진 트리인 경우.
* 모든 말단 노드는 같은 높이에 있어야 하며, 마지막 단계에서 노드의 개수가 최대가 되어야 함.
* 모든 내부 노드가 두 개의 자식 노드를 가짐.
* 모든 말단 노드가 동일한 깊이 또는 레벨을 가짐.
* 노드의 개수가 정확히 2^(k-1)개여야 함. (k: 트리의 높이) <br/> → 흔하게 나타나는 경우가 아님. (즉, 이진 트리가 모두 포화 이진 트리일 것이라고 생각하면 안 됨.)

##### 이진 힙(Binary Heap)

###### 최소 힙(Min Heap)
* 트리의 마지막 단계에서 오른쪽 부분을 뺀 나머지 부분이 가득 채워져 있는 완전 이진 트리이며, <br/> 각 노드의 원소가 자식들의 원소보다 작음. <br/> 즉, key(부모 노드) >= key(자식 노드)인 완전 이진 트리.
* 가장 큰 값은 루트 노드.
* N개가 힙에 들어가 있으면 높이는 log(N).

###### 최대 힙(Max Heap)
* 원소가 내림차순으로 정렬되어 있다는 점에서만 최소힙과 다름.
* 각 노드의 원소가 자식들의 원소보다 큼.

##### 트라이(Trie) (‘접두사 트리(Prefix Tree)’라고도 부름.)
* n-차 트리(n-ary Tree)의 변종.
* 각 노드에 문자를 저장하는 자료구조.
* 따라서 트리를 아래쪽으로 순회하면 단어 하나가 나옴.
* 접두사를 빠르게 찾아보기 위한 흔한 방식으로, 모든 언어를 트라이에 저장해 놓는 방식.
* 유효한 단어 집합을 이용하는 많은 문제들은 트라이를 통해 최적화할 수 있음.

#### 트리(Tree)의 구현
* 기본적으로 트리는 그래프의 한 종류이므로 그래프의 구현 방법(인접 리스트 또는 인접 배열)으로 구현 가능.

##### 인접 배열(Adjacency Matrix)
* 1차원 배열에 자신의 부모 노드만 저장하는 방법.
* 트리는 부모 노드를 0개(루트 노드) 또는 1개를 가지기 때문.
* 이진 트리의 경우, 2차원 배열에 자식 노드를 저장하는 방법.
* 이진 트리는 각 노드가 최대 두 개의 자식을 갖는 트리이기 때문.
* 예) A[i][0]: 왼쪽 자식 노드, A[i][1]: 오른쪽 자식 노드

##### 인접 행렬(Adjacency List)
* 가중치가 없는 트리의 경우
    - ArrayList< ArrayList > list = new ArrayList<>();
* 가중치가 있는 트리의 경우
    - class Node { int num, dist; // 노드 번호, 거리 } // 정의
    - ArrayList[] list = new ArrayList[정점의 수 + 1];

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

### 그래프(Graph)란?
단순히 정점(N, node)과 그 정점 연결하는 간선(E, edge)을 하나로 모아 놓은 자료 구조. → G = ( V, E ) <br/>
즉, 연결되어 있는 객체 간의 관계를 표현할 수 있는 자료 구조. (지도, 지하철 노선도의 최단 경로 등) <br/>
그래프는 여러 개의 고립된 부분 그래프(Isolated Subgraphs)로 구성. <br/>

#### 그래프(Graph)와 관련된 용어
* 정점(vertex): 위치라는 개념. ('node'라고도 부름.)
* 간선(edge): 위치 간의 관계. (즉, 노드를 연결하는 선. ('link', 'branch'라고도 부름.))
* 인접 정점(adjacent vertex): 간선에 의해 직접 연결된 정점.
* 정점의 차수(degree): 무방향 그래프에서 하나의 정점에 인접한 정점의 수.
    - 무방향 그래프에 존재하는 정점의 모든 차수의 합 = 그래프의 간선 수의 2배.
* 진입 차수(in-degree): 방향 그래프에서 외부에서 오는 간선의 수. (내차수 라고도 부름.)
* 진출 차수(out-degree): 방향 그래프에서 외부로 향하는 간선의 수. (외차수 라고도 부름.)
    - 방향 그래프에 있는 정점의 진입 차수 또는 진출 차수의 합 <br/> = 방향 그래프의 간선의 수(내차수 + 외차수).
* 경로 길이(path length): 경로를 구성하는 데 사용된 간선의 수.
* 단순 경로(simple path): 경로 중에서 반복되는 정점이 없는 경우.
* 사이클(cycle): 단순 경로의 시작 정점과 종료 정점이 동일한 경우.

#### 그래프(Graph)의 특징
* 그래프는 네트워크 모델.
* 2개 이상의 경로가 가능.
    - 즉, 노드들 사이에 무방향/방향에서 양방향 경로를 가질 수 있음.
* self-loop 뿐 아니라 loop/circuit 모두 가능.
* 루트 노드라는 개념이 없음.
* 부모-자식 관계라는 개념이 없음.
* 순회는 DFS나 BFS로 이루어짐.
* 그래프는 순환(Cyclic) 혹은 비순환(Acyclic).
* 그래프는 크게 방향 그래프와 무방향 그래프가 있음.
* 간선의 유무는 그래프에 따라 다름.

#### 그래프(Graph)와 트리(Tree)의 차이
<img src='https://user-images.githubusercontent.com/59400030/88264479-c95c7900-cd06-11ea-869a-f22852358ff3.png' width='70%'/>

#### 그래프(Graph)의 종류

##### 무방향 그래프 & 방향 그래프
* 무방향 그래프(Undirected Graph)
    - 무방향 그래프의 간선은 간선을 통해서 양 방향으로 갈 수 있음.
    - 정점 A와 정점 B를 연결하는 간선은 (A, B)와 같이 정점의 쌍으로 표현.
        + (A, B)는 (B, A)와 동일.
    - Ex) 양방향 통행 도로
* 방향 그래프(Directed Graph)
    - 간선에 방향성이 존재하는 그래프.
    - A → B로만 갈 수 있는 간선은 <A, B>로 표시.
        + <A, B>는 <B, A>와 다름.
    - Ex) 일방 통행

##### 가중치 그래프
* 가중치 그래프(Weighted Graph)
    - 간선에 비용이나 가중치가 할당된 그래프.
    - ‘네트워크(Network)’ 라고도 한다.
        + Ex) 도시-도시의 연결, 도로의 길이, 회로 소자의 용량, 통신망의 사용료 등

##### 연결 그래프 & 비연결 그래프
* 연결 그래프(Connected Graph)
    - 무방향 그래프에 있는 모든 정점쌍에 대해서 항상 경로가 존재하는 경우.
    - Ex) 트리(Tree): 사이클을 가지지 않는 연결 그래프.
* 비연결 그래프(Disconnected Graph)
    - 무방향 그래프에서 특정 정점쌍 사이에 경로가 존재하지 않는 경우.

##### 사이클 & 비순환 그래프
* 사이클(Cycle)
    - 단순 경로의 시작 정점과 종료 정점이 동일한 경우.
        + 단순 경로(Simple Path): 경로 중에서 반복되는 정점이 없는 경우.
* 비순환 그래프(Acyclic Graph)
    - 사이클이 없는 그래프.

##### 완전 그래프
* 완전 그래프(Complete Graph)
    - 그래프에 속해 있는 모든 정점이 서로 연결되어 있는 그래프.
    - 무방향 완전 그래프.
        + 정점 수: n이면 간선의 수 = n(n-1)/2

#### 그래프(Graph)의 구현

##### 인접 리스트(Adjacency List)
인접 리스트(Adjacency List)로 그래프를 표현하는 것이 가장 일반적인 방법.
* 모든 정점(혹은 노드)을 인접 리스트에 저장. <br/>
  즉, 각각의 정점에 인접한 정점들을 리스트로 표시한 것.
    - 배열(혹은 해시테이블)과 배열의 각 인덱스마다 존재하는 <br/>
      또 다른 리스트(배열, 동적 가변 크기 배열(ArrayList), 연결리스트(LinkedList) 등)를 <br/> 이용해서 인접 리스트를 표현.
    - 정점의 번호만 알면 이 번호를 배열의 인덱스로 하여 각 정점의 리스트에 쉽게 접근 가능.
* 무방향 그래프(Undirected Graph)에서 A와 B 사이의 간선을 두 번 저장.
    - 한 번은 A 정점에 인접한 간선을 저장하고, 다른 한 번은 B 정점에 인접한 간선을 저장.
    - 정점의 수가 N, 간선의 수가 E인 무방향 그래프 → N개의 리스트, N개의 배열, 2E개의 노드가 필요.
* 트리에선 특정 노드 하나(루트 노드)에서 다른 모든 노드로 접근이 가능. → Tree 클래스 불필요.
    - 그래프에선 특정 노드에서 다른 모든 노드로 접근이 가능하지는 않음. → Graph 클래스 필요.

##### 인접 행렬(Adjacency Matrix)
인접 행렬은 NxN 불린 행렬(Boolean Matrix)로써 matrix[i][j]가 true라면 i → j로의 간선이 있다는 뜻.
* 0과 1을 이용한 정수 행렬(Integer Matrix)을 사용할 수도 있음.
* 정점(노드)의 개수가 N인 그래프를 인접 행렬로 표현.
    - 간선의 수와 무관하게 항상 n^2개의 메모리 공간이 필요.
* 무방향 그래프를 인접 행렬로 표현한다면 이 행렬은 대칭 행렬(Symmetric Matrix).
    - 물론 방향 그래프는 대칭 행렬이 안 될 수도 있음.
* 인접 리스트를 사용한 그래프 알고리즘들(Ex. 너비 우선 탐색) 또한 인접 행렬에서도 사용이 가능.
    - 하지만 인접 행렬은 조금 효율성이 떨어짐.
    - 인접 리스트는 어떤 노드에 인접한 노드들을 쉽게 찾을 수 있지만, <br/>
      인접 행렬에서는 인접한 노드를 찾기 위해서는 모든 노드를 전부 순회해야 함.

##### 인접 리스트(Adjacency List)와 인접 행렬(Adjacency Matrix) 중 선택 방법
* 인접 리스트
    - 그래프 내에 적은 숫자의 간선만을 가지는 희소 그래프(Sparse Graph)의 경우.
    - 장점
        + 어떤 노드에 인접한 노드들 을 쉽게 찾을 수 있음.
        + 그래프에 존재하는 모든 간선의 수는 O(N+E)안에 알 수 있음. → 인접 리스트 전체를 조사.
    - 단점
        + 간선의 존재 여부와 정점의 차수 = 정점 i의 리스트에 있는 노드의 수. <br/>
          즉, 정점 차수만큼의 시간이 필요.

* 인접 행렬
    - 그래프에 간선이 많이 존재하는 밀집 그래프(Dense Graph)의 경우.
    - 장점
        + 두 정점을 연결하는 간선의 존재 여부 (M[i][j])를 O(1) 안에 즉시 알 수 있음.
        + 정점의 차수는 O(N)안에 알 수 있음. → 인접 배열의 i번 째 행 또는 열을 모두 더함.
    - 단점
        + 어떤 노드에 인접한 노드들을 찾기 위해서는 모든 노드를 전부 순회해야 함.
        + 그래프에 존재하는 모든 간선의 수는 O(N^2)안에 알 수 있음. → 인접 행렬 전체를 조사.

#### 그래프 탐색이란?
하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것. <br/>

##### 일반적인 방법 두 가지

###### 깊이 우선 탐색(DFS, Depth-First Search)
* 모든 노드를 방문 하고자 하는 경우에 이 방법을 선택.
* 깊이 우선 탐색이 너비 우선 탐색보다 좀 더 간단.

###### 너비 우선 탐색(BFS, Breadth-First Search)
* 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택. <br/>

즉, 지구상에 존재하는 모든 친구 관계를 그래프로 표현한 후 A와 B 사이에 존재하는 경로를 찾을 때, <br/>
깊이 우선 탐색은 모든 친구 관계를 탐색하고, 너비 우선 탐색은 A와 가까운 관계부터 탐색.

<hr/>

### 깊이 우선 탐색(DFS, Depth-First Search)이란?
루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 <br/>
해당 분기를 완벽하게 탐색하는 방법.

<pre>
1. 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면
   다시 가장 가까운 갈림길로 돌아와서 다른 방향으로 다시 탐색을 진행하는 방법과 유사함.
2. 즉, 넓게(wide) 탐색하기 전에 깊게(deep) 탐색함.
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
루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법. <br/>
너비 우선 탐색(BFS)이 깊이 우선 탐색(DFS)보다 좀 더 복잡. <br/>

<pre>
1. 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법.
2. 즉, 깊게(deep) 탐색하기 전에 넓게(wide) 탐색하는 것.
3. 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택함.
</pre>

#### 너비 우선 탐색(BFS)의 특징
* 직관적이지 않음.
* BFS는 재귀적으로 동작하지 않음.
* 이 알고리즘을 구현할 때 주의해야 하는 것은 <br/>
  어떤 노드를 방문했었는지 여부를 반드시 검사해야한다는 것이며, <br/>
  이를 검사하지 않을 경우 무한 루프에 빠질 위험이 있음.
* 방문한 노드들을 차례로 저장한 후 꺼낼 수 있는 자료 구조인 큐(Queue)를 사용하므로 <br/>
  즉, 선입선출(FIFO) 원칙으로 탐색.

#### 너비 우선 탐색(BFS)의 과정
깊이가 1인 모든 노드를 방문하고 나서 그 다음에는 깊이가 2인 모든 노드를, <br/>
그 다음에는 깊이가 3인 모든 노드를 방문하는 식으로 계속 방문하다가 더 이상 방문할 곳이 없으면 탐색을 마침. <br/>

<img src='https://user-images.githubusercontent.com/59400030/88892428-b6562580-d27f-11ea-971a-701dbcbfca69.png' width='50%'/><br/>

<pre>
1. 시작 노드를 방문. (방문한 노드는 체크!)
   큐에 방문한 노드를 삽입(enqueue).
   초기 상태의 큐에는 시작 노드만이 저장.
   즉, 시작 노드의 이웃 노드를 모두 방문한 다음, 이웃의 이웃들을 방문.
2. 큐에서 꺼낸 노드와 인접한 노드들을 모두 차례로 방문. (단, 이미 방문했던 노드는 제외.)
   인접한 노드가 없으면 큐에서 다음 노드를 출력(dequeue)하고,
   있으면 큐에 방문한 노드를 삽입(enqueue).
3. 큐에 삽입된 노드들이 소진될 때까지 반복.
</pre>

#### 너비 우선 탐색(BFS)의 시간 복잡도
* 인접 리스트로 표현된 그래프: O(N+E)
* 인접 행렬로 표현된 그래프: O(N^2)
* 깊이 우선 탐색(DFS)과 마찬가지로 그래프 내에 적은 숫자의 간선만을 가지는 <br/>
  희소 그래프(Sparse Graph) 의 경우 인접 행렬보다 인접 리스트를 사용하는 것이 유리.

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
3. 해 검사(Solution Check): 새로운 부분해 집합이 문제의 해가 되는지 검사하고,
                           아직 문제의 해가 완성되지 않았다면 1번부터 다시 시작.
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

<hr/>

### 해싱(Hashing)이란?
대부분의 탐색 방법들은 탐색 키를 저장된 키 값과 반복적으로 비교하면서 탐색을 원하는 항목에 접근. <br/>
반면 해싱은 키 값에 직접 산술적인 연산을 적용하여 항목이 저장되어 있는 테이블의 주소를 계산하여 항목에 접근. <br/>
이렇게 키 값의 연산에 의해 직접 접근이 가능한 구조를 해시 테이블(Hash Table)이라 부름. <br/>

해시 테이블(Hash Table)은 레코드를 한개 이상 보관할 수 있는 버킷(Bucket)들로 구성된 기억 공간으로 <br/>
보조기억장치에 구성할 수도 있고, 주기억장치에 구성할 수도 있음.

<pre>
Bucket: 하나의 주소를 갖는 파일의 한 구역을 의미, Bucket의 크기는 같은 주소에 포함될 수 있는 레코드 수를 의미.
             
Slot: 한 개의 레코드를 저장할 수 있는 공간으로 n개의 Slot이 모여 하나의 Bucket을 형성.

Collision: 서로 다른 두 개 이상의 레코드가 같은 주소를 갖는 현상.

Synonym: 충돌로 인해 같은 Home Address를 갖는 레코드들의 집합.

Overflow: 계산된 Home Address의 Bucket 내에 저장할 기억 공간이 없는 상태로,
          Bucket을 구성하는 Slot이 여러 개일 때 Collision은 발생해도 Overflow는 발생하지 않을 수 있음.
</pre>

키들의 비교에 의한 탐색 방법은 정렬이 안 되어 있다면 O(n)이고, 정렬이 되어 있다면 O(log(n)). <br/>
정렬되어 있는 경우의 시간 복잡도가 O(log(n))인 건 이진 탐색의 시간 복잡도를 생각하면 쉬움. <br/>

해싱은 이론적으로 O(1)의 시간 안에 탐색을 끝마칠 수 있으므로 <br/>
위와 같은 시간 복잡도 보다 더욱 빠른 탐색을 필요로 할 때 사용. <br/>

#### 해싱은 다음과 같이 크게 세 가지로 구분.
<pre>
1. 완전 해싱(Perfect Hashing)
   완전 해싱은 나중에 좋은 해싱 기법으로 언급될 simple uniform 해싱을 의미.
   즉 서로 다른 키(key)값이 해싱에 의해 주소값을 할당받을 때, 주소값이 절대로 겹치지 않는 이상적인 해싱을 의미.
   물론 이런 방식은 일대일대응 이외에는 존재하지 않는 방식으로 이상적인 것.
2. 정형 해싱(Conventional Hashing)
   데이터 개수를 이미 알고 있어서, 데이터들이 저장될 주소 범위를 미리 데이터 개수만큼 지정해 두는 방식을 의미.
   즉, 필요한 메모리의 크기는 미리 측정되고 미리 할당받아야 함.
3. 동적 해싱(Dynamic Hashing)
   정형 해싱의 문제점은 데이터를 입력하기 이전에 데이터 개수에 대한 정보가 있어서
   메모리를 미리 할당받아야 한다는 점.
   일반적으로 시간이 지남에 따라서 데이터의 양의 증가하게 되므로
   잘못된 측정으로 데이터가 메모리의 범위를 넘게 되면,
   더 큰 메모리 크기를 잡고 다시 해싱을 해야 하는 시간적, 자원적 낭비가 일어나게 됨.
   동적 해싱은 이러한 데이터의 증감에 적응하기 위해서 나타난 것으로,
   동적으로 메모리의 크기를 변화시키는 해싱 기법을 의미.
</pre>

즉, 해싱은 가변 크기의 입력값에서 고정된 크기의 출력값을 생성해 내는 과정을 의미하며, <br/>
해시 함수(Hash Function)라 알려진 수학적 공식을 따라 진행. <br/>

여기서 해시 함수(Hash Function)란, 레코드 키에 대한 해시 테이블(Hash Table)내의 홈 주소(Home Address)를 <br/>
계산한 후 주어진 레코드를 해당 기억장소에 저장하거나 검색 작업을 수행하는 것을 의미.
<pre>
1. 제산법(Division), 레코드 키로 해시표의 크기보다 큰 수 중에서
   가장 작은 소수로 나눈 나머지를 홈 주소로 삼는 방식.
                    
2. 제곱법(Mid-Square), 레코드 키값을 제곱한 후 그 중간 부분의 값을 홈 주소로 삼는 방식.

3. 폴딩법(Folding), 레코드 키값을 여러 부분으로 나눈 후 각 부분의 값을 더하거나,
   XOR(배타적 논리합)한 값을 홈 주소로 삼는 방식.
                   
4. 기수 변환법(Radix Conversion), 키 숫자의 진수를 다른 진수로 변환시켜
   주소 크기를 초과한 높은 자릿수를 절단하고, 이를 다시 주소 범위에 맞게 조정하는 방식.
                                
5. 대수적 코딩법(Algebraic Coding), 키값을 이루고 있는 각 자리의 비트 수를 한 다항식의 계수로 간주하고,
   이 다항식을 해시표의 크기에 의해 정의된 다항식으로 나누어 얻은 나머지 다항식의 계수를 홈 주소로 삼는 방식.
                                  
6. 계수(숫자) 분석법(Digit Analysis), 키값을 이루는 숫자의 분포를 분석하여
   비교적 고른 자리를 필요한 만큼 택해서 홈 주소로 삼는 방식.
                                    
7. 무작위법(Random), 난수(Random Number)를 발생시켜 나온 값을 홈 주소로 삼는 방식.
</pre>

#### 라빈 카프(Rabin-Karp) 알고리즘
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

즉, 라빈 카프 알고리즘은 문자열의 해시 값을 비교하여 그 일치 여부를 검사하는 알고리즘이며, <br/> O(N)의 시간 복잡도를 가짐. <br/>

이렇게 빠르게 계산할 수 있는 이유는 '비교 대상'을 구하는 연속적인 과정이 연결된 수학적 수식에 의해 반복되기 때문.
<pre>
1. [a  b  a  b  a  c  a  b]  a  c  a  a  b  a  c  a  a  b  a

2. a  [b  a  b  a  c  a  b  a]  c  a  a  b  a  c  a  a  b  a

위 과정에서 바로 가장 앞에 있는 문자 'a' 만큼의 수치를 빼 준 뒤 2를 곱하고
새롭게 뒤에 들어온 'a'의 수치를 더해줌.

새로운 비교 대상 = 2 * (기존 비교 대상 - 가장 앞에 있는 문자의 수치) + 새롭게 들어온 문자의 수치
</pre>

정확하게 해시 값의 일치 여부를 검증하기 위해서 나머지 연산(MOD)를 사용하는 경우가 많으나, <br/>
일반적으로 오버 플로우(Over Flow)가 발생해도 해시 값 자체는 동일하기 때문에 <br/> 나머지 연산을 굳이 사용해주지 않아도 되긴 함. <br/>

하지만 더 안정적인 프로그램을 작성하고자 할 때는 나머지 연산(MOD)를 사용하는 것을 추천. <br/>
