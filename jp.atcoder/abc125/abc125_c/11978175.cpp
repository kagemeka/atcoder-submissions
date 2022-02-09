#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {return b ? gcd(b, a % b) : abs(a);}
long long lcm(long long a, long long b) {return abs(a / gcd(a, b) * b);}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n; cin >> n;
  vector<int>  a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  vector<int> lg(n), rg(n);
  for (int i = 1; i < n; i++) lg[i] = gcd(lg[i-1], a[i-1]);
  for (int i = n-2; i > -1; i--) rg[i] = gcd(rg[i+1], a[i+1]);
  int res = 1;
  for (int i = 0; i < n; i++) {
    res = max(res, (int)gcd(lg[i], rg[i]));
  }
  cout << res << '\n';
  return 0;

}
