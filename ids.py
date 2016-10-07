#-*- coding: cp949 -*-
# IDS
# ������

import sys
global ids_cost
global ids_goal_check

ids_goal_check = 0      # goal�� �����ߴ��� üũ�ϴ� flag
ids_cost = 0            # goal ���� �����ϴµ� �ɸ� cost

class IDS :
    ids_road = list()       #   ������ ���� ������ ����Ʈ
    ids_depth = 0           #   Goal ���� �ɸ� depth
    def Solve(self, maze):
        print "Start Searching by Using IDS"
        IDS.ids_road.append(maze.start)     #   ������ �߰�

        maze.map[maze.start[0]][maze.start[1]]=2    #   �����±� 2�� ��ũ

        while 1:             #   ��ã�� �Լ� ����
            path_find(IDS.ids_road, maze, IDS.ids_depth)    # �����±�, �̷�, depth�� ���޹޴� �Լ�
            IDS.ids_depth = IDS.ids_depth + 1       #   depth 1 ��

def path_find(path, maze, depth):               # ��ã�� �Լ�
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]    #   4������ ã�� ���� ����Ʈ
    global ids_cost                         #   �ڽ�Ʈ
    global ids_goal_check                   #   flag
    ids_cost = ids_cost + 1                 #   �Լ� ȣ��� cost 1 ����
    if depth < len(path):                   #   path ���̸�ŭ �� ���
        for i in range(0, 15):
            for j in range(0, 15):
                if maze.map[i][j] == 1:         #   1 = ��
                    sys.stdout.write(" o ")     #   �� = 'o'
                elif (maze.map[i][j] == 0):     #   0 = �� �� �ִ� ��
                    sys.stdout.write(" . ")     #   �� = '.'
                else:
                    sys.stdout.write(" x ")     #  �����±� = 'x'
            print ""                        # �ٹٲ�
        print ""
        if ids_goal_check == 1:         # goal�� ����
            print ("cost : ")           # cost ���
            print (ids_cost)
            print ("depth : " )          # depth ���
            print(len(path))
        return                           # �Լ� return
    elif len(path) > 0:                 #   ������ �� ã�� �κ�
        for d in dir:                   #   dir 4���� �̿�
            k = path[len(path)-1][0] + d[0]     #   �� ��ġ X ��ǥ
            l = path[len(path)-1][1] + d[1]     #   �� ��ġ Y ��ǥ
            if 0 <= k <15 and 0<= l <= 15 and ids_goal_check==0 :   # �� ������ ������ Ȯ��
                if maze.map[k][l] == 0:         #   ���� ��� �ִٸ�
                    path.append([k, l])         # ����Ʈ�� �߰�
                    maze.map[k][l] = 2          #   2�� ��ũ

                    if k==maze.goal[0] and l==maze.goal[1] :    #   goal�� ���޽�
                        ids_goal_check =1                       # flag =1
                    path_find(path, maze, depth)                #   ���
                    current = path.pop()                        #   backtrack
                    maze.map[current[0]][current[1]] = 0        #   ��ũ�� ����



