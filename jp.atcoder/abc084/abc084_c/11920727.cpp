#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> c(n-1);
  vector<int> s(n-1);
  vector<int> f(n-1);
  for (int i = 0; i < n - 1; i++) {
    cin >> c[i] >> s[i] >> f[i];
  }
  for (int i = 0; i < n - 1; i++) {
    int t = 0;
    for (int j = i; j < n - 1; j++) {
      if (t <= s[j]) {
        t = s[j] + c[j];
      } else {
        t = s[j] + ((t - s[j] + f[j] - 1) / f[j]) * f[j] + c[j];
      }
    }
    cout << t << '\n';
  }
  cout << 0 << '\n';
  return 0;
}
