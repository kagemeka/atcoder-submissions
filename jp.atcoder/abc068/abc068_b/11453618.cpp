#include <bits/stdc++.h>
using namespace std;

int pow(long long x, long long n, int p) {
  if (n == 0) return 1;
  x %= p;
  if (n == 1) return x;
  if (n % 2) return (x * pow(x, n - 1, p) % p);
  long long y = pow(x, n / 2, p);
  return y * y % p;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  cout << pow(2, floor(log2(n)), 1e9 + 7) << '\n';
  return 0;
}
