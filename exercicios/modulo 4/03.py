n1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
n3 = []

i = 0
while i < 10:
    n3.append(n1[i])
    n3.append(n2[i])
    i += 1

print(n1) 
print(n2)
print(n3)