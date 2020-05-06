# 피보나치 수열이란 앞의 두 수를 더하여 나오는 수열이다.
# 첫 번째 수와 두 번째 수는 모두 1이고, 세 번째 수부터는 이전의 두 수를 더하여 나타낸다. (1, 1, 2, 3, 5, 8, 13, …)
# 자연수 n을 입력받아 n번째 피보나치 수를 출력하는 프로그램을 작성하시오.

# 자연수 N이 입력 (n은 40보다 같거나 작다.)
# n번째 피보나치 수를 출력

listFibo = [0 for i in range(41)]

def fibonacci(n):
    if(n == 1):
        listFibo[n] = 1
        return
    elif(n == 2):
        listFibo[n] = 1
        return
    else:
        if(listFibo[n] <= 0):
            fibonacci(n-1)
            fibonacci(n-2)
            listFibo[n] = listFibo[n-1] + listFibo[n-2]
            return

num = int(input())
fibonacci(num)
print(listFibo[num])