#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n + 1);
  vector<int> b(n);
  for (int i = 0; i < n + 1; i++) cin >> a[i];
  for (int i = 0; i < n; i++) cin >> b[i];
  long long tot = 0;
  for (int i = 0; i < n; i++) {
    tot += min(b[i], a[i]);
    b[i] = max(0, b[i] - a[i]);
    tot += min(b[i], a[i+1]);
    a[i+1] = max(0, a[i+1] - b[i]);
  }
  cout << tot << '\n';
  return 0;
}
