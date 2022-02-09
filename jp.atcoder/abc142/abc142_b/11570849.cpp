#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  vector<int> h(n);
  for (int i = 0; i < n; i++) cin >> h[i];
  sort(h.begin(), h.end());
  cout << n - (lower_bound(h.begin(), h.end(), k) - h.begin()) << '\n';
  return 0;
}
