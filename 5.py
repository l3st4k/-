A, B = float(input()), float(input())
count = 0

while A >= B:
    A -= B
    count += 1
print(count)