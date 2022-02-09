#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n; cin >> n;
  vector<int> a(n + 2);
  for (int i = 1; i < n + 1; i++) cin >> a[i];
  int s = 0;
  for (int i = 0; i < n + 1; i++) {
    s += abs(a[i+1] - a[i]);
  }
  for (int i = 1; i < n + 1; i++) {
    int res;
    if (a[i-1] <= a[i] && a[i] <= a[i+1]) res = s;
    else if (a[i-1] >= a[i] && a[i] >= a[i+1]) res = s;
    else res = s - 2 * min(abs(a[i] - a[i-1]), abs(a[i+1] - a[i]));
    cout << res << '\n';
  }
  return 0;
}
