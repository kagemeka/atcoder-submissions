#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, a, b;
  cin >> n >> a >> b;
  int c = a + b;
  int cnt = 0;
  if (c) {
    int q, r;
    q = n / c;
    cnt += q * a;
    r = n % c;
    cnt += min(a, r);
  }
  cout << cnt << '\n';
  return 0;
}
