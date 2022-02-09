#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int x;
  cin >> x;
  int res = 1;
  for (int i = 2; i < floor(sqrt(x)) + 1; i++) {
    res = max(res, (int)pow(i, (int)(log(x) / log(i) + 0.0001)));
  }
  cout << res << '\n';
  return 0;
}
