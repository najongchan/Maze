#-*- coding: cp949 -*-
# IDS
# 나종찬

import sys
global ids_cost
global ids_goal_check

ids_goal_check = 0      # goal에 도달했는지 체크하는 flag
ids_cost = 0            # goal 까지 도달하는데 걸린 cost

class IDS :
    ids_road = list()       #   지나온 길을 저장할 리스트
    ids_depth = 0           #   Goal 까지 걸린 depth
    def Solve(self, maze):
        print "Start Searching by Using IDS"
        IDS.ids_road.append(maze.start)     #   시작점 추가

        maze.map[maze.start[0]][maze.start[1]]=2    #   지나온길 2로 마크

        while 1:             #   길찾는 함수 실행
            path_find(IDS.ids_road, maze, IDS.ids_depth)    # 지나온길, 미로, depth를 전달받는 함수
            IDS.ids_depth = IDS.ids_depth + 1       #   depth 1 증

def path_find(path, maze, depth):               # 길찾는 함수
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]    #   4방향을 찾는 변수 리스트
    global ids_cost                         #   코스트
    global ids_goal_check                   #   flag
    ids_cost = ids_cost + 1                 #   함수 호출시 cost 1 증가
    if depth < len(path):                   #   path 길이만큼 길 출력
        for i in range(0, 15):
            for j in range(0, 15):
                if maze.map[i][j] == 1:         #   1 = 벽
                    sys.stdout.write(" o ")     #   벽 = 'o'
                elif (maze.map[i][j] == 0):     #   0 = 갈 수 있는 길
                    sys.stdout.write(" . ")     #   길 = '.'
                else:
                    sys.stdout.write(" x ")     #  지나온길 = 'x'
            print ""                        # 줄바꿈
        print ""
        if ids_goal_check == 1:         # goal에 도달
            print ("cost : ")           # cost 출력
            print (ids_cost)
            print ("depth : " )          # depth 출력
            print(len(path))
        return                           # 함수 return
    elif len(path) > 0:                 #   지나온 길 찾는 부분
        for d in dir:                   #   dir 4방향 이용
            k = path[len(path)-1][0] + d[0]     #   현 위치 X 좌표
            l = path[len(path)-1][1] + d[1]     #   현 위치 Y 좌표
            if 0 <= k <15 and 0<= l <= 15 and ids_goal_check==0 :   # 맵 내부의 점인지 확인
                if maze.map[k][l] == 0:         #   길이 비어 있다면
                    path.append([k, l])         # 리스트에 추가
                    maze.map[k][l] = 2          #   2로 마크

                    if k==maze.goal[0] and l==maze.goal[1] :    #   goal에 도달시
                        ids_goal_check =1                       # flag =1
                    path_find(path, maze, depth)                #   재귀
                    current = path.pop()                        #   backtrack
                    maze.map[current[0]][current[1]] = 0        #   마크를 지움



