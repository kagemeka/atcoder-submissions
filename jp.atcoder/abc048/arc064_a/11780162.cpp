#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, x;
  cin >> n >> x;
  vector<int> a(n + 1);
  for (int i = 1; i < n + 1; i++) cin >> a[i];
  long long tot = 0;
  for (int i = 1; i < n + 1; i++) {
    tot += max(a[i-1] + a[i] - x, 0);
    a[i] = min(x - a[i-1], a[i]);
  }
  cout << tot << '\n';
  return 0;
}
