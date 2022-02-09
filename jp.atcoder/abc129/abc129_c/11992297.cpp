#include <bits/stdc++.h>
using namespace std;
int MOD = 1e9 + 7;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  bitset<1001001> broken(0);
  for (int i = 0; i < m; i++) {
    int a; cin >> a;
    broken.set(a);
  }
  vector<int> ways(n + 1);
  ways[0] = 1;
  if (!broken[1]) ways[1] = 1;
  for (int i = 2; i < n + 1; i++) {
    if (!broken[i]) ways[i] = (ways[i-1] + ways[i-2]) % MOD;
  }
  cout << ways[n] << '\n';
  return 0;
}
