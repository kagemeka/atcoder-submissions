import string
s = input()
size = len(s)
alpha_counts = {letter: 0 for letter in string.ascii_lowercase}
count = 0
ans = []
for times in range(1, size+1):
    for j in range(times-1, size):
        alpha = s[j]
        alpha_counts[alpha] += 1
        count += 1
        ans.append(alpha)
        if alpha_counts[alpha] > count/2:
            if count >= 2:
                print(''.join(ans))
                exit()
    else:
        alpha_counts = {letter: 0 for letter in string.ascii_lowercase}
        ans = []
        count = 0
else:
    print("-1, -1")
