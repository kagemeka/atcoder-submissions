#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int h, n;
  cin >> h >> n;
  int s = 0;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    s += a;
  }
  string ans = (s >= h) ? "Yes" : "No";
  cout << ans << '\n';
  return 0;
}
