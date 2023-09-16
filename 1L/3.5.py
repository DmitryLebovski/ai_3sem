

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_x = [x[i] for i in range(0, len(x), 2)]
even_x2 = even_x[::-1]
for i in range(0, len(x), 2):
    x[i] = even_x2[i//2]
print(x)

print(even_x)
print(even_x2)