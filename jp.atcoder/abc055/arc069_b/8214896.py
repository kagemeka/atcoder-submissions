n = int(input())
s = input()

ans = ['S'] * n
for i in range(n-1):
    if ans[i] == 'S':
        if s[i] == 'x':
            ans[i+1] = 'W'
    else:
        if s[i] == 'o':
            if ans[i-1] == 'S':
                ans[i+1] = 'W'
            else:
                ans[i+1] = 'S'
        else:
            if ans[i-1] == 'W':
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
