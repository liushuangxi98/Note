import os
import string
def print_chess(arr):
    for i in arr:
        i = list(map(str,i))
        print('  '.join(i))

def is_win(arr):
    for i in arr[1:]:
        for j in i:
            for z in ['x', 'y', 'z']:
                if z == 'x':
                    five = [arr[i+1][j+1+r] for r in range(5)]
                    if five == [1,1,1,1,1]:
                        return 'a win'
                    if five == [2,2,2,2,2]:
                        return 'b win'
                if z == 'x':
                    five = [arr[i+1+r][j+1] for r in range(5)]
                    if five == [1,1,1,1,1]:
                        return 'a win'
                    if five == [2,2,2,2,2]:
                        return 'b win'
                if z == 'x':
                    five = [arr[i+1+r][j+1+r] for r in range(5)]
                    if five == [1,1,1,1,1]:
                        return 'a win'
                    if five == [2,2,2,2,2]:
                        return 'b win'
    return 'no win'
size = 15
crood = string.ascii_lowercase
arr = [[0 for i in range(size)] for j in range(size)]
arr[0] = [i for i in crood[0:size]]
for idx, var in enumerate(crood[0:size]):
    arr[idx][0] = var
print_chess(arr)
while True:
    player_a_x, player_a_y = [crood.index(i) for i in list(input())[::-1]]
    arr[player_a_x][player_a_y] = 1
    print_chess(arr)
    if is_win(arr):
        break
    player_b_x, player_b_y = [crood.index(i) for i in list(input())[::-1]]
    arr[player_b_x][player_b_y] = 2
    print_chess(arr)
    if is_win(arr):
        break