#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, p;
  string s;
  cin >> n >> p >> s;
  reverse(s.begin(), s.end());
  vector<int> a(n + 1);
  for(int i = 0; i < n; i++) a[i + 1] = s[i] - '0';
  if(p == 2 || p == 5) {
    long cnt = 0;
    for(int i = 0; i < n; i++) {
      if(a[i] % p != 0) continue;
      cnt += n - i;
    }
    cout << cnt << endl;
    return 0;
  }
  int b = 1;
  for(int i = 0; i < n; i++) {
    a[i + 1] = (a[i + 1] * b + a[i]) % p;
    b *= 10;
    b %= p;
  }
  vector<int> c(p);
  long cnt = 0;
  for(auto& x: a) { cnt += c[x]++; }
  cout << cnt << endl;
}
