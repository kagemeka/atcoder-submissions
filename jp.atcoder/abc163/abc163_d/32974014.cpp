#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  cin >> n >> k;

  const int mod = 1000000007;

  vector<long> s0(n + 1), s1(n + 1);
  for (int i = 0; i < n + 1; i++) {
    s0[i] = i;
    s1[i] = n - i;
  }
  for (int i = 0; i < n; i++) {
    s0[i + 1] += s0[i];
    s1[i + 1] += s1[i];
  }

  long tot = 0;
  for (int i = k - 1; i < n + 1; i++) {
    tot += s1[i] - s0[i] + 1;
    tot %= mod;
  }
  cout << tot << endl;
}
