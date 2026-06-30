import sys
from collections import deque

with open("848/paranteze1.in", "r") as f:
    n = int(f.readline())
    parant_list = [line.rstrip("\n") for line in f]

ans = []

for p in parant_list:
    st = deque()
    nuareinchis = True
    for pz in p:
        if pz == "(":
            st.append(pz)
        if pz== ")":
            if st:
                st.pop()
            else:
                nuareinchis = False
                break
    if not st and nuareinchis:
        ans.append("1")
    else:
        ans.append("0")

with open("848/paranteze1.out", "w") as f:
    f.write("\n".join(ans))
        

