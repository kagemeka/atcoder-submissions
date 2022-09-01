#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  int const k = 1 << 20;
  vector<int> f(k);
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(auto& x: a) f[x]++;
  vector<bool> is_prime(k, true);
  for(int i = 2; i < k; i++) {
    if(!is_prime[i]) continue;
    for(long j = (long)i * i; j < k; j += i) is_prime[j] = false;
    for(int j = 1; j <= (k - 1) / i; j++) f[j * i] += f[j];
  }
  int cnt = 0;
  for(auto& x: a) cnt += f[x] == 1;
  cout << cnt << '\n';
}
