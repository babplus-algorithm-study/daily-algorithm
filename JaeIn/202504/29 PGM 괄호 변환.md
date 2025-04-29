```python
from collections import deque

# 균형잡힌 괄호 문자열
def is_correct_string(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(':
            stack.append("(")
        elif str[i] == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

def separate_to_u_v(str):
    queue = deque(str)
    left_count , right_count = 0 , 0
    u , v = '' , ''

    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left_count += 1
        if char == ')':
            right_count += 1

        if left_count == right_count:
            break
    v = ''.join(queue)
    return u , v


def reverse_parentheses(str):
    reversed_str = ""
    for char in str:
        if char == "(":
            reversed_str += ")"
        elif char == ")":
            reversed_str += "("
    return reversed_str

def change_to_correct_parentheses(str):

    # 1번 요구사항
    if str == '':
        return ''

    # 2번 요구사항
    u , v = separate_to_u_v(str)

    # 3번 요구사항
    if is_correct_string(u):
        return u + change_to_correct_parentheses(v)
    else:
        return "(" + change_to_correct_parentheses(v) + ")" + reverse_parentheses(u[1:-1])


def solution(str):

    if is_correct_string(str):
        return str
    else:
        return change_to_correct_parentheses(str)

    return



```
