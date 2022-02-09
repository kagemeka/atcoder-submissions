n = int(input())
s = input()

def loop():
    for i in range(1, n-1):
        if ans[i] == 'S':
            if s[i] == 'x':
                if ans[i-1] == 'S':
                    ans[i+1] = 'W'
                else:
                    ans[i+1] = 'S'
            else:
                if ans[i-1] == 'W':
                    ans[i+1] = 'W'
                else:
                    ans[i+1] = 'S'
        else:
            if s[i] == 'o':
                if ans[i-1] == 'S':
                    ans[i+1] = 'W'
                else:
                    ans[i+1] = 'S'
            else:
                if ans[i-1] == 'W':
                    ans[i+1] = 'W'
                else:
                    ans[i+1] = 'S'

ans = ['S'] * n
if s[0]  == 'x':
    ans[1] = 'W'
else:
    ans[1] = 'S'
loop()
if ans[n-1] == 'S':
    if (s[n-1] == 'o' and ans[n-2] == 'S') or (s[n-1] == 'x' and ans[n-2] == 'W'):
        print(''.join(ans))
        exit()

ans = ['W'] * n
if s[0]  == 'x':
    ans[1] = 'W'
else:
    ans[1] = 'S'
loop()
if ans[n-1] == 'W':
    if (s[n-1] == 'x' and ans[n-2] == 'W') or (s[n-1] == 'o' and ans[n-2] == 'S'):
        print(''.join(ans))
        exit()

ans = ['W'] * (n-1) + ['S']
if s[0]  == 'x':
    ans[1] = 'S'
else:
    ans[1] = 'W'
loop()
if ans[n-1] == 'S':
    if (s[n-1] == 'x' and ans[n-2] == 'S') or (s[n-1] == 'o' and ans[n-2] == 'W'):
        print(''.join(ans))
        exit()

ans = ['S'] * (n-1) + ['W']
if s[0]  == 'x':
    ans[1] = 'S'
else:
    ans[1] = 'W'
loop()
if ans[n-1] == 'W':
    if (s[n-1] == 'x' and ans[n-2] == 'S') or (s[n-1] == 'o' and ans[n-2] == 'W'):
        print(''.join(ans))
        exit()

print(-1)
