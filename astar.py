#-*- coding: cp949 -*-
# ASTAR
# 나종찬

import sys

class Node:                     # node 클래스
    def __init__(self, pos, parent, cur_cost, maze):        # initialize
        self.pos=pos                                            #   노드 좌표
        self.parent = parent                                    #   부모노드
        self.cost = cur_cost                                    #   현재 cost = g
        self.f = cur_cost + (abs(pos[0]-maze.goal[0]) + abs(pos[1] - maze.goal[1]))     # f = g + h (h는 맨하탄디스턴스)
        self.next_node = None                                   #   다음 노드를 가리킴
        self.link=[]                                            #   Linked_list

class ASTAR :                               #       ASTAR 클래스
    def Solve(self, maze) :                 #   maze solver
        print "Start Searching by Using A Star"
        node_list = Node(maze.start, None, 0, maze)     #   모든 노드를 저장할 Linked_list
        maze.map[node_list.pos[0]][node_list.pos[1]]=2  #   start 지점
        astar_cost = 0              #   cost 값 초기화
        astar_depth = 0             #   depth 값 초기화

        while node_list.pos != maze.goal:       #   노드의 현재 위치가 goal 이 아닌경우 반복
            path_find(node_list,maze)           #   길 찾기 함수
            if len(node_list.link) > 0:         #   리스트의 길이 만큼
                for node_i in node_list.link:
                    insertion_sort(node_i, node_list)  #   리스트 정렬
            maze.map[node_list.pos[0]][node_list.pos[1]] = 2    #   지나온 길 표시
            astar_cost = astar_cost+1       #   cost 값 증가
            node_list = node_list.next_node                 #   다음 노드로 이동
            for i in range(0, 15):                      #   maze_map 출력
                for j in range(0, 15):
                    if (maze.map[i][j] == 1):           #   벽 = 1
                        sys.stdout.write(' o ')          #   벽 = ' o '
                    elif (maze.map[i][j] == 0):         #   빈공간 = 0
                        sys.stdout.write(' . ')          #   빈공간 = ' . '
                    else:
                        sys.stdout.write(' x ')         #   지나간길 = ' x '
                print ""                                # 줄바꿈
            print ""

        if node_list.pos == maze.goal :                 #   goal에 도착하면
            maze.map[maze.goal[0]][maze.goal[1]]=2      #   goal 마크

            for i in range(0, 15):                  #   maze.map 출력
                for j in range(0, 15):
                    if (maze.map[i][j] == 1):
                        sys.stdout.write(' o ')
                    elif (maze.map[i][j] == 0):
                        sys.stdout.write(' . ')
                    else:
                        sys.stdout.write(' x ')
                print ""
            print ""

            print "cost: "                      #   cost 출력
            print astar_cost

            print "depth: "                     #   depth 출력
            depth_finder = node_list            # depth_finder 출동
            while depth_finder != None:         #   goal에서 start 까지 d
                depth_finder = depth_finder.parent      #   parent를 찾으면서
                astar_depth = astar_depth + 1           #   depth 1씩 증가
            print astar_depth

def path_find(cur_node, maze):                  #   길 탐색 함수
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]      # 상하좌우 4방향
    for d in dir:                                # 4방향 탐색
        k = cur_node.pos[0] + d[0]
        l = cur_node.pos[1] + d[1]
        if(0 <= k < len(maze.map) and 0 <= l <len(maze.map[0])):    #   Map 크기 내에서
            if maze.map[k][l]==0:                                       # 0 이면
                cur_node.link.append(Node([k,l],cur_node, cur_node.cost + 1 ,maze))     #   길에 추가


# f 값에 따라 작은 순서로 Linked_list 구현
def insertion_sort(current, node_list):            # sort
    front_node = node_list                        # 앞에 올 Node
    back_node = node_list.next_node               # 뒤에 올 Node

    if (node_list.f >= current.f):              #   f  값이 current 보다 높으면
        front_node = node_list.next_node        #   current 와 위치 이동
        node_list.next_node = current           #
        current.next_node = front_node
        return

    while front_node != None:                   #   front_node 가 끝까지 갈 동안
        if front_node.next_node == None :       #   front_node 가 끝이면?
            front_node.next_node = current      #   current 를 맨 뒤에 붙인다
            break                               #   반복문 탈출
        elif front_node.f < current.f :         #   fornt 의 f 값이 더 작다면
            if(back_node.f >= current.f):       #   뒤의 노드의 f 값이 current의 f 보다 크다면
                front_node.next_node = current
                current.next_node = back_node   #   사이에 삽입
                break
            else:                               #   뒤의 노드의 f  값이 더 작으면
                back_node = back_node.next_node     #   back_node 뒤로 이동
                front_node = front_node.next_node   #   front_node 뒤로 이동


