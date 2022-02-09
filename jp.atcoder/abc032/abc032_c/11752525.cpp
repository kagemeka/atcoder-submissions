#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < n; i++) {
    if (a[i] == 0) {
      cout << n << '\n';
      return 0;
    }
  }
  a.push_back(k + 1);
  int res = 0;
  long long tmp = 1;
  int l = 0;
  for (int r = 0; r < n + 1; r++) {
    tmp *= a[r];
    if (tmp > k) {
      res = max(res, r - l);
      while (tmp > k) {
        tmp /= a[l];
        l++;
        if (l > r) break;
      }
    }
  }
  cout << res << '\n';
  return 0;
}
