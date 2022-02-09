#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long x, y; cin >> x >> y;
  long long cnt = 0;
  while (x <= y) {
    cnt++;
    x *= 2;
  }
  cout << cnt << '\n';
  return 0;
}
