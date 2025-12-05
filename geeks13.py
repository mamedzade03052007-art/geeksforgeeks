from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(f'{stack.pop()} popped from stack')
print(f'Top element is: {stack[-1]}' if stack else 'Stack is empty')