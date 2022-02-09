#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long x;
  cin >> x;
  long long res = x / 11 * 2;
  int r = x % 11;
  if (r) {
    if (r <= 6) res++;
    else res += 2;
  }
  cout << res << '\n';
  return 0;
}
