n = int(input())
ls = list(map(int, input().split()))
ls.sort(reverse=True)
alice_point = 0
bob_point = 0

for i in range(n):
  if i % 2 == 0:
    alice_point += ls[i]
  else:
    bob_point += ls[i]

difference = alice_point - bob_point
print(difference)
