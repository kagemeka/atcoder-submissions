#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long n, a, b;
  cin >> n >> a >> b;
  long long c = a + b;
  long long cnt = 0;
  if (c) {
    long long q, r;
    q = n / c;
    cnt += q * a;
    r = n % c;
    cnt += min(a, r);
  }
  cout << cnt << '\n';
  return 0;
}
