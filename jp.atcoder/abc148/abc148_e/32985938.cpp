#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  long n;
  cin >> n;

  if (n & 1) {
    cout << 0 << endl;
  }
  long cnt = 0;
  long p = 2;
  while (p < n) {
    p *= 5;
    cnt += n / p;
  }
  cout << cnt << endl;
}
