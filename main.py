sign_map = {'+': 0,
            '*': 1,
            'i': 2,
            '(': 3,
            ')': 4
            }

matrix = [
    [1, -1, -1, -1, 1],
    [1, 1, 1, 1, -1],
    [1, 1, None, None, 1],
    [-1, -1, -1, -1, 0],
    [1, 1, None, None, 1]
]

file_path = input()

stack = []
vn_stack = []

f = open(file_path, 'r')
l = f.readlines()[0].strip()
lst = list(l)

i = 0
while i < len(lst):
    ch = lst[i]
    if ch not in sign_map.keys():
        print('E')
        exit(0)

    index = sign_map[ch]
    if len(stack) == 0:  # 栈为空
        stack.append(index)
        print('I{}'.format(ch))
        i += 1
        continue

    priority = matrix[stack[-1]][index]  # 栈顶优先级
    if priority == -1 or priority == 0:  # 栈内 >= 栈外, 移进
        stack.append(index)
        i += 1
        print('I{}'.format(ch))

    elif priority == 1:  # 栈内 > 栈外
        tmp = len(stack) - 1
        if stack[tmp] == 2:
            pass
        elif (tmp == 0 or matrix[stack[tmp - 1]][stack[tmp]] == -1 or matrix[stack[tmp - 1]][stack[tmp]] == 0) and len(
                vn_stack) != 0:  # 栈内 < 栈外
            vn_stack.pop()
        else:
            print("RE")
            exit(0)

        vn_stack.append(1)
        stack = stack[:tmp]
        print("R")
        continue
    else:
        print('E')
        exit(0)

while len(stack) != 0:
    tmp = len(stack) - 1
    if stack[tmp] == 2:
        pass
    elif (tmp == 0 or matrix[stack[tmp - 1]][stack[tmp]] == -1 or matrix[stack[tmp - 1]][stack[tmp]] == 0) and len(
            vn_stack) != 0:  # 栈内 < 栈外
        vn_stack.pop()
    else:
        print("RE")
        exit(0)
    vn_stack.append(1)
    stack = stack[:tmp]
    print("R")
    continue
