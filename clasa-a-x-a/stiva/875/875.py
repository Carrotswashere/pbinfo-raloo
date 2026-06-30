#for python using deque can be faster for operations with large data

from collections import deque

st = deque()
tops = []
ops = int(input())
for i in range(ops):
    command = input().split()
    if command[0] == "pop":
        st.pop()
    if command[0] == "top" and len(st) > 0:
        tops.append(st[-1])
    if command[0] == "push":
        st.append(command[1])
        
        
for t in tops:
    print(f"{t}")