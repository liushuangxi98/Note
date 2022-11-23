import re
import string

while True:
    n = int(input())
    matrix_dict = {i: list(map(int, input().split(' '))) for i in string.ascii_uppercase[0:n]}
    rule = input()
    counts = 0
    while True:
        temp_replace = re.findall('\(\w\w\)', rule)
        if temp_replace:
            temp_replace = temp_replace[0]
            A = matrix_dict.get(temp_replace[1:3][0])
            B = matrix_dict.get(temp_replace[1:3][1])
            new_matrix, count = [A[0], B[1]], A[0] * B[1] * A[1]
            matrix_dict.update({temp_replace[1:3][0].lower():new_matrix})
            counts+=count
            rule = rule.replace(temp_replace,temp_replace[1:3][0].lower())
        else:
            break
    print(counts)

