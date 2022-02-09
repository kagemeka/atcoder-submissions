#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long n, m;
  cin >> n >> m;
  long long res = 0;
  if (n >= m / 2) res = m / 2;
  else {
    res = n;
    m -= n * 2;
    res += m / 4;
  }
  cout << res << '\n';
  return 0;
}
