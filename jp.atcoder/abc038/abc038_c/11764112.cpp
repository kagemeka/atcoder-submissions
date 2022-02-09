#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> a(n + 1);
  for (int i = 0; i < n; i++) cin >> a[i];
  a[n] = 0;

  long long res = 0;
  long long cnt = 0;
  int prev = 1001001001;
  for (int &x : a) {
    if (x <= prev) {
      res += cnt * (cnt - 1) / 2 + cnt;
      cnt = 1;
    } else {
      cnt++;
    }
    prev = x;
  }
  cout << res << '\n';
  return 0;
}
