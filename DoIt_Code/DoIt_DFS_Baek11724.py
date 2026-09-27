# 백준 11724번
import sys # 현재 실행 중인 파이썬 시스템/환경에 접근하는 모듈

input = sys.stdin.readline
n, m = map(int, input().split())
# 1. 연결 리스트 (맵) 생성
A= [[] for _ in range( n)] # 노드 개수 만큼 연결 리스트 생성

# 2. 방문 리스트 생성
visited = [False] * n



# 3. dfs 함수 정의
def dfs(v): # 방문할 방문 리스트의 인덱스 v를 매개변수로 받음
    visited[v] = True # 방문 처리
    for i in A[v]: # 연결 리스트 A에서 v에 연결된 노드들을 탐색
        if not visited[i]: # 방문하지 않은 노드라면
            dfs(i) # 재귀적으로 dfs 호출


# 4. 연결 리스트 생성
for _ in range(m):
    a,b = map(int, input().split())
    A[a-1].append(b-1) 
    A[b-1].append(a-1) 

count = 0 

for i in range(n):
    if not visited[i] :
        dfs(i) # dfs 호출
        count += 1 # 연결 요소 개수 증가 = dfs 호출 횟수 증가

print(count) # 연결 요소 개수 출력

