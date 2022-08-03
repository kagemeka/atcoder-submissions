#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int dt;
  cin >> dt;
  int h = 21 + dt / 60;
  int m = dt % 60;
  printf("%02d:%02d", h, m);
}
