#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int w, a, b;
  cin >> w >> a >> b;
  if (b > a) swap(a, b);
  cout << max(0, a - (b + 3)) << '\n';
  return 0;
}
