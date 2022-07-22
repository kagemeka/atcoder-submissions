#include <bits/stdc++.h>
using namespace std;
template<typename T, typename N> auto power(T x, N n) -> T {
  T y = 1;
  while(n) {
    if(n & 1) y *= x;
    x *= x;
    n >>= 1;
  }
  return y;
}
auto main() -> int {
  int k;
  cin >> k;
  vector<int> cnt(k + 1);
  for(int i = k; i >= 1; i--) {
    cnt[i] = power(k / i, 3);
    for(int j = i * 2; j <= k; j += i) cnt[i] -= cnt[j];
  }
  int s = 0;
  for(int i = 0; i < k + 1; i++) { s += cnt[i] * i; }
  cout << s << endl;
}
