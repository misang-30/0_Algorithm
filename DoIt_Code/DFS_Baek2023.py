# 백준 2023번
# 소문제 : 소수 찾기 문제.
# "신기한 소수" : N자리 숫자 중 왼쪽부터 1자리, 2자리,.., N자리까지 모두 소수인 수를 찾는 문제
# 입력 : N (1 ≤ N ≤ 8)
# 출력 : N자리 신기한 소수를 한 줄에 하나씩 오름차순으로 출력

# 힌트 : 1자리 소수는 2, 3, 5, 7 뿐이므로, 이 수를 시작으로 재귀적으로 N자리까지 확장하며 소수인지 확인


import sys

sys.setrecursionlimit(10000)


# 1. 입력
input = sys.stdin.readline
n = int(input())

# 알고리즘 
# 1. 2,3,5,7을 먼저 탐색. 이 중 선택한 수를 a라 한다.
# 2. 두자리 수 만든다. 이때, 10*a + i로 만드는 데, i는 1,3,5,7,9만 가능. (짝수는 소수가 될 수 없으므로)
# 3. 만약 10*a + i가 소수라면 2과정을 한번 더 해서 3자리 수를 만든다. 아니라면 넘어간다. 
# 4. N자리 되면 출력한다. 

# 소수 판별 함수 (암기)
# 4x9 = 36 처럼 어떤 수가 합성수라면 약수 2개가 모두 36의 제곱근 이하에 존재한다. 따라서 2부터 제곱근까지 나누어 떨어지는지 확인하면 된다.
# 둘다 크면 곱이 36보다 커지므로 약수가 될 수 없다.
# 따라서 N ** (1/2) 이하에서 약수를 못찾았다면 그 뒤에도 새로운 약수를 찾을 수 없다. 
# 즉, 소수이다.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
 
def DFS(num) :
    
    if len(str(num)) == n : # 자릿수 세는 방법론.
        print(num)
        return
    else :
        for i in range(10):
            if (i%2 ==0) :
                continue # continue를 만나면 현재 반복에서 남은 코드를 건너뛰고 바로 다음 반복으로 넘어가.

            if (is_prime(10*num + i )) : 
                DFS(10*num + i)


DFS (2)
DFS (3)
DFS (5)
DFS (7)



