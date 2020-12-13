d = input("Enter all street numbers of their houses: ").split()
mx = -1
ans = 999999999
for i in d:
    if int(i) > int(mx):
        mx = i
mx = int(mx)
for i in range(1, mx + 1):
    temp = 0
    for j in d:
        temp += abs(int(j) - int(i))
    if temp < ans:
        ans = temp
print("The shortest total distance:", ans)
