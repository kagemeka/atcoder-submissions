n = int(input())
cards = [int(a) for a in input().split()]
pairwise_distincts = set(cards)

if (len(cards) - len(pairwise_distincts)) % 2 == 0:
    ans = len(pairwise_distincts)
else:
    ans = len(pairwise_distincts) - 1

print(ans)
