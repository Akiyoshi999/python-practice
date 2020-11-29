import math

N = int(input())
math_list = {}
max_length = 0

for n in range(N):
    x, y = (int(x) for x in input().split())
    xy_list = [x, y]
    math_list[n] = xy_list

for key in math_list.keys():
    for tar in math_list.keys():
        if key == tar:
            pass
        total = (math_list[key][0]-math_list[tar][0])**2 + \
            (math_list[key][1]-math_list[tar][1])**2
        total = math.sqrt(total)
        if max_length < total:
            max_length = total
print('{:.6f}'.format(max_length))
