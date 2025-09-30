ice_map = [
    [0,0,1,1,0],    
    [0,0,0,1,1],    
    [1,1,1,1,1],    
    [0,0,0,0,0],    
    ]
# 얼음 여부를 확인해야하는 범위가 얼마나 되는지 알기 위해
n = len(ice_map)
m = len(ice_map[0])

# 스택을 활용한 DFS 구현
# graph, star_node
def dfs_stack(x,y):
    star_node = (x, y)
    stack = [star_node]
    # stack이 비워지면 얼음 하나 확인!
    while stack:
        x,y = stack.pop() 
        # 주어진 범위를 벗어나면 무시
        if x < 0 or x >= n  or y <0 or y >= m:
            # 범위를 벗어나는 경우
            continue           

        # 현재 노드를 아직 방문하지 않았다면,
        if ice_map[x][y] == 0:
            # 방문 처리
            ice_map[x][y] = 1
            # 인접 노드를 스택 추가
            stack.append((x+1,y))
            stack.append((x-1,y))
            stack.append((x,y+1))
            stack.append((x,y-1))
            # print("----이동 경로 확인----")
                

           
    # 얼음의 확인 여부  반환            
    return True



        # 한번 카운트 된 얼음은 다시 카운트 되면 안되므로
result = 0

for i in range(n):
    for j in range(m):
        if ice_map[i][j] == 0:
            if dfs_stack(i,j) == True:    
                result += 1
      

print(f"result {result}")

