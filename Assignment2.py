import copy
from heapq import heappush, heappop
row = [1, 0, -1, 0]
column = [0,-1, 0, 1]

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        if not self.heap:
            return True
        else:
            return False


class node:
    def __init__(self, parent, mat, empty_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_pos = empty_pos
        self.cost = cost
        self.level = level

    def __lt__(self, nxt):
        return self.cost < nxt.cost


def newNode(mat, empty_pos, new_empty_pos, level, final, parent) -> node:
    new_mat = copy.deepcopy(mat)
    x1 = empty_pos[0]
    y1 = empty_pos[1]
    x2 = new_empty_pos[0]
    y2 = new_empty_pos[1]

    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    cost = CalculateCost(new_mat, final)

    new_node = node(parent, new_mat, new_empty_pos, cost ,level)

    return new_node

def printmat(mat):
    for i in range(n):
        for j in range(n):
            print("%d" % (mat[i][j]), end = " ")

        print()

def printsteps(root):
    if root == None:
        return

    printsteps(root.parent)
    printmat(root.mat)
    print()

def CalculateCost(mat , final) -> node:

    count = 0
    for i in range(n):
        for j in range(n):
            if ((mat[i][j]) and (mat[i][j] != final[i][j])):
                count+=1
    return count

def isSafe(x, y):

    return x >= 0 and x < n and y >= 0 and y < n

def findzero(initial,n):
    for i in range(n):
        for j in range(n):
            if initial[i][j] == 0:
                empty_pos = [i,j]
    return empty_pos

def solution(initial, final,empty_pos):

    pq = PriorityQueue()

    cost = CalculateCost(initial, final)
    root = node(None, initial, empty_pos, cost, 0)

    pq.push(root)

    while not pq.empty():

        minimum = pq.pop()

        if minimum.cost == 0:
            printsteps(minimum)
            return


        for i in range(n):
            new_tile_pos = [minimum.empty_pos[0] + row[i] , minimum.empty_pos[1] + column[i],]

            if isSafe(new_tile_pos[0], new_tile_pos[1]):

                child = newNode(minimum.mat, minimum.empty_pos, new_tile_pos, minimum.level + 1, final, minimum, )

                pq.push(child)
                #print(pq.empty())

initial = [ [ 1, 2, 3 ],
		    [ 5, 6, 0 ],
			[ 7, 8, 4 ] ]


final = [ [ 1, 2, 3 ],
		[ 5, 8, 6 ],
		[ 0, 7, 4 ] ]

n = 3;
empty_pos = findzero(initial,n)
solution(initial,final,empty_pos)