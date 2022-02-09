n = int(input())
s = input()

ans = ['S'] * n
if s[0]  == 'x':
    ans[1] = 'W'
for i in range(1, n-1):
    if ans[i] == 'S':
        if s[i] == 'x' and ans[i-1] == 'S':
            ans[i+1] = 'W'
        elif s[i] == 'o' and ans[i-1] == 'W':
            ans[i+1] = 'W'
    else:
        if s[i] == 'o' and ans[i-1] == 'S':
            ans[i+1] = 'W'
        elif s[i] == 'x' and ans[i-1] == 'W':
            ans[i+1] = 'W'

print(ans)
ok = False
if ans[n-1] == 'S':
    if (s[n-1] == 'o' and ans[n-2] == 'S') or (s[n-1] == 'x' and ans[n-2] == 'W'):
        ok = True
else:
    if (s[n-1] == 'x' and ans[n-2] == 'S') or (s[n-i] == 'o' and ans[n-2] == 'W'):
        ok = True

if ok:
    print(''.join(ans))
else:
    print(-1)
