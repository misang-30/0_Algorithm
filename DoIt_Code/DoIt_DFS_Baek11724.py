# 백준 11724번
import sys

sys.setrecursionlimit(10**4)
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# 인접리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    A[a-1].append(b)
    A[b-1].append(a)

count = 0

# 1번과 연결된 모든 노드 체크하고, 남은 노드가 있다면 COUNT 증가시키고 DFS 실행 
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)
        
print(count)
