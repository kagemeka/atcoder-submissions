#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  long n;
  int x, m;
  cin >> n >> x >> m;
  vector<long> f(m);
  for(long i = 0; i < m; i++) f[i] = i * i % m;
  vector<long> s(m), idx(m, -1);
  int a = -1, b = -1, c = -1;
  s[0] = x;
  idx[x] = 0;
  for(int i = 0; i < m; i++) {
    x = f[x];
    if(idx[x] == -1) {
      idx[x] = i + 1;
      s[i + 1] = s[i] + x;
      continue;
    }
    a = idx[x];
    b = i + 1 - a;
    c = s[i] + x - s[a];
    break;
  }
  n--;
  if(n <= a) {
    cout << s[n] << endl;
    return 0;
  }
  long res = s[a];
  n -= a;
  res += n / b * c;
  n %= b;
  res += s[a + n % b] - s[a];
  cout << res << endl;
}
