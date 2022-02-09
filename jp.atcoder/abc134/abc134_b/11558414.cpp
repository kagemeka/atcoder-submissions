#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, d;
  cin >> n >> d;

  d = 2 * d + 1;
  cout << (n + d - 1) / d << '\n';
  return 0;
}
