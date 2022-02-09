#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  int h;
  int m = 0;
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    cin >> h;
    if (h >= m) {
      cnt++;
      m = h;
    }
  }
  cout << cnt << '\n';
  return 0;
}
