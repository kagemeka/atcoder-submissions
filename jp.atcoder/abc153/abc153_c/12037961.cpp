#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k; cin >> n >> k;
  vector<int> h(n);
  for (int i = 0; i < n; i++) cin >> h[i];
  sort(h.begin(), h.end(), greater<int>());
  for (int i = 0; i < n - 1; i++) h[i+1] += h[i];
  cout << h[n-1] - h[0] << '\n';
  return 0;

}
