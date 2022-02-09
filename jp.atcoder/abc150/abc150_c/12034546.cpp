#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> p(n);
  vector<int> q(n);
  for (int i = 0; i < n; i++) cin >> p[i];
  for (int i = 0; i < n; i++) cin >> q[i];

  vector<long long> factorial(n + 1); factorial[0] = 1;
  for (int i = 1; i < n + 1; i++) {
    factorial[i] = factorial[i-1] * i;
  }

  bitset<100> a(0), b(0);
  long long d = 0;
  for (int i = 0; i < n - 1; i++) {
    a.set(p[i]); b.set(q[i]);
    int c1 = 0, c2 = 0;
    for (int j = 0; j < p[i]; j++) {
      c1 += a[j];
    }
    for (int j = 0; j < q[i]; j++) {
      c2 += b[j];
    }
    d += ((q[i] - c2) - (p[i] - c1)) * factorial[n - (i + 1)];
  }
  cout << abs(d) << '\n';
  return 0;
}
