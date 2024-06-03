for i in range(1, 21, 2):
    print(i, end=' ')
print()

for a in range(0, 101, 10):
    print(a, end=' ')
print()

for b in range(20, 0, -1):
    print(b, end=' ')
print()

user_enter = int(input("Number of stars: "))
for c in range(0, user_enter):
    print("*", end=' ')
print()

for x in range(0, user_enter):
    print()
    for y in range(0, x+1):
        print("*", end=' ')

