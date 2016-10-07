#-*- coding: cp949 -*-
# ASTAR
# ������

import sys

class Node:                     # node Ŭ����
    def __init__(self, pos, parent, cur_cost, maze):        # initialize
        self.pos=pos                                            #   ��� ��ǥ
        self.parent = parent                                    #   �θ���
        self.cost = cur_cost                                    #   ���� cost = g
        self.f = cur_cost + (abs(pos[0]-maze.goal[0]) + abs(pos[1] - maze.goal[1]))     # f = g + h (h�� ����ź���Ͻ�)
        self.next_node = None                                   #   ���� ��带 ����Ŵ
        self.link=[]                                            #   Linked_list

class ASTAR :                               #       ASTAR Ŭ����
    def Solve(self, maze) :                 #   maze solver
        print "Start Searching by Using A Star"
        node_list = Node(maze.start, None, 0, maze)     #   ��� ��带 ������ Linked_list
        maze.map[node_list.pos[0]][node_list.pos[1]]=2  #   start ����
        astar_cost = 0              #   cost �� �ʱ�ȭ
        astar_depth = 0             #   depth �� �ʱ�ȭ

        while node_list.pos != maze.goal:       #   ����� ���� ��ġ�� goal �� �ƴѰ�� �ݺ�
            path_find(node_list,maze)           #   �� ã�� �Լ�
            if len(node_list.link) > 0:         #   ����Ʈ�� ���� ��ŭ
                for node_i in node_list.link:
                    insertion_sort(node_i, node_list)  #   ����Ʈ ����
            maze.map[node_list.pos[0]][node_list.pos[1]] = 2    #   ������ �� ǥ��
            astar_cost = astar_cost+1       #   cost �� ����
            node_list = node_list.next_node                 #   ���� ���� �̵�
            for i in range(0, 15):                      #   maze_map ���
                for j in range(0, 15):
                    if (maze.map[i][j] == 1):           #   �� = 1
                        sys.stdout.write(' o ')          #   �� = ' o '
                    elif (maze.map[i][j] == 0):         #   ����� = 0
                        sys.stdout.write(' . ')          #   ����� = ' . '
                    else:
                        sys.stdout.write(' x ')         #   �������� = ' x '
                print ""                                # �ٹٲ�
            print ""

        if node_list.pos == maze.goal :                 #   goal�� �����ϸ�
            maze.map[maze.goal[0]][maze.goal[1]]=2      #   goal ��ũ

            for i in range(0, 15):                  #   maze.map ���
                for j in range(0, 15):
                    if (maze.map[i][j] == 1):
                        sys.stdout.write(' o ')
                    elif (maze.map[i][j] == 0):
                        sys.stdout.write(' . ')
                    else:
                        sys.stdout.write(' x ')
                print ""
            print ""

            print "cost: "                      #   cost ���
            print astar_cost

            print "depth: "                     #   depth ���
            depth_finder = node_list            # depth_finder �⵿
            while depth_finder != None:         #   goal���� start ���� d
                depth_finder = depth_finder.parent      #   parent�� ã���鼭
                astar_depth = astar_depth + 1           #   depth 1�� ����
            print astar_depth

def path_find(cur_node, maze):                  #   �� Ž�� �Լ�
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]      # �����¿� 4����
    for d in dir:                                # 4���� Ž��
        k = cur_node.pos[0] + d[0]
        l = cur_node.pos[1] + d[1]
        if(0 <= k < len(maze.map) and 0 <= l <len(maze.map[0])):    #   Map ũ�� ������
            if maze.map[k][l]==0:                                       # 0 �̸�
                cur_node.link.append(Node([k,l],cur_node, cur_node.cost + 1 ,maze))     #   �濡 �߰�


# f ���� ���� ���� ������ Linked_list ����
def insertion_sort(current, node_list):            # sort
    front_node = node_list                        # �տ� �� Node
    back_node = node_list.next_node               # �ڿ� �� Node

    if (node_list.f >= current.f):              #   f  ���� current ���� ������
        front_node = node_list.next_node        #   current �� ��ġ �̵�
        node_list.next_node = current           #
        current.next_node = front_node
        return

    while front_node != None:                   #   front_node �� ������ �� ����
        if front_node.next_node == None :       #   front_node �� ���̸�?
            front_node.next_node = current      #   current �� �� �ڿ� ���δ�
            break                               #   �ݺ��� Ż��
        elif front_node.f < current.f :         #   fornt �� f ���� �� �۴ٸ�
            if(back_node.f >= current.f):       #   ���� ����� f ���� current�� f ���� ũ�ٸ�
                front_node.next_node = current
                current.next_node = back_node   #   ���̿� ����
                break
            else:                               #   ���� ����� f  ���� �� ������
                back_node = back_node.next_node     #   back_node �ڷ� �̵�
                front_node = front_node.next_node   #   front_node �ڷ� �̵�


