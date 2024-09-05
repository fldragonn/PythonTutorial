s = 0
c = 0
for i in range(1000, 3001, 2):
    s += i
    c += 1
a = s / c
print(f'합: {s}')
print(f'평균: {a}')
