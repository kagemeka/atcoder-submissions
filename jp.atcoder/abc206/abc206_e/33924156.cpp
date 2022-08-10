#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int l, r;
  cin >> l >> r;
  l = max(l, 2);
  int const k = 1 << 20;
  vector<int> d(k);
  long res = 0;
  for(int i = l; i <= r; i++) {
    res -= d[i];
    for(int j = i * 2; j <= r; j += i) { d[j]++; }
  }
  vector<int> lpf(k);
  for(int i = 2; i < k; i++) {
    if(lpf[i] != 0) continue;
    for(int j = i; j < k; j += i) {
      if(lpf[j] == 0) lpf[j] = i;
    }
  }
  auto f = [&](int n) -> int {
    vector<int> exps;
    while(n > 1) {
      int p = lpf[n];
      n /= p;
      exps.push_back(p);
    }
    int cnt = exps.size();
    for(int i = 0; i < (int)exps.size() - 1; i++) {
      if(exps[i] == exps[i + 1]) return 0;
    }
    return cnt;
  };
  for(int i = 2; i <= r; i++) {
    int cnt = f(i);
    if(cnt == 0) continue;
    int sign = cnt & 1 ? 1 : -1;
    long c = r / i - (max(l, i) - 1) / i;
    res += c * (c - 1) / 2 * sign;
  }
  cout << res * 2 << endl;
}
