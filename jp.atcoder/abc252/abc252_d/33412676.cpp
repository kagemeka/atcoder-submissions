#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  auto f = [&](int n) -> long { return (long)n * (n - 1) >> 1; };
  int const k = 1 << 18;
  vector<int> cnt(k);
  for(auto& x: a) cnt[x]++;
  long s = (long)n * (n - 1) * (n - 2);
  for(int i = 0; i < k; i++) {
    long x = cnt[i];
    s -= x * (x - 1) * (x - 2);
    s -= 6l * (n - x) * f(x);
  }
  cout << s / 6 << endl;
}
