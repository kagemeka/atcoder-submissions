a, b = [int(x) for x in input().split()]

if a == b:
    print("Draw")
    exit()
elif a == 1:
    winner = "Alice"
elif b == 1:
    winner = "Bob"
elif a < b:
    winner = "Bob"
else:
    winner = "Alice"

print(winner)
