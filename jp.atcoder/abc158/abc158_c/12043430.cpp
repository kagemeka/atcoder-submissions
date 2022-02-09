#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int a, b; cin >> a >> b;
  int ans = -1;
  for (int i = 1; i < 2000; i++) {
    if (i * 8 / 100 == a && i / 10 == b) {
      ans = i;
      break;
    }
  }
  cout << ans << '\n';
  return 0;
}
