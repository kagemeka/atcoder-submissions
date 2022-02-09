#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int r, d, x;
  cin >> r >> d >> x;
  for (int i = 0; i < 10; i++) {
    x = r * x - d;
    cout << x << '\n';
  }
  return 0;
}
