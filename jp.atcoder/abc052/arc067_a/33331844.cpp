#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  int const k = 1 << 10;
  vector<int> cnt(k);
  for(int i = 1; i <= n; i++) {
    int x = i;
    for(int i = 2; i * i <= x; i++) {
      while(x % i == 0) {
        cnt[i]++;
        x /= i;
      }
    }
    if(x > 1) { cnt[x]++; }
  }
  long const mod = 1000000007;
  long p = 1;
  for(int i = 0; i < k; i++) {
    p *= (cnt[i] + 1);
    p %= mod;
  }
  cout << p << endl;
}