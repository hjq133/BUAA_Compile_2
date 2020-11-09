import sys

priority = {'+': {'+': 1, '*': -1, 'i': -1, '(': -1, ')': 1, '#': 1},
            '*': {'+': 1, '*': 1, 'i': -1, '(': -1, ')': 1, '#': 1},
            'i': {'+': 1, '*': 1, 'i': None, '(': None, ')': 1, '#': 1},
            '(': {'+': -1, '*': -1, 'i': -1, '(': -1, ')': 0, '#': None},
            ')': {'+': 1, '*': 1, 'i': None, '(': None, ')': 1, '#': 1},
            '#': {'+': -1, '*': -1, 'i': -1, '(': -1, ')': None, '#': -9}
            }
grammar = ["E+E", "E*E", "(E)", "i"]

if sys.argv[0] == '/home/hjq133/myDesktop/编译作业/BUAA_Compile_2/main2.py':
    file_path = '../data.txt'
else:
    file_path = sys.argv[1]
stack = []

f = open(file_path, 'r')
l = f.readlines()[0].strip()
l = l + "#"
lst = list(l)


def analyze():
    stack.append("#")

    i = 0
    while i < len(lst):
        # 寻找栈中第一个终结符
        ch = lst[i]
        j = len(stack) - 1
        while stack[j] == 'E':
            j -= 1

        if priority[stack[j]][ch] == -1 or priority[stack[j]][ch] == 0:  # < =
            move_in(ch)
            i += 1
        elif priority[stack[j]][ch] == 1:  # >
            reduction(j)
        elif priority[stack[j]][ch] == -9:
            break
        else:
            print("E")
            exit(0)

    if ''.join(stack) != "#E":
        print("RE")
        exit(0)

    return


def move_in(ch):
    print('I{}'.format(ch))
    stack.append(ch)


def reduction(j):  # i 栈外字符, j: 栈中第一个终结符
    i = j
    k = j-1
    global stack
    while stack[k] == 'E':  # 寻找栈中下一个终结符
        k -= 1
    while priority[stack[k]][stack[i]] != -1:  # 一直找到 < 符号
        i = k
        k -= 1
        while stack[k] == 'E':  # 寻找栈中下一个终结符
            k -= 1
    if ''.join(stack[k+1:]) in grammar:
        print("R")
        stack = stack[:k+1]
        stack.append("E")
    else:
        print("RE")
        exit(0)
    # k j 为待归约字符串


analyze()
exit(0)
