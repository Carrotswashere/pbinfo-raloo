from collections import deque

st = deque()
cubsno = int(input())
cubs = [0] * (cubsno)
cubs = input().split()
cubs0 = cubs

for latura in cubs:
    if len(st) == 0:
        st.append(latura)
        continue
    if latura <= st[-1]:
        st.append(latura)
    if latura > st[-1]:
        while st and latura > st[-1]:
            st.pop()
        st.append(latura)

indexes = []
  
for  i,item in enumerate(cubs0, start=1):
    if item in st:
        indexes.append(i)

print(len(indexes))
print(*indexes)
