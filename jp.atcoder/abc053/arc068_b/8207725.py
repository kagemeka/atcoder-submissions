n = int(input())
cards = [int(a) for a in input().split()]
pairwise_distincts = set(cards)
number = len(pairwise_distincts)
if (len(cards) - number) % 2 == 0:
    ans = number
else:
    ans = number - 1

print(ans)
