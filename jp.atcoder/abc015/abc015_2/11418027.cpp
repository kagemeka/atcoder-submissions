#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, a, cnt = 0, tot = 0;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a;
    if (a) {
      cnt++;
      tot += a;
    }
  }
  cout << (tot + cnt - 1) / cnt << '\n';
  return 0;
}
