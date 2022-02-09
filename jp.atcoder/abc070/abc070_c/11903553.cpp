#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {return b ? gcd(b, a % b) : abs(a);}
long long lcm(long long a, long long b) {return abs(a / gcd(a, b) * b);}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  long long res = 1;
  for (int i = 0; i < n; i++) {
    long long t; cin >> t;
    res = lcm(res, t);
  }
  cout << res << '\n';
  return 0;
}
