graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0],
]

n = len(graph)  # 행
m = len(graph[0])   # 열
print(f"n:{n}")
print(f"m:{m}")

# 스택을 활용한 dfs 구현
def dfs_stack(x, y):
    start_node = (x,y)
    stack = [start_node]

    while stack:
        x,y = stack.pop()

        # 주어진 범위를 벗어나면 무시
        if x < 0 or x >= n or y < 0 or y >= m:
            # 범위를 벗어나는 경우
            continue
        
        # 현재 노드를 아직 방문하지 않았다면,
        if graph[x][y] == 0:
            # 방문했을 때 1로 만듦
            graph[x][y] = 1
            # 인접 노드를 스택 추가
            stack.append((x-1,y)) # 좌노드
            stack.append((x+1,y)) # 우노드
            stack.append((x,y-1)) # 하노드
            stack.append((x,y+1)) # 상노드
            print("----이동 경로 확인----")
            print(stack)    # 노드 좌표
            for i in graph:
                print(i)
    return True

result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] ==0:
            if dfs_stack(i, j) == True:
                result += 1
print(f"얼음 개수:{result}")