#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k; cin >> n >> k;
  vector<long long> h(n + 1);
  for (int i = 1; i < n + 1; i++) cin >> h[i];
  sort(h.begin(), h.end());
  for (int i = 0; i < n; i++) h[i+1] += h[i];
  cout << h[max(0, n - k)] << '\n';
  return 0;
}
